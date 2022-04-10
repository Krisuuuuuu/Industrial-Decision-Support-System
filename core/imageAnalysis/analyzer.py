
class Analyzer:
    def __init__(self):
        self._test_data: any = None
        self._train_data: any = None

    def set_image_data(self, test_data: any, train_data: any):
        self._test_data = test_data
        self._train_data = train_data
