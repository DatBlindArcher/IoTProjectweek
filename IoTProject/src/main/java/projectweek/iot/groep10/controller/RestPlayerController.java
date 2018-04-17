package projectweek.iot.groep10.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import projectweek.iot.groep10.domain.Player;
import projectweek.iot.groep10.services.PlayerService;

@RestController
public class RestPlayerController
{
    @Autowired
    private PlayerService service;

    @GetMapping("/getplayer")
    public Player getPlayer()
    {
        Player player = service.playerDb.createPlayer();
        return player;
    }
}