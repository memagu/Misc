from .scene import Scene


class GameLoop:
    def __init__(self, limit_fps=60):
        self.limit_fps = limit_fps

    def init(self, canvas=None, window=None):
        self._start_game_loop()

    def _start_game_loop(self):
        # Update scene
        Scene.get_active_scene().update_scene()

        # Access and call all game_objects in scene
        game_objects = Scene.get_active_scene().get_game_objects()
        for game_object in game_objects:
            game_object.start()

        while True:
            game_objects = Scene.get_active_scene().get_game_objects()
            for game_object in game_objects:
                if not game_object.started:
                    game_object.start()

                if game_object.destroyed:
                    Scene.get_active_scene().remove_game_object(game_object)

                # handle input
                game_object.input()

                # handle update
                game_object.update()

                # handle fixed_update
                game_object.fixed_update()

                # handle render
                game_object.render()

