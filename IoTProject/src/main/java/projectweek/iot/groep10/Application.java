package projectweek.iot.groep10;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import projectweek.iot.groep10.services.PlayerService;

@SpringBootApplication(scanBasePackages = "projectweek.iot.groep10.controller")
public class Application {

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }

    @Bean
    public PlayerService service() {
        return new PlayerService();
    }
}