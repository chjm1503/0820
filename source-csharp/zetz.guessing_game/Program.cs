using System;

namespace zetz
{
    class GuessingGame
    {
        private int secretNumber;

        public void InitGame()
        {
            secretNumber = new Random().Next(1, 101);
        }

        public void Run()
        {
            Console.WriteLine("Guess the number!");

            int guess;
            while (true)
            {
                Console.WriteLine("Please input your guess.");

                guess = Convert.ToInt32(Console.ReadLine());

                if (guess == secretNumber)
                {
                    Console.WriteLine("You win!");
                    break;
                }
                else if (guess < secretNumber)
                {
                    Console.WriteLine("Too small!");
                }
                else
                {
                    Console.WriteLine("Too big!");
                }
            }
        }

        public static void Main(String[] args)
        {
            Console.WriteLine("Hello, world!");

            var game = new GuessingGame();
            game.InitGame();
            game.Run();
        }
    };
}
