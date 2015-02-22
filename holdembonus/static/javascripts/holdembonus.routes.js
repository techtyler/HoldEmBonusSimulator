(function () {
  'use strict';

  angular
    .module('holdembonus.routes')
    .config(config);

  config.$inject = ['$routeProvider'];

  

  /**
  * @name config
  * @desc Define valid application routes
  */
  function config($routeProvider) {
    $routeProvider.when('/register', {
      controller: 'RegisterController', 
      controllerAs: 'vm',
      templateUrl: '/static/templates/players/register.html'
    }).otherwise('/');
  }
})();