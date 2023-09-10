package main

import (
	"fmt"
	"math/rand"
)

type guessingGame struct {
	secretNumber int
}

func newGuessingGame() guessingGame {
	return guessingGame{secretNumber: rand.Int() % 100}
}

func (i guessingGame) run() {
	fmt.Println("Guess the number!")

	var guess int
	for {
		fmt.Println("Please input your guess.")

		fmt.Scanln(&guess)

		if guess == i.secretNumber {
			fmt.Println("You win!")
			break
		} else if guess < i.secretNumber {
			fmt.Println("Too small!")
		} else {
			fmt.Println("Too big!")
		}
	}
}

func main() {
	fmt.Println("Hello, world!")
	game := newGuessingGame()
	game.run()
}
