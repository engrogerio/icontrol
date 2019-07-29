
contextMenu: function customMenu(node) {
  var control;
  var items = {
      createItem: {
          label: "Create",
          action: function (node) { return { createItem: this.create(node) }; }
      },
      renameItem: {
          label: "Rename",
          action: function (node) { return { renameItem: this.rename(node) }; }
      }
      // deleteItem: {
      //     label: "Delete",
      //     action: function (node) { return { deleteItem: this.remove(node) }; },
      //     "separator_after": true
      // },
      // copyItem: {
      //     label: "Copy",
      //     action: function (node) { $(node).addClass("copy"); return { copyItem: this.copy(node) }; }
      // },
      // cutItem: {
      //     label: "Cut",
      //     action: function (node) { $(node).addClass("cut"); return { cutItem: this.cut(node) }; }
      // },
      // pasteItem: {
      //     label: "Paste",
      //     action: function (node) { $(node).addClass("paste"); return { pasteItem: this.paste(node) }; }
      // }
  };
}


$(function(){
    $(".search-input").keyup(function() {
    var searchString = $(this).val();
    console.log(searchString);
    $('#jstree').jstree('search', searchString);
    });

  $("#tree").jstree({
    "plugins": ["search" ], //, "contextmenu"],
       core:{
         // so that create works
          "check_callback" : true,
          "data": jsonData
       },
       "search": {  
        "case_insensitive": true,
        "show_only_matches" : true
        },
        'themes': {
          'name': 'proton',
          'responsive': true
      },
        'context_menu':{
          'items': customMenu
        }
   })
   //this mades the tree clicable link works
   //https://stackoverflow.com/questions/8378561/
   .bind("select_node.jstree", function (e,data) { 
     $('#jstree').jstree('save_state');
   })
   .on("activate_node.jstree", function(e,data){
     document.location.href = data.node.a_attr.href; 
     });

    //this makes the dropdown stays opened while we click outside
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