from base.target import Target
from images.imageAdaptee import ImageAdaptee


class ImageAdapter(Target, ImageAdaptee):
    def request(self) -> any:
        return ImageAdaptee().load_test_data()

    def train_data_request(self) -> any:
        return ImageAdaptee().load_train_data()
