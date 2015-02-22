(function () {
  'use strict';

  angular
    .module('holdembonus.players', [
      'holdembonus.players.controllers',
      'holdembonus.players.services'
    ]);

  angular
    .module('holdembonus.players.controllers', []);

  angular
    .module('holdembonus.players.services', ['ngCookies']);
})();