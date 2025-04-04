import ijson
import os

def save_index(index: int, pos_path: str):
    """Save the last processed index."""
    with open(pos_path, "w") as f:
        f.write(str(index))

def load_index( pos_path: str) -> int:
    """Load last processed index."""
    if os.path.exists(pos_path):
        with open(pos_path, "r") as f:
            return int(f.read().strip())
    return 0  # Start from the beginning if no index is saved

def process_json( json_path: str, pos_path: str):
    """Read JSON array lazily and resume from the last processed index."""
    last_index = load_index(pos_path)

    with open(json_path, "r", encoding="utf-8") as f:
        objects = ijson.items(f, "item")  # Stream objects

        for index, obj in enumerate(objects):
            if index < last_index:
                continue  # Skip already processed objects
            
            print(obj)  # Process object (store in DB, filter, etc.)

            if index % 1000 == 0:  # Save progress every 1000 objects
                save_index(index, pos_path)

    print("Processing complete.")
    os.remove(pos_path)  # Remove tracking file if fully processed