from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import *
from django.db.models import Count, Avg, F
from django.utils import timezone

@api_view(['GET', 'POST'])
def vendor_list(request):
    if request.method == 'GET':
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def vendor_details(request, vendor_id):
    try:
        vendor = Vendor.objects.get(id=vendor_id)
    except Vendor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET'])
def vendor_performance(request, vendor_id):
    try:
        vendor = Vendor.objects.get(id=vendor_id)
    except Vendor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = VendorPerformanceSerializer(vendor)
    return Response(serializer.data)

def update_vendor_performance(vendor):
    # on time delivery rate
    completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
    on_time_delivery_count = completed_orders.filter(delivery_date__lte = timezone.now()).count()
    total_completed_count = completed_orders.count()
    
    if total_completed_count > 0:
        vendor.on_time_delivery_rate = (on_time_delivery_count / total_completed_count) * 100
    else:
        vendor.on_time_delivery_rate = 0.0
    
    # quality rating average
    quality_rating_avg = completed_orders.exclude(quality_rating__isnull=True).aggregate(avg_rating=Avg('quality_rating'))
    vendor.quality_rating = quality_rating_avg['avg_rating'] if quality_rating_avg['avg_rating'] else 0.0

    # avg response time
    response_times = completed_orders.exclude(acknowledgment_date__isnull=True).annotate(
        response_time= F('acknowledgment_date') - F('issue_date')
    ).aggregate(avg_response_time=Avg('response_time'))
    vendor.average_response_time = response_times['avg_response_time'].total_seconds() if response_times['avg_response_time'] is not None else 0.0

    # Calculate Fulfillment Rate
    total_po_count = PurchaseOrder.objects.filter(vendor=vendor).count()
    fulfilled_po_count = completed_orders.exclude(status='completed_with_issues').count()
    if total_po_count > 0:
        vendor.fulfillment_rate = (fulfilled_po_count / total_po_count) * 100
    else:
        vendor.fulfillment_rate = 0.0

    vendor.save()

@api_view(['POST'])
def acknowledge_purchase_order(request, po_id):
    try:
        purchase_order = PurchaseOrder.objects.get(pk=po_id)
    except PurchaseOrder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Update acknowledgment_date
    purchase_order.acknowledgment_date = timezone.now()
    purchase_order.save()

    # Recalculate average_response_time
    vendor = purchase_order.vendor
    update_vendor_performance(vendor)

    return Response("Purchase order acknowledged successfully.", status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def purchase_details(request):
    if request.method == 'GET':
        purchase = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(purchase, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def purchase_list(request, purchase_id):
    try:
        purchase = PurchaseOrder.objects.get(id=purchase_id)
    except PurchaseOrder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PurchaseOrderSerializer(purchase)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PurchaseOrderSerializer(purchase, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        purchase.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
