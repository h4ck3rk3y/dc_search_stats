'use strict';

angular.module('AngularFlask', ['angularFlaskServices'])
	.config(['$routeProvider', '$locationProvider',
		function($routeProvider, $locationProvider) {
		$routeProvider
		.when('/', {
			templateUrl: 'static/partials/search.html',
			controller: SearchController
		})
		.when('/search', {
			templateUrl: 'static/partials/search.html',
			controller: SearchController
		})
		/* Create a "/blog" route that takes the user to the same place as "/post" */
		.when('/blog', {
			templateUrl: 'static/partials/search.html',
			controller: SearchController
		})
		.when('/userslist',{
			templateUrl: 'static/partials/user-list.html',
			controller: UserListController
		})
		.when('/user/:user',{
			templateUrl: '/static/partials/search-list.html',
			controller: UserController
		})
		.when('/random',{
			templateUrl: '/static/partials/search.html',
			controller: RandomSearchController
		})
		.otherwise({
			redirectTo: '/'
		})
		;

		$locationProvider.html5Mode(true);
	}])
	.filter('clean_date', function() {
	return function(input) {
		return input.replace('GMT', '');
	}
});