/**
 * Created by deadblue on 15/07/08.
 */

(function(context){
    context.logger = {
        debug: function(msg) {
            var d = new Date();
            d = d.getFullYear() + '-' +
                (d.getMonth() + 1) + '-' +
                d.getDate() + ' ' +
                d.getHours() + ':' +
                d.getMinutes() + ':' +
                d.getSeconds();
            console.log('[' + d + '] ' + msg);
        }
    };
})(window);