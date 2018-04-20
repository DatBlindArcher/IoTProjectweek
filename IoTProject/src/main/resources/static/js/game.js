var stompClient = null;
var stickman = null
var ctx = null;
var peescore = 0;

window.onload = function() {
    var c = document.getElementById("game");
    ctx = c.getContext("2d");

    stickman = new Image();
    stickman.onload = function() {
        drawCanvas();
    };
    stickman.src = '/img/stickman_pee.png';
};

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
            peescore = player.score;
            drawCanvas();
        });
    });
}

function drawCanvas() {
    if (ctx != null && stickman != null && stickman.complete) {
        ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
        ctx.drawImage(stickman, 10, 10);

        var start = {x:85, y:150};
        var point1 = {x:100, y:150};
        var point2 = {x:100 + peescore * 2, y:150};
        var end = {x:200 + peescore * 2, y:300};

        ctx.beginPath();
        ctx.moveTo(start.x, start.y);
        ctx.bezierCurveTo(point1.x, point1.y, point2.x, point2.y, end.x, end.y);
        ctx.lineWidth = 5;

        // line color
        ctx.strokeStyle = 'yellow';
        ctx.stroke();
    }
}

function disconnect() {
    if (stompClient !== null) {
        stompClient.disconnect();
        console.log("Disconnected");
    }
}

/*function onScoreChange(score) {
    console.log(score);
    peescore = score;
    drawCanvas();
}*/

$(function () {
    $("form").on('submit', function (e) {
        e.preventDefault();
    });

    $("#receive").click(function() { connect(); });

    /*var slider = document.getElementById('peescore');
    slider.onchange = function () { onScoreChange(this.value) };*/
});