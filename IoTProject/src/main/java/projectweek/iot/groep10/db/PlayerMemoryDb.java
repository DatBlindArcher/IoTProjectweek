package projectweek.iot.groep10.db;

import projectweek.iot.groep10.domain.Player;

import java.util.*;

public class PlayerMemoryDb {
    private int counter;
    private Map<Integer, Player> players;
    private Comparator<Player> comparator;

    public PlayerMemoryDb() {
        counter = 0;
        players = new HashMap<Integer, Player>();
        comparator = new Comparator<Player>() {
            @Override
            public int compare(Player a, Player b) {
                return (int)(b.getScore() - a.getScore());
            }
        };

        createPlayer();
        createPlayer();
    }

    public Player createPlayer() {
        players.put(++counter, new Player(counter));
        return players.get(counter);
    }

    public Player setPlayer(Player player) {
        players.get(player.getId()).setName(player.getName());
        players.get(player.getId()).setScore(player.getScore());
        return players.get(player.getId());
    }

    public List<Player> getLeaderBoard() {
        List<Player> list = new ArrayList<Player>(players.values());
        Collections.sort(list, comparator);
        return list;
    }

    public Collection<Player> getPlayers() {
        return players.values();
    }
}