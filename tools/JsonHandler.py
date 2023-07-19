import json

class JsonHanlder():        

    @staticmethod
    def openJson (file_path):
        with open(file_path, 'r') as f:
            json_data = json.load(f)

            return json_data

    @staticmethod
    def writeJson(json_data, file_path):

        with open(file_path, 'w') as f:
            json.dump(json_data, f)

