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

function UserController($scope, $routeParams, User)
{
	var userQueries = User.get({user: $routeParams.user}, function(queries)
	{
		$scope.queries = queries;
	})
}