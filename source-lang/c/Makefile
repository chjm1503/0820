build/guessing_game/guessing_game: build/obj/guessing_game.o build/obj/guessing_game_main.o
	gcc build/obj/guessing_game.o build/obj/guessing_game_main.o -o build/guessing_game/guessing_game

build/obj/guessing_game.o: guessing_game/guessing_game.c
	gcc -I../include -c guessing_game/guessing_game.c -o build/obj/guessing_game.o

build/obj/guessing_game_main.o: guessing_game/guessing_game_main.c
	gcc -I../include -c guessing_game/guessing_game_main.c -o build/obj/guessing_game_main.o