'use strict';

angular.module('angularFlaskServices', ['ngResource'])
	.factory('Search', function($resource){
		return $resource('/api/search/random', {}, {
			query: {
				method: 'GET',
			}
		})
	})
;



