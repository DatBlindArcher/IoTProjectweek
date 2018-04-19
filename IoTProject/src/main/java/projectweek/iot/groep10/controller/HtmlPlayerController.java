package projectweek.iot.groep10.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HtmlPlayerController {

    @GetMapping("/")
    public String index()
    {
        return "index";
    }

    @GetMapping("/test")
    public String test()
    {
        return "test";
    }
}