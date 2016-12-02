'use strict';

/* Controllers */

function IndexController($scope) {
	
}

function AboutController($scope) {
	
}

function SearchController($scope, Search){
	var searchQuery = Search.get({}, function(search){
		$scope.search = search;
	});
}
