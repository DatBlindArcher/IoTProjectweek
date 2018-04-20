package projectweek.iot.groep10.controller;

import org.springframework.messaging.handler.annotation.DestinationVariable;
import org.springframework.messaging.simp.annotation.SubscribeMapping;
import org.springframework.stereotype.Controller;
import projectweek.iot.groep10.domain.Player;

@Controller
public class SocketPlayerController {

    @SubscribeMapping("/topic/scores/{playerid}")
    public Player setplayer(@DestinationVariable String playerid, Player player) {
        return player;
    }
}
