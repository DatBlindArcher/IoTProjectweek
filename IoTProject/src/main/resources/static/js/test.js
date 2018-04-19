var stompClient = null;
var player = null;

function start() {
    jQuery.ajax({
        url: "/createplayer",
        type: "GET",

        contentType: 'application/json; charset=utf-8',
        success: function(resultData) {
            player = resultData;
            console.log(player);
            $("#name").val(player.name);
            $("#score").val(player.score);
        },
        error : function(jqXHR, textStatus, errorThrown) {
        },

        timeout: 120000,
    });

    connect();
}

function setConnected(connected) {
    $("#connect").prop("disabled", connected);
    $("#disconnect").prop("disabled", !connected);
}

function connect() {
    var socket = new SockJS('/players');
    stompClient = Stomp.over(socket);
    stompClient.connect({}, function (frame) {
        setConnected(true);
        console.log('Connected: ' + frame);
        stompClient.subscribe('/topic/scores/' + player.id, function (player) {
            console.log(player.body);
        });
    });
}

function disconnect() {
    if (stompClient !== null) {
        stompClient.disconnect();
    }
    setConnected(false);
    console.log("Disconnected");
}

function sendScore() {
    player.score = Number($("#score").val());
    stompClient.send("/app/scores/" + player.id, {}, JSON.stringify(player));
}

function saveScore() {
    player.score = Number($("#score").val());

    jQuery.ajax({
        url: "/setplayer",
        type: "POST",
        data: JSON.stringify(player),

        contentType: 'application/json; charset=utf-8',
        success: function(resultData) {
            player = resultData;
            console.log(player);
            $("#name").val(player.name);
            $("#score").val(player.score);
        },
        error : function(jqXHR, textStatus, errorThrown) {
            console.log(textStatus);
        },

        timeout: 120000,
    });}

$(function () {
    $("form").on('submit', function (e) {
        e.preventDefault();
    });
    $( "#connect" ).click(function() { connect(); });
    $( "#disconnect" ).click(function() { disconnect(); });
    $( "#send" ).click(function() { sendScore(); });
    $( "#save" ).click(function() { saveScore(); });
});