import json
import pathlib
from json import JSONDecodeError


SRC_FILE = pathlib.Path.joinpath(pathlib.Path(__file__).parent.parent.parent, 'Resources/adiDuctileIronInfo.json')


class Adaptee:

    @staticmethod
    def _load_json_from_file():
        try:
            with open(SRC_FILE, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print('Invalid file name')
        except JSONDecodeError:
            print('Loaded file is not a valid JSON')
        except Exception as e:
            print(f'Something is wrong: {e}')

