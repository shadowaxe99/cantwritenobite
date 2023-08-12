import pygame
import numpy as np


class Writer:
    def __init__(self, stroke_path):
        self.stroke_path = stroke_path
        self.index = 0

    def draw(self, surface):
        if self.index < len(self.stroke_path) - 1:
            pygame.draw.circle(surface, (0, 0, 0), self.stroke_path[self.index], 5)
            self.index += 1


def get_stroke_path(data, factor, offset_x, offset_y):
    stroke_path = []
    for stroke in data['strokes']:
        for x, y in zip(stroke[0], stroke[1]):
            stroke_path.append((int(x * factor + offset_x), int(y * factor + offset_y)))
    return stroke_path