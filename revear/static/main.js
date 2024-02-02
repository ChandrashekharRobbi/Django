

document.addEventListener('DOMContentLoaded' , function() {
    // change event listener for checkboxes
    var checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(function(checkbox) {
        checkbox.addEventListener('change', function() {
            // console.log(checkbox)
            var rowId = checkbox.id.replace('checked-', 'row-');
            // console.log(rowId)
            var row = document.getElementById(rowId);
            // console.log(row)
            if (checkbox.checked){
                row.parentNode.appendChild(row);
            }
            // console.log(row.classList)
            row.classList.toggle('strikethrough', checkbox.checked);
        });
    });
});