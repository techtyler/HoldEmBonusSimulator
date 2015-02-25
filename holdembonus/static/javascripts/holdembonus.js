(function() {
    
    angular
        .module('holdembonus', [
            'holdembonus.config',
            'holdembonus.routes',
            'auth'
        ]);
    
    angular
        .module('holdembonus.routes', ['ngRoute']);
    
    angular
        .module('holdembonus.config, []');
    
})();
