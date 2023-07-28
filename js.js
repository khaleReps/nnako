$(document).ready(function() {
    var editColumnAdded = false;
    var deleteColumnAdded = false;
    var selectedCount = 0;
    var editBtnClickedOnce = false;
    var deleteBtnClickedOnce = false;
    var isEditing = false;
    var isDeleting = false;

    function updateSelectedCount() {
        // Count selected checkboxes
        selectedCount = $("tbody input[type='checkbox']:checked").length;
        console.log(selectedCount + " checkboxes selected.");
    }

    // Add event listener to checkboxes
    $("tbody").on("change", "input[type='checkbox']", function() {
        if (isEditing || isDeleting) {
            updateSelectedCount();
        }
    });

    // Click event handler for #editBtn
    $("#editBtn").click(function() {
        if (!editColumnAdded) {
            // Add a new column to the right
            $("thead tr").append("<th>Update</th>");
            $("tbody tr").each(function() {
                $(this).append("<td><input type='checkbox'></td>");
            });
            editColumnAdded = true;
            isEditing = true;
        } else {
            // Remove the column
            $("thead th:last-child").remove();
            $("tbody td:last-child").remove();
            editColumnAdded = false;

            if (editBtnClickedOnce) {
                updateSelectedCount();
                $("#selectedCountText").text(selectedCount + " checkboxes selected.");
                if (selectedCount > 0) {
                    $("#selectedCountModal").modal("show");
                }
            }

            editBtnClickedOnce = true;
            isEditing = false;
        }
    });

    // Click event handler for #deleteBtn
    $("#deleteBtn").click(function() {
        if (!deleteColumnAdded) {
            // Add a new column to the left
            $("thead tr").prepend("<th>Delete</th>");
            $("tbody tr").each(function() {
                $(this).prepend("<td><input type='checkbox'></td>");
            });
            deleteColumnAdded = true;
            isDeleting = true;
        } else {
            // Remove the column
            $("thead th:first-child").remove();
            $("tbody td:first-child").remove();
            deleteColumnAdded = false;

            if (deleteBtnClickedOnce) {
                updateSelectedCount();
                $("#selectedCountText").text(selectedCount + " checkboxes selected.");
                if (selectedCount > 0) {
                    $("#selectedCountModal").modal("show");
                }
            }

            deleteBtnClickedOnce = true;
            isDeleting = false;
        }
    });
});








