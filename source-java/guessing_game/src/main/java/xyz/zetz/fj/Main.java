package xyz.zetz.fj;

import xyz.zetz.fj.guessing_game.GuessingGame;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");

        GuessingGame gaming = new GuessingGame();
        gaming.startGaming();
    }
}