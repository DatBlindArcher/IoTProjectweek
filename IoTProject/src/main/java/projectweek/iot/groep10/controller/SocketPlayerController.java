package projectweek.iot.groep10.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.messaging.handler.annotation.DestinationVariable;
import org.springframework.messaging.handler.annotation.MessageMapping;
import org.springframework.messaging.handler.annotation.SendTo;
import org.springframework.stereotype.Controller;
import projectweek.iot.groep10.domain.Player;
import projectweek.iot.groep10.services.PlayerService;

@Controller
public class SocketPlayerController {

    private PlayerService service;

    @Autowired
    public SocketPlayerController(PlayerService service) {
        this.service = service;
    }

    @MessageMapping("/scores/{playerid}")
    @SendTo("/topic/scores/{playerid}")
    public Player setplayer(@DestinationVariable String playerid, Player player) {
        return player;
    }
}
