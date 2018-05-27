
 var json = {
        "Array": [1, 2, 3], "Boolean": true, "Null": null, "Number": 123,
        "Object": {"a": "b", "c": "d"}, "String": "Hello World",
        "auto": "$Hello World"
		};
		
		$(document).ready(function () {
			$('label.tree-toggler').click(function () {
				$(this).parent().children('ul.tree').toggle(200);
			});
			$('label.tree-toggler').parent().children('ul.tree').toggle(0);
		});
 
        // $('#myDropdown').on("click",'.dropdown-menu',function(e){
        //     alert("Im here !!!")
        //       e.stopPropagation();
        //     });

        var jsonData = [
  {"id":"27","parent":"#","text":"Incidência Obrigatória"},
  {"id":"28","parent":"#","text":"Executar trabalho em regime de turnos ininterruptos de revezamento"},
  {"id":"30","parent":"#","text":"Executar trabalho em jornada de sobreaviso"},
  {"id":"33","parent":"28","text":"Trabalhar em ferrovias"},
  {"id":"35","parent":"27","text":"Utilizar sistemas alternativos eletrônicos de marcação do ponto"}
];

$("#tree").jstree({
    core:{
        "data": jsonData
    }
});
