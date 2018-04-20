var stompClient = null;

function connect() {
    disconnect();
    var socket = new SockJS('/players');
    stompClient = Stomp.over(socket);
    stompClient.connect({}, function (frame) {
        stompClient.subscribe('/topic/scores/' + Number($("#player").val()), function (response) {
            var player = JSON.parse(response.body);
            console.log(player);
            $("#name").text(player.name);
            $("#score").text(player.score);
        });
    });
}

function disconnect() {
    if (stompClient !== null) {
        stompClient.disconnect();
        console.log("Disconnected");
    }
}


$(function () {
    $("form").on('submit', function (e) {
        e.preventDefault();
    });

    $( "#receive" ).click(function() { connect(); });
});