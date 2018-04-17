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
                return (int)(a.getScore() - b.getScore());
            }
        };
    }

    public Player createPlayer() {
        players.put(++counter, new Player(counter));
        return players.get(counter);
    }

    public void setPlayerName(int id, String name) {
        players.get(id).setName(name);
    }

    public void setPlayerScore(int id, int score) {
        players.get(id).setScore(score);
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