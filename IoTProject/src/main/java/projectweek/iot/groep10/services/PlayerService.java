package projectweek.iot.groep10.services;

import org.springframework.stereotype.Service;
import projectweek.iot.groep10.db.PlayerMemoryDb;

@Service
public class PlayerService {
    public PlayerMemoryDb playerDb;

    public PlayerService() {
        playerDb = new PlayerMemoryDb();
    }
}
