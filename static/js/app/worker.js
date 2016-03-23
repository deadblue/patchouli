/**
 * build tree worker
 */

onmessage = function(evt){
    var tree = {'text': 'ROOT', 'nodes': []};
    var keys = evt.data;
    keys.forEach(function(key) {
        var parent = tree;
        var parts = key.split(':');
        parts.forEach(function(part, index){
            var brothers = parent['nodes'];
            if(typeof(brothers) == 'undefined') {
                parent['nodes'] = brothers = [];
            }
            var filtered = brothers.filter(function(node){ return node['text']==part; });
            if(filtered.length <= 0) {
                if(index == parts.length - 1) {
                    parent = {'text': part, 'full_name': key};
                } else {
                    parent = {'text': part, 'nodes': [], 'selectable': false};
                }
                brothers.push(parent);
            } else {
                parent = filtered[0];
            }
        });
    });
    postMessage(tree);
};