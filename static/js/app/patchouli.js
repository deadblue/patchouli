/**
 * Created by deadblue on 15/07/07.
 */

$(function() {
    var redisModel = $('#redis_modal');
    var loadingStatus = $('#loading_status');
    function show_keys(server){
        redisModel.modal('show');
        loadingStatus.text('load keys...');
        // load keys
        $.get('/api/keys', {'server': server}, function(keys) {
            // use web worker to build tree data
            var worker = new Worker('static/js/app/worker.js');
            worker.addEventListener('message', function(evt) {
                // render treeview
                loadingStatus.text('render tree...');
                $('#redis_tree').treeview({
                    data: evt.data['nodes'],
                    levels: 1,
                    showBorder: false,
                    onNodeSelected: function(evt, node) {
                        if(node.hasOwnProperty('full_name')) {
                            var url = '/value?server=' + encodeURIComponent(_SERVER)
                                + '&key=' + encodeURIComponent(node['full_name']);
                            window.open(url, 'redis_value')
                        }
                    }
                });
                redisModel.modal('hide');
            });
            loadingStatus.text('load complete! build tree...');
            worker.postMessage(keys);
        });
    }

    // 加载keys，生成树
    show_keys(_SERVER);

});