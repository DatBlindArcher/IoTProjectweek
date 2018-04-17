package projectweek.iot.groep10.controller;

import org.springframework.web.bind.annotation.GetMapping;

@org.springframework.web.bind.annotation.RestController
public class RestController
{
    public static int index = 0;

    @GetMapping("/getplayer")
    public String getPlayer()
    {
        index++;
        return "player " + index;
    }
}