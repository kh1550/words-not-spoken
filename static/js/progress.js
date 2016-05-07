document.addEventListener('DOMContentLoaded',init);

function init() {
    var button = document.getElementById('progress');
    button.addEventListener('click', progress);
}

function progress(event) {
    console.log("Progress clicked!");
    document.getElementById('friends').style.display = "block";

    if (document.getElementById('list').childNodes.length < 2) {
        var req = new XMLHttpRequest();
        req.open('POST', '/progress', true);
        req.send();
        req.addEventListener('load', function() {
            console.log("Content received!");
            var parsed = JSON.parse(req.responseText);
            if (parsed.list) {
                var list = document.getElementById('list');
                for (var i = 0; i < parsed.list.length; i++) {
                    var li = document.createElement("LI");
                    var item = document.createTextNode(parsed.list[i]);
                    li.appendChild(item);
                    list.appendChild(li);
                }
            }
        });
    }

    document.getElementById('exit').addEventListener('click', function() {
        document.getElementById('friends').style.display = "none";
    });
}