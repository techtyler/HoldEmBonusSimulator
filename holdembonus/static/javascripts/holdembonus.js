(function() {
    
    angular
        .module('holdembonus', [
            'holdembonus.config',
            'holdembonus.routes',
            'holdembonus.players'
        ]);
    
    angular
        .module('holdembonus.routes', ['ngRoute']);
    
    angular
        .module('holdembonus.config, []');
    
})();
