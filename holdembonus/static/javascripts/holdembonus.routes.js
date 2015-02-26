(function () {
  'use strict';

  angular
    .module('holdembonus.routes', ['ngRoute'])
    //.config(config);

  config.$inject = ['$routeProvider'];

  

  /**
  * @name config
  * @desc Define valid application routes
  */
  function config($routeProvider) {
    $routeProvider.when('/register', {
      controller: 'rest-ang-auth.RegisterCtrl', 
      controllerAs: 'vm',
      templateUrl: 'auth/register.html'
    }).otherwise('/');
   }
})();