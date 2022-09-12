class Scene:
    _active_scene = None

    def __init__(self, game_objects: list, width: int = 600, height: int = 600):
        self._new_objects = set()
        self._active_objects = set()
        self._deleted_objects = []
        self._width = width
        self._height = height

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    @classmethod
    def get_active_scene(cls):
        return cls._active_scene

    @classmethod
    def add_to_active_scene(cls, game_object):
        try:
            cls._active_scene.load_game_object(game_object)
        except AttributeError as e:
            print("\033[91mAttributeError: No active scene in.")

    def load_game_object(self, game_object):
        self._new_objects.add(game_object)

    def unload_game_object(self, game_object):
        self._active_objects.remove(game_object)

    def activate(self):
        Scene._active_scene = self

    @classmethod
    def get_game_objects(cls):
        return cls._active_scene.get_active_game_objects()

    def get_active_game_objects(self):
        return self._active_objects

    def update_scene(self):
        while True:
            try:
                self._active_objects.add(self._new_objects.pop())
            except KeyError:
                break

        while True:
            try:
                self._active_objects.remove(self._deleted_objects.pop())
            except IndexError:
                break


if __name__ == "__main__":
    print(__file__)
    sc = Scene([""])
    print(f"{sc.width=}")
    sc.add_to_active_scene("")
