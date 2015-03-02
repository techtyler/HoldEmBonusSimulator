(function () {
  'use strict';

  angular
    .module('holdembonus.routes', ['ngRoute'])
    .config(config);

  config.$inject = ['$routeProvider'];

  

  /**
  * @name config
  * @desc Define valid application routes
  */
  function config($routeProvider) {
    $routeProvider.when('/home', {
      templateUrl: 'home.html'
    })
    
    .when('/', {
      redirectTo: '/home'
    })

    .otherwise('/');
   }
})();