{% block scripts %}  
    <script>

    // Go back to the previous page
    function goBack(){
        window.history.back()
    }    
    


    $(document).ready(function() {
        var selectedCount = 0;

        var editBtnClickedOnce = false;
        var editColumnAdded = false;
        var editSelectedCount = 0;
        var isEditing = false;
  
        var deleteBtnClickedOnce = false;
        var deleteColumnAdded = false;
        var deleteSelectedCount = 0;
        var isDeleting = false;

        
        
        function updateSelectedCount() {
            editSelectedCount = $("tbody td:nth-last-child(2) input[type='checkbox']:checked").length;
            deleteSelectedCount = $("tbody td:nth-last-child(1) input[type='checkbox']:checked").length;
                    
            if (editSelectedCount > 0) {
                $("#editSelectedCountText").text(editSelectedCount + " checkboxes selected for editing.");
                console.log(editSelectedCount + " Edit checkboxes selected.");
            } else {
                $("#editSelectedCountText").text("");
            }
        
            if (deleteSelectedCount > 0) {
                $("#deleteSelectedCountText").text(deleteSelectedCount + " checkboxes selected for deleting.");
                console.log(deleteSelectedCount + " Delete checkboxes selected.");
            } else {
                $("#deleteSelectedCountText").text("");
            }
        }


        
        function updateEditSelectedCount() {
            editSelectedCount = $("tbody td:nth-last-child(2) input[type='checkbox']:checked").length;
        
            // Update text for editing checkboxes
            if (editSelectedCount > 0) {
              $("#editSelectedCountText").text(editSelectedCount + " checkboxes selected for editing.");
              console.log(editSelectedCount + " Edit checkboxes selected.");
            } else {
              $("#editSelectedCountText").text("");
            }
        }

        function updateDeleteSelectedCount() {
            deleteSelectedCount = $("tbody td:nth-last-child(1) input[type='checkbox']:checked").length;
        
            // Update text for deleting checkboxes
            if (deleteSelectedCount > 0) {
              $("#deleteSelectedCountText").text(deleteSelectedCount + " checkboxes selected for deleting.");
              console.log(deleteSelectedCount + " Delete checkboxes selected.");
            } else {
              $("#deleteSelectedCountText").text("");
            }
        }
        
        // Add event listener to checkboxes
        $(document).on("change", "tbody input[type='checkbox']", function() {
            if (isEditing) {
                updateEditSelectedCount();
            }
        
            if (isDeleting) {
                updateDeleteSelectedCount();
            }
        });
        

        function handleCheckboxChange(checkbox) {
            if (checkbox.checked) {
                console.log("Checkbox selected.");
            } else {
                console.log("Checkbox deselected.");
            }
        }

        // Click event handler for #editBtn
        $("#editBtn").click(function() {
            if (!editColumnAdded) {
                console.log("Edit column opened.");
                
                // Add a new column to the right
                $("thead tr").append("<th>Update</th>");
                $("tbody tr").each(function() {
                    $(this).append("<td><input type='checkbox' onclick='handleCheckboxChange'></td>");
                    
                    function handleCheckboxChange(checkbox) {
                        if (checkbox.checked) {
                            console.log(editSelectedCount + " edit checkboxes selected.");
                        } else {
                            console.log(editSelectedCount + " edit checkboxes selected.");
                        }
                    }    
                });

                editColumnAdded = true;
                isEditing = true;
            } else {
                // Remove the column
                console.log("Edit column closed.");
                $("thead th:last-child").remove();
                $("tbody td:last-child").remove();
                editColumnAdded = false;
                
                if (editBtnClickedOnce) {
                    updateSelectedCount();
                    $("#modalTitle").text("Updates");
                    $("#selectedCountText").text(editSelectedCount + " members selected for update.");
                    if (editSelectedCount > 0) {
                        $("#selectedCountModal").modal("show");
                    }
                    
                }
                
                $("#selectedCountModal").modal("show");
                editBtnClickedOnce = true;
                isEditing = false;
            }
        });
    
        // Click event handler for #deleteBtn
        $("#deleteBtn").click(function() {
            if (!deleteColumnAdded) {
                // Add a new column to the left
                console.log("Delete column opened.");
                $("thead tr").prepend("<th>Delete</th>");
                $("tbody tr").each(function() {
                    $(this).prepend("<td><input type='checkbox' onclick='handleCheckboxChange(this)'></td>");

                    function handleCheckboxChange(checkbox) {
                        if (checkbox.checked) {
                            console.log(deleteSelectedCount + " delete checkboxes selected.");
                        } else {
                            console.log(deleteSelectedCount + " delete checkboxes selected.");
                        }
                    }


                    
                });
                deleteColumnAdded = true;
                isDeleting = true;
            } else {
                // Remove the column
                console.log("Delete column closed."); // Corrected log message
                $("thead th:first-child").remove();
                $("tbody td:first-child").remove();
                deleteColumnAdded = false;
        
                if (deleteBtnClickedOnce) {
                    updateSelectedCount();
                    $("#modalTitle").text("Deletion");
                    $("#selectedCountText").text(deleteSelectedCount + " members selected for deletion.");      
                }
                
        
                $("#selectedCountModal").modal("show");
                deleteBtnClickedOnce = true;
                isDeleting = false;
            }
        });
    
        // Update the selected count after modifying the table
        updateSelectedCount();


        // Handle form submission using AJAX
        $('#addMemberForm').submit(function (event) {
            event.preventDefault(); // Prevent regular form submission
            var form = $(this);
            var url = form.attr('action');
            var data = form.serialize();

            $.ajax({
                type: 'POST',
                url: url,
                data: data,
                success: function (response) {
                    if (response.success) {
                        $('#addMemberModal').modal('hide'); // Hide the modal on success
                        location.reload(); // Refresh the page to update the members list
                    }
                },
                error: function (xhr, status, error) {
                    // Handle errors if needed
                }
            });
        });
    });
    
    </script>
{% endblock %}  