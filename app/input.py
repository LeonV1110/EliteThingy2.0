from biological import Biological, jsonBiological
import json
class Input:

    def read_biologicals(filePath: str) -> list[Biological]:
        res = []
        with open(filePath, 'r') as file:
            
            for line in file:
                try:
                    biological = json.loads(line.strip())
                    res.append(jsonBiological(biological))
                except json.JSONDecodeError as e:
                    print(f'Error decoding JSON: {e}')
        return res