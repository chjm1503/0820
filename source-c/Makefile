OUTPUT_PATH  := ./build

guessing_game: guessing_game.o guessing_game_main.o
	gcc -o builc/cache/guessing_game.o builc/cache/guessing_game_main.o

guessing_game.o : guessing_game/guessing_game.c
	gcc -c guessing_game/guessing_game.c -I../include 

guessing_game_main.o: guessing_game/main.c
	gcc -c guessing_game/main.c -I../include


clean:
	rm -rf build/*make
