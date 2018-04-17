package projectweek.iot.groep10.domain;

public class Player {
    private int id;
    private String name;
    private double score;

    public Player(int id) {
        this.id = id;
        this.name = "Player " + id;
        this.score = 0;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getScore() {
        return score;
    }

    public void setScore(double score) {
        this.score = score;
    }
}