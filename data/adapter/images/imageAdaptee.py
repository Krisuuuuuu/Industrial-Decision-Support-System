import pathlib
from abc import ABC

import tensorflow_datasets as tfds

SRC_FILE = pathlib.Path.joinpath(pathlib.Path(__file__).parent.parent.parent, 'resources/test')


class ImageAdaptee(ABC):

    @staticmethod
    def load_test_data() -> any:
        return tfds.load(name="rock_paper_scissors", split="test")

    @staticmethod
    def load_train_data() -> any:
        return tfds.load(name="rock_paper_scissors", split="train")
