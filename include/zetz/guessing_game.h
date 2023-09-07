#ifndef ZETZ_GUESSING_GAME_H
#define ZETZ_GUESSING_GAME_H

#ifndef ZETZ_API_EXPORT
#define ZETZ_API __declspec(dllexport)
#else
#define ZETZ_API __declspec(dllimport)
#endif // ZETZ_API_EXPORT

#ifdef __cplusplus
extern "C"
{
#endif

    ZETZ_API void zetz_guessing_game_init();
    ZETZ_API void zetz_guessing_game_run();

#ifdef __cplusplus
}
#endif

#endif // ZETZ_GUESSING_GAME_H