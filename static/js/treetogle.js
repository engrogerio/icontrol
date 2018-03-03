
 var json = {
        "Array": [1, 2, 3], "Boolean": true, "Null": null, "Number": 123,
        "Object": {"a": "b", "c": "d"}, "String": "Hello World",
        "auto": "$Hello World"
		};

    angular.module('ngApp', ['angular-jsoneditor']).controller('ngCtrl', function ($scope) {
        $scope.obj = {data: json, options: {mode: 'tree'}};
        $scope.onLoad = function (instance) {
            instance.expandAll();
            this.options.mode = 'tree';
            this.options.completer = [
                {value: "$sameer", score: 1000, meta: "custom"},
                {value: "$rathore", score: 1000, meta: "custom"}
            ];
        };
        $scope.changeData = function () {
            $scope.obj.data = {foo: 'bar'};
        };
        $scope.changeOptions = function () {
            $scope.obj.options.mode = $scope.obj.options.mode == 'tree' ? 'code' : 'tree';
        };
        $scope.pretty = function (obj) {
            return obj;
        };
		});
		
		$(document).ready(function () {
			$('label.tree-toggler').click(function () {
				$(this).parent().children('ul.tree').toggle(200);
			});
			$('label.tree-toggler').parent().children('ul.tree').toggle(0);
		});
 
        $('#myDropdown').on("click",'.dropdown-menu',function(e){
            alert("Im here !!!")
              e.stopPropagation();
            });
        