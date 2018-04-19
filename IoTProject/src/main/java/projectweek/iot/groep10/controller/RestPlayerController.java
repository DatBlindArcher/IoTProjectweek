package projectweek.iot.groep10.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import projectweek.iot.groep10.domain.Player;
import projectweek.iot.groep10.services.PlayerService;

import java.util.List;

@RestController
public class RestPlayerController
{
    private PlayerService service;

    @Autowired
    public RestPlayerController(PlayerService service) {
        this.service = service;
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
        return service.playerDb.createPlayer();
    }

    @PostMapping("/setplayer")
    public Player setPlayer(@RequestBody Player player)
    {
        return service.playerDb.setPlayer(player);
    }
}