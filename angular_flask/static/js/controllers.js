'use strict';

/* Controllers */

function IndexController($scope) {
	
}

function AboutController($scope) {
	
}

function SearchController($scope, Search, $timeout){

	(function tick(){
		var searchQuery = Search.get({}, function(search){
			$scope.search=search;
			$timeout(tick, 5000);
		});
	})();
}

function UserController($scope, $routeParams, User)
{
	var userQueries = User.get({user: $routeParams.user}, function(queries)
	{
		$scope.queries = queries;
	})
}