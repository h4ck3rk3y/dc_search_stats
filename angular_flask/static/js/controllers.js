'use strict';

/* Controllers */

function IndexController($scope) {

}

function AboutController($scope) {

}

function ChartsController($scope, Charts, $timeout) {
    console.log("We are the world");
    var vm = $scope;



    Charts.get({}, function(char_data){
        vm.char_data=char_data;

        var values = char_data["arr"];

        vm.labels = ['Explicit', 'Indian Television', 'Sports', 'Bollywood'];
        vm.data = [0, 0, 0, 10];
    });


    function tick(){
        var searchQuery = Charts.get({}, function(char_data){
            console.log(char_data);

            var values = char_data["arr"];
            vm.dataSource = {
                "chart": {
                  "caption": "Categories for " + vm.char_data["total"] + "searches",
                  "captionFontSize": "30",
                  // more chart properties - explained later
                    },
                "data": [{
                    "label": "Explicit",
                    "value": values["0"]
                    },
                    {
                        "label": "Indian Television",
                        "value": values["1"]
                    },
                    {
                        "label": "Sports",
                        "value": values["2"]
                    },
                    {
                        "label": "Bollywood",
                        "value": values["3"]
                    },
                    {
                        "label": "English Television",
                        "value": values["4"]
                    },
                    {
                        "label": "Songs",
                        "value": values["5"]
                    },
                    {
                        "label": "English Movies",
                        "value": values["6"]
                    },
                    {
                        "label": "Academics",
                        "value": values["7"]
                    },
                    {
                        "label": "Games",
                        "value": values["8"]
                    },
                    {
                        "label": "Softwares",
                        "value": values["9"]
                    },
                    {
                        "label": "Others",
                        "value": values["10"]
                    }],
            };

            timer = $timeout(tick, 2000);
        });
    };

    var timer = $timeout(tick, 2000);


    $scope.$on("$destroy", function(event) {
        $timeout.cancel(timer);
    });

}


angular.module('AngularFlask').controller('ChartsController', ChartsController);

function SearchController($scope, Search, $timeout) {

    var vm = $scope;

	var searchQuery = Search.get({}, function(search){
		$scope.search=search;
	});


	function tick(){
		var searchQuery = Search.get({}, function(search){
			$scope.search=search;
			timer = $timeout(tick, 2000);
		});
	};

	var timer = $timeout(tick, 2000);


    vm.$on("$destroy", function(event) {
        $timeout.cancel(timer);

    });

}

function RandomSearchController($scope, RandomSearch, $timeout){

	var searchQuery = RandomSearch.get({}, function(search){
		$scope.search=search;
	});


	function tick(){
		var searchQuery = RandomSearch.get({}, function(search){
			$scope.search=search;
			timer = $timeout(tick, 1000);
		});
	};

	var timer = $timeout(tick, 1000);


    $scope.$on("$destroy", function() {
        if (timer) {
            $timeout.cancel(timer);
        }
    });

}


function UserController($scope, $routeParams, User)
{
	var userQueries = User.get({user: $routeParams.user}, function(queries)
	{
		$scope.queries = queries;
	})
}

function UserListController($scope, UserList){
	var userList = UserList.get({}, function(userList){
		$scope.user_list = userList;
	})
}
