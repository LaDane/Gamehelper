import json
import os


class FileHandler:
    def load_file(self, filename):
        filedestiation = f"json/{filename}.json"
        if os.path.exists(filedestiation):
            with open(filedestiation, 'r') as file:
                result = json.load(file)
            return result
        return None

    def save_file(self, data, filename):
        with open(f"json/{filename}.json", 'w') as file:
                json.dump(data, file, indent=4)