
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
    var searchString = $(this).val().trim();
    console.log(searchString);
    $('#jstree').jstree('search', searchString);
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