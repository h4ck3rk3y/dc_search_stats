'use strict';

angular.module('angularFlaskServices', ['ngResource'])
	.factory('Search', function($resource){
		return $resource('/api/search', {}, {
			query: {
				method: 'GET',
			}
		})
	})
	.factory('RandomSearch', function($resource){
		return $resource('/api/search/random', {}, {
			query: {
				method: 'GET',
			}
		})
	})
	.factory('User', function($resource){
		return $resource('/api/search/:user', {}, {
			query: {
				method: 'GET',
				params: {'user': ''}
			}
		})
	})
	.factory('UserList', function($resource){
		return $resource('/api/users', {}, {
			query: {
				method: 'GET',
			}
		})
	})
	.factory('Query', function($resource){
		return $resource('/api/reverse/:query', {}, {
			query: {
				method: 'GET',
				params: {'query': ''}
			}
		})
	})
;



