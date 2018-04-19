package projectweek.iot.groep10.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.servlet.ModelAndView;
import projectweek.iot.groep10.services.PlayerService;

@Controller
public class HtmlPlayerController {

    private PlayerService service;

    @Autowired
    public HtmlPlayerController(PlayerService service) {
        this.service = service;
    }

    @GetMapping("/")
    public ModelAndView index()
    {
        return new ModelAndView("index", "players", service.playerDb.getLeaderBoard());
    }

    @GetMapping("/test")
    public String test()
    {
        return "test";
    }

    @GetMapping("/game")
    public String game()
    {
        return "game";
    }
}