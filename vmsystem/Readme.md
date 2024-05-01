
# Vendor Management System with Performance Metrics

## Output:


https://github.com/ChandrashekharRobbi/Django/assets/91750738/7e5a0466-82fe-4989-9b53-209acc2356af


## Introduction

This Vendor Management System (VMS) is a Django-based web application designed to handle vendor profiles, track purchase orders, and calculate vendor performance metrics. The system provides APIs for managing vendors, purchase orders, and retrieving performance metrics.

## Installation

1. **Clone the Repository**: Clone the project repository from GitHub:

   ```
   git clone https://github.com/ChandrashekharRobbi/Django/edit/main/vmsystem/
   ```

2. **Create Virtual Environment**: Navigate to the project directory and create a virtual environment:

3. **Activate Virtual Environment**: Activate the virtual environment:

   

4. **Install Dependencies**: Install the project dependencies using pip:

   ```
   pip install -r requirements.txt
   ```

5. **Run Migrations**: Apply database migrations to create the database schema:

   ```
   python manage.py migrate
   ```

6. **Create Superuser (Optional)**: Create a superuser to access the Django admin interface:

   ```
   python manage.py createsuperuser
   ```

Here's the documentation for each API endpoint:

1. **Vendor List Endpoint**
   - **URL Pattern**: `/api/vendors/`
   - **HTTP Methods**: GET, POST
   - **Description**: This endpoint allows users to retrieve a list of all vendors or create a new vendor.
     - **GET**: Returns a list of all vendors with their details.
     - **POST**: Creates a new vendor with the provided details.
   - **Parameters**:
     - None for GET request.
     - JSON body with vendor details for POST request.
   - **Response**:
     - **GET**: Returns a JSON object containing details of all vendors.
     - **POST**: Returns the details of the newly created vendor if successful, along with status code 201 (Created). Returns error messages with status code 400 (Bad Request) if the request is invalid.

2. **Vendor Details Endpoint**
   - **URL Pattern**: `/api/vendors/<int:vendor_id>/`
   - **HTTP Methods**: GET, PUT, DELETE
   - **Description**: This endpoint allows users to retrieve, update, or delete details of a specific vendor.
     - **GET**: Returns details of the vendor with the specified ID.
     - **PUT**: Updates the details of the vendor with the specified ID.
     - **DELETE**: Deletes the vendor with the specified ID.
   - **Parameters**:
     - `vendor_id`: Integer ID of the vendor.
   - **Response**:
     - **GET**: Returns a JSON object containing details of the specified vendor if found, with status code 200 (OK). Returns status code 404 (Not Found) if the vendor does not exist.
     - **PUT**: Returns the updated details of the vendor if successful, along with status code 200 (OK). Returns error messages with status code 400 (Bad Request) if the request is invalid.
     - **DELETE**: Returns status code 204 (No Content) if the vendor is successfully deleted. Returns status code 404 (Not Found) if the vendor does not exist.

3. **Vendor Performance Endpoint**
   - **URL Pattern**: `/api/vendors/<int:vendor_id>/performance/`
   - **HTTP Method**: GET
   - **Description**: This endpoint allows users to retrieve the performance metrics of a specific vendor.
     - **GET**: Returns the performance metrics (on-time delivery rate, quality rating average, average response time, fulfillment rate) for the vendor with the specified ID.
   - **Parameters**:
     - `vendor_id`: Integer ID of the vendor.
   - **Response**:
     - Returns a JSON object containing the performance metrics of the specified vendor if found, with status code 200 (OK). Returns status code 404 (Not Found) if the vendor does not exist.

4. **Acknowledge Purchase Order Endpoint**
   - **URL Pattern**: `/api/purchase_orders/<int:po_id>/acknowledge/`
   - **HTTP Method**: POST
   - **Description**: This endpoint allows vendors to acknowledge a purchase order, updating the acknowledgment date and triggering recalculation of vendor performance metrics.
     - **POST**: Acknowledges the purchase order with the specified ID and triggers recalculation of vendor performance metrics.
   - **Parameters**:
     - `po_id`: Integer ID of the purchase order.
   - **Response**:
     - Returns a success message with status code 200 (OK) if the purchase order is successfully acknowledged. Returns status code 404 (Not Found) if the purchase order does not exist.

5. **Purchase Details Endpoint**
   - **URL Pattern**: `/api/purchase_orders/`
   - **HTTP Methods**: GET, POST
   - **Description**: This endpoint allows users to retrieve a list of all purchase orders or create a new purchase order.
     - **GET**: Returns a list of all purchase orders with their details.
     - **POST**: Creates a new purchase order with the provided details.
   - **Parameters**:
     - None for GET request.
     - JSON body with purchase order details for POST request.
   - **Response**:
     - **GET**: Returns a JSON object containing details of all purchase orders.
     - **POST**: Returns the details of the newly created purchase order if successful, along with status code 201 (Created). Returns error messages with status code 400 (Bad Request) if the request is invalid.

6. **Purchase List Endpoint**
   - **URL Pattern**: `/api/purchase_orders/<int:purchase_id>/`
   - **HTTP Methods**: GET, PUT, DELETE
   - **Description**: This endpoint allows users to retrieve, update, or delete details of a specific purchase order.
     - **GET**: Returns details of the purchase order with the specified ID.
     - **PUT**: Updates the details of the purchase order with the specified ID.
     - **DELETE**: Deletes the purchase order with the specified ID.

## Configuration

1. **Database Configuration**: Update the database settings in `settings.py` according to your database configuration.

2. **API Configuration**: Configure API endpoints in `urls.py` to match your desired URL patterns.

## Running the Application

1. **Run Development Server**: Start the Django development server:

   ```
   python manage.py runserver
   ```

2. **Access Admin Interface**: Access the Django admin interface by navigating to `http://127.0.0.1:8000/admin/` in your web browser. Use the superuser credentials created earlier to log in.

3. **API Endpoints**: Access the API endpoints for managing vendors and purchase orders:

   - Vendor API: `http://127.0.0.1:8000/api/vendors/`
   - Purchase Order API: `http://127.0.0.1:8000/api/purchase_orders/`

## Usage

1. **Vendor Management**:
   - Create, retrieve, update, and delete vendors using the provided API endpoints.
   - Retrieve vendor performance metrics by accessing the performance API endpoint.

2. **Purchase Order Management**:
   - Create, retrieve, update, and delete purchase orders using the provided API endpoints.
   - Acknowledge purchase orders to trigger recalculation of vendor performance metrics.

## Documentation

1. **API Documentation**: Detailed documentation for each API endpoint is provided within the project files. Refer to the respective views and serializers for API functionality.

2. **Code Documentation**: Inline comments and docstrings are provided throughout the project files to explain the functionality and usage of different components.

## Dependencies

The project relies on the following major dependencies:
- Django: Web framework for building web applications.
- Django REST Framework: Toolkit for building Web APIs in Django.
