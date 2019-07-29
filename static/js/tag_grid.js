    $(function() {
     var data = [
         {"Name":"Rogério Vieira da SIlva",
        "Description":"JS Developer",
        "Rating":2,
        "Price":100000.00},
        {"Name":"Gustavo Vieira da SIlva",
        "Description":"JS Developer",
        "Rating":3,
        "Price":100.00},
        {"Name":"Rogério Vieira da SIlva",
        "Description":"JS Developer",
        "Rating":4,
        "Price":1000.00},
        {"Name":"Gustavo Vieira da SIlva",
        "Description":"JS Developer",
        "Rating":4,
        "Price":1000000.00},
        {"Name":"Rogério Vieira da SIlva",
        "Description":"JS Developer",
        "Rating":4,
        "Price":1000000.00},
        {"Name":"Gustavo Vieira da SIlva",
        "Description":"JS Developer",
        "Rating":4,
        "Price":1000000.00},
        {"Name":"Rogério Vieira da SIlva",
        "Description":"JS Developer",
        "Rating":4,
        "Price":1000000.00},
        {"Name":"Gustavo Vieira da SIlva",
        "Description":"JS Developer",
        "Rating":4,
        "Price":1000000.00}
     ];
        $("#jsGrid").jsGrid({
            height: "auto",
            width: "100%",
     
            sorting: true,
            paging: false,
            autoload: true,
     
            controller: {
                loadData: function() {
                    // var d = $.Deferred();
     
                    // $.ajax({
                    //     url: "http://services.odata.org/V3/(S(3mnweai3qldmghnzfshavfok))/OData/OData.svc/Products",
                    //     dataType: "json"
                    // }).done(function(response) {
                    //     d.resolve(response.value);
                    // });
     
                    return data;//d.promise();
                }
            },
     
            fields: [
                { name: "Name", type: "text" },
                { name: "Description", type: "textarea", width: 150 },
                { name: "Rating", type: "number", width: 50, align: "center",
                    itemTemplate: function(value) {
                        return $("<div>").addClass("rating").append(Array(value + 1).join("&#9733;"));
                    }
                },
                { name: "Price", type: "number", width: 50,
                    itemTemplate: function(value) {
                        return value.toFixed(2) + "$"; }
                }
            ]
        });
     
    });