function connect() {
    var socket = new SockJS('/players');
    stompClient = Stomp.over(socket);
    stompClient.connect({}, function (frame) {
        stompClient.subscribe('/topic/scores/' + Number($("#player").val()), function (player) {
            console.log(player.body);
            $("#name").val(player.name);
            $("#score").val(player.score);
        });
    });
}

$(function () {
    $("form").on('submit', function (e) {
        e.preventDefault();
    });

    $( "#receive" ).click(function() { connect(); });
});