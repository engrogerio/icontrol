$(function(){
    $(".search-input").keyup(function() {
    console.log('teste')
    var searchString = $(this).val();
    console.log(searchString);
    $('#jstree').jstree('search', searchString);
    });
    //alert(jsonData);
    //var serialized_tags = [{"text": "MENU", "a_attr": {"href": "/tag/update/dd10a033-c380-438a-b150-242d4a0bb009"}, "id": "dd10a033-c380-438a-b150-242d4a0bb009", "parent": "#"}, {"text": "Process Number", "a_attr": {"href": "/tag/update/b6809f01-4a0d-4e3c-b470-2511f6c4166c"}, "id": "b6809f01-4a0d-4e3c-b470-2511f6c4166c", "parent": "dd10a033-c380-438a-b150-242d4a0bb009"}, {"text": "TESTE", "a_attr": {"href": "/tag/update/90d51658-4608-4166-a6b0-a630f54e5cc7"}, "id": "90d51658-4608-4166-a6b0-a630f54e5cc7", "parent": "b6809f01-4a0d-4e3c-b470-2511f6c4166c"}, {"text": "Sessão de dados", "a_attr": {"href": "/tag/update/a384feac-d46d-4f89-9da3-c9002a48c8b6"}, "id": "a384feac-d46d-4f89-9da3-c9002a48c8b6", "parent": "90d51658-4608-4166-a6b0-a630f54e5cc7"}, {"text": "Process Letter", "a_attr": {"href": "/tag/update/ccfbdeac-2cff-41ba-8918-ff296d3e322f"}, "id": "ccfbdeac-2cff-41ba-8918-ff296d3e322f", "parent": "a384feac-d46d-4f89-9da3-c9002a48c8b6"}, {"text": "Name", "a_attr": {"href": "/tag/update/792138c8-0168-4207-b110-6e9e0a5011c2"}, "id": "792138c8-0168-4207-b110-6e9e0a5011c2", "parent": "a384feac-d46d-4f89-9da3-c9002a48c8b6"}, {"text": "Process", "a_attr": {"href": "/tag/update/0c01f499-3df9-4b0d-b600-dc25641109ef"}, "id": "0c01f499-3df9-4b0d-b600-dc25641109ef", "parent": "792138c8-0168-4207-b110-6e9e0a5011c2"}, {"text": "Process Code", "a_attr": {"href": "/tag/update/88476d25-8458-43ee-97bc-c71801ab4674"}, "id": "88476d25-8458-43ee-97bc-c71801ab4674", "parent": "792138c8-0168-4207-b110-6e9e0a5011c2"}, {"text": "Requirements", "a_attr": {"href": "/tag/update/8e257d68-4de0-48be-9500-e0304329fe95"}, "id": "8e257d68-4de0-48be-9500-e0304329fe95", "parent": "792138c8-0168-4207-b110-6e9e0a5011c2"}, {"text": "Function", "a_attr": {"href": "/tag/update/c9a7d0fc-4b05-4215-9531-e335d8db8319"}, "id": "c9a7d0fc-4b05-4215-9531-e335d8db8319", "parent": "792138c8-0168-4207-b110-6e9e0a5011c2"}, {"text": "Code", "a_attr": {"href": "/tag/update/c6b84282-d2b0-44e2-b765-82b4f503d26b"}, "id": "c6b84282-d2b0-44e2-b765-82b4f503d26b", "parent": "b6809f01-4a0d-4e3c-b470-2511f6c4166c"}, {"text": "TESTE2", "a_attr": {"href": "/tag/update/2f7fbe02-3ad3-4723-95b0-74575d72897e"}, "id": "2f7fbe02-3ad3-4723-95b0-74575d72897e", "parent": "b6809f01-4a0d-4e3c-b470-2511f6c4166c"}, {"text": "Company", "a_attr": {"href": "/tag/update/78562a16-f168-479c-86e2-a36545957f90"}, "id": "78562a16-f168-479c-86e2-a36545957f90", "parent": "dd10a033-c380-438a-b150-242d4a0bb009"}];


  $("#tree").jstree({
    "plugins": ["search"],
       core:{
           "data": jsonData
       },
       "search": {  
        "case_insensitive": true,
        "show_only_matches" : true
        },
   })
   //this mades the tree clicable link works
   //https://stackoverflow.com/questions/8378561/
   .bind("select_node.jstree", function (e,data) { 
     $('#jstree').jstree('save_state');
   })
   .on("activate_node.jstree", function(e,data){
     document.location.href = data.node.a_attr.href; 
     });

    //this makes the dropdown stays opened until while we click outside
    //https://stackoverflow.com/questions/19740121/
   
   $('#keepdown').on({
    "shown.bs.dropdown": function() { this.closable = true; },
    "click":             function(e) { 
        var target = $(e.target);
        if(target.hasClass("dropdown-toggle")) 
          this.closable = true;
        else 
          this.closable = false; 
          
    },
    "hide.bs.dropdown":  function() { return this.closable; }
});
});