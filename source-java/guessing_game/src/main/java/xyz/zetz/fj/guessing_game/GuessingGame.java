package xyz.zetz.fj.guessing_game;

import java.io.IOException;
import java.util.Random;
import java.util.Scanner;

public class GuessingGame {
    private final int mSecretNumber = new Random().nextInt(99) + 1;

    public GuessingGame() {
    }

    public void startGaming() {
        System.out.println("Guess the number!");

        Scanner scan = new Scanner(System.in);
        int guess = 0;
        while (true) {
            System.out.println("Please input your guess.");
            if (scan.hasNextInt()) {
                guess = scan.nextInt();
            }

            System.out.println("Your guessed: " + guess);

            if (guess == mSecretNumber) {
                System.out.println("You win!");
                break;
            } else if (guess < mSecretNumber) {
                System.out.println("Too small!");
            } else {
                System.out.println("Too big!");
            }
        }
        scan.close();
    }
}