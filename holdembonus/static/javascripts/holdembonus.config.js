(function () {
  'use strict';

  angular
    .module('holdembonus.config', [])
    .config(config);

  config.$inject = ['$httpProvider', '$locationProvider'];

  /**
  * @name config
  * @desc Enable HTML5 routing
  */
  function config($httpProvider, $locationProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
    $locationProvider.html5Mode(true);
    $locationProvider.hashPrefix('!');
  }
})();