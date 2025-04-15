import ijson
import os

def get_checkpoint(checkpoint_path: str)-> int:
    if os.path.exists(checkpoint_path):
        with open(checkpoint_path, 'r') as f:
            return #TODO
        
    else:
        return 0


def read_file(filepath: str, checkpoint_path: str, indexes:int = 10000):
    checkpoint = get_checkpoint(checkpoint_path)
    return