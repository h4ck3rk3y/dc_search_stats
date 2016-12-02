'use strict';

/* Controllers */

function IndexController($scope) {
	
}

function AboutController($scope) {
	
}

function SearchController($scope, Search, $timeout){

	var searchQuery = Search.get({}, function(search){
		$scope.search=search;
	});


	function tick(){
		var searchQuery = Search.get({}, function(search){
			$scope.search=search;
			timer = $timeout(tick, 500);
		});
	};

	var timer = $timeout(tick, 500);


    $scope.$on("$destroy", function() {
        if (timer) {
            $timeout.cancel(timer);
        }
    });

}

function RandomSearchController($scope, RandomSearch, $timeout){

	var searchQuery = RandomSearch.get({}, function(search){
		$scope.search=search;
	});


	function tick(){
		var searchQuery = RandomSearch.get({}, function(search){
			$scope.search=search;
			timer = $timeout(tick, 500);
		});
	};

	var timer = $timeout(tick, 500);


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