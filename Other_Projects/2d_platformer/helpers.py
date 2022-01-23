import constants as c
import pygame


def coords_to_pygame(surface, position, size_y=0):
    return position[0], surface.get_height() - position[1] - size_y


def pygame_to_coords(surface, position):
    return position[0], position[1] * -1 + surface.get_height()


class Tile:
    def change_health(self, amount):
        self.health += amount

    def set_health(self, value):
        self.health = value

    def change_permeability(self, amount):
        self.permeability += amount

    def set_permeability(self, value):
        self.permeability = value

    def draw(self, surface, position, size=(160, 160)):
        if type(self) != Air:
            texture = pygame.transform.scale(self.texture, size)
            position = coords_to_pygame(surface, position, size[0])

            surface.blit(texture, position)


class Air(Tile):
    texture = None
    permeability = 1
    health = 8


class Glass(Tile):
    texture = c.GLASS
    permeability = 1
    health = 8


class Grass(Tile):
    texture = c.GRASS
    permeability = 0
    health = 8


class Dirt(Tile):
    texture = c.DIRT
    permeability = 0
    health = 8


class Stone(Tile):
    texture = c.STONE
    permeability = 0
    health = 8


class Deeplate(Tile):
    texture = c.DEEPSLATE
    permeability = 0
    health = 8


class Bedrock(Tile):
    texture = c.BEDROCK
    permeability = 0
    health = 8


class Column:
    def __init__(self, spans: [range]):
        self.spans = spans

    def tile(self, row):
        for span in self.spans:
            if span.__contains__(row):
                if row == 0:
                    return Bedrock()

                if row == span[-1]:
                    return Grass()

                if row in span[-2:-4:-1]:
                    return Dirt()

                if row in span[-24::-1]:
                    return Deeplate()

                return Stone()

        return Air()

    def tile_in_span(self, row):
        for span in self.spans:
            if span.__contains__(row):
                return span
        return None

    def remove_tile(self, span, row):
        r1 = range(span[0], row)
        if list(r1):
            self.spans.append(r1)

        r2 = range(row + 1, span[-1] + 1)
        if list(r2):
            self.spans.append(r2)

        self.spans.remove(span)
        return

    def add_tile(self, row):
        self.spans.append(range(row, row + 1))
        for span1 in self.spans:
            for span2 in self.spans:
                if span1[0] == span2[-1] + 1:
                    self.spans.append(range(span2[0], span1[-1] + 1))
                    self.spans.remove(span1)
                    self.spans.remove(span2)

                elif span2[0] == span1[-1] + 1:
                    self.spans.append(range(span1[0], span2[-1] + 1))
                    self.spans.remove(span1)
                    self.spans.remove(span2)
        return


class Level:
    def __init__(self, columns: [Column]):
        self.columns = columns

    def tile(self, col, row):
        return self.columns[col].tile(row)


def main():
    print(__file__.split("\\")[-1])


if __name__ == "__main__":
    main()
