from pathlib import Path

import numpy as np
import pytest

from manim import Animation, Circle, Scene
from tests.helpers.graphical_units import set_test_scene


class CircleTestX(Scene):
    def construct(self):
        circle = Circle()
        self.play(Animation(circle))


data_p = Path(__file__).parent / "control_data" / "graphical_units_data" / "geometry"

file_test = data_p / "CircleTestX.npy"
file_control = data_p / "CircleTest.npy"
file_test.unlink(
    missing_ok=True
)  # file_test should not exist yet, however if it does, it will be removed for sure
set_test_scene(CircleTestX, "geometry")

comparison = np.load(file_test) == np.load(file_control)
equal_arrays = comparison.all()
print(equal_arrays)
if equal_arrays == False:
    raise ValueError("something went wrong with set_test_scene")
file_test.unlink(missing_ok=False)  # removes file_test
