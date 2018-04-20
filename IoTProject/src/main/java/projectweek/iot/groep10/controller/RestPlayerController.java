package projectweek.iot.groep10.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.messaging.simp.SimpMessageSendingOperations;
import org.springframework.web.bind.annotation.*;
import projectweek.iot.groep10.domain.Player;
import projectweek.iot.groep10.services.PlayerService;

import java.util.List;

@RestController
public class RestPlayerController
{
    private PlayerService service;
    private SimpMessageSendingOperations messagingTemplate;

    @Autowired
    public RestPlayerController(PlayerService service, SimpMessageSendingOperations messagingTemplate) {
        this.service = service;
        this.messagingTemplate = messagingTemplate;
    }

    @GetMapping("/leaderboard")
    public Player[] getLeaderboard()
    {
        List<Player> players = service.playerDb.getLeaderBoard();
        Player[] result = new Player[players.size()];
        players.toArray(result);
        return result;
    }

    @GetMapping("/createplayer")
    public Player createPlayer()
    {
        Player result = service.playerDb.createPlayer();
        messagingTemplate.convertAndSend("/topic/scores/" + result.getId(), result);
        return result;
    }

    @PostMapping("/setplayer")
    public Player setPlayer(@RequestBody Player player)
    {
        Player result = service.playerDb.setPlayer(player);
        messagingTemplate.convertAndSend("/topic/scores/" + result.getId(), result);
        return result;
    }
}