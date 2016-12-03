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
			timer = $timeout(tick, 2000);
		});
	};

	var timer = $timeout(tick, 2000);


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


function ReverseQueryController($scope, Query)
{
	$scope.$watch("query", function(){
		if($scope.query!=undefined && $scope.query.length >= 2){
			var reverseQueries = Query.get({query: $scope.query}, function(matches){
				$scope.matches = matches;
			});
		}

		if($scope.query == '')
		{
			$scope.matches = undefined;
		}
	}, true);
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