import json
from typing import dataclass_transform
class ReadJson:
    def __init__(self) -> None:
        self.correct_choice = [
        {"correct words": {
        "1": "",
        "2": "",
        "3": "",
        "4": "",
        "5": "",
        "6": ""
            }}
]

    def readJson(self, idx) -> list:
        """ Reads json file and returns its key value """
        data = {}
        with open("results.json", "r" ) as f:
            data = json.load(f)
        for dct in data:
            for key, value in dct.items():
                for keys, val in value.items():
                    if keys == str(idx):
                        return [keys, val]

    def writeJson(self, dict_str: dict):
       """ Writes the values of arguments provided to json file """
       for dct in self.correct_choice:
            for key, value in dct.items():
                value.update(dict_str)
       dt = json.dumps(self.correct_choice, indent=4)
       print(dt)
       with open("results.json", "w") as f:
           f.write(dt)

    def resetJson(self):
        """ Resets all the values of all keys provided """
        data = {}

        for i, dct in enumerate(self.correct_choice):
            for key, value in dct.items():
                value.update({f"{i + 1}": ""})

        with open("results.json", "r") as f:
            data = json.load(f)
        for dic in data:
            for key, value in dic.items():
                for i in range(1, 7):
                    value.update({f"{i}": ""})
        dt = json.dumps(data, indent=4)
        with open("results.json", "w") as f:
            f.write(dt)


if __name__ == "__main__":
    ReadJson()
