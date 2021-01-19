var $proceduresTree = $('#tree');

$(function () {
  $('#tree').jstree({
    "plugins": ["search"], //, "contextmenu"],

    "core": { 
      // so that create works
      //"check_callback" : true,
      "data": jsonData,
      "icons": true
    },
    "search": {  
      "case_insensitive": true,
      "show_only_matches" : true,
      'show_only_matches_children': true
    },
    'context_menu': {
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
  
  
  var to = false;
  $('.search-input').keyup(function () {
    if(to) { clearTimeout(to); }
    to = setTimeout(function () {
      var v = $('.search-input').val();
      $('#tree').jstree(true).search(v);
    }, 250);
  });
});
