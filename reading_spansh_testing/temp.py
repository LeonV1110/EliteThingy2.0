import gzip
import ijson
import simplejson as json
from decimal import Decimal
import concurrent.futures
import os
import logging
import time
import uuid
from datetime import datetime

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

def convert_chunk_to_jsonl(chunk_data, chunk_index: int, output_path_template: str):
    output_path = output_path_template.format(chunk_index)
    try:
        with gzip.open(output_path, 'at', encoding='utf-8') as fout:
            for obj in chunk_data:
                fout.write(json.dumps(obj, use_decimal=True) + '\n')
        logging.info(f"[Chunk {chunk_index}] ✅ Written {len(chunk_data)} records to {output_path}")
    except Exception as e:
        logging.error(f"[Chunk {chunk_index}] ❌ Error writing file: {e}")

def process_json_array_multithreaded(input_file: str, output_base_folder: str, chunk_size: int = 250_000, max_threads: int = 24):
    if not os.path.exists(input_file):
        logging.error(f"❌ Input file does not exist: {input_file}")
        return

    # Create unique output folder
    run_id = str(uuid.uuid4())
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    folder_name = f"{run_id}-{timestamp}-GalaxyChunks"
    output_folder = os.path.join(output_base_folder, folder_name)
    os.makedirs(output_folder, exist_ok=True)
    output_file_template = os.path.join(output_folder, "jsonl_galaxy_{:05d}.json.gz")

    logging.info(f"📁 Output folder: {output_folder}")

    start_time = time.time()

    try:
        with gzip.open(input_file, 'rb') as fin:
            parser = ijson.items(fin, 'item')

            chunk_data = []
            chunk_index = 0

            with concurrent.futures.ThreadPoolExecutor(max_threads) as executor:
                futures = []

                for i, obj in enumerate(parser):
                    try:
                        chunk_data.append(obj)
                    except Exception as e:
                        logging.warning(f"⚠️ Failed to parse object at index {i}: {e}")
                        continue

                    if len(chunk_data) >= chunk_size:
                        futures.append(executor.submit(convert_chunk_to_jsonl, chunk_data.copy(), chunk_index, output_file_template))
                        logging.info(f"🚀 Dispatched chunk {chunk_index} with {len(chunk_data)} records")
                        chunk_data.clear()
                        chunk_index += 1

                # Final chunk
                if chunk_data:
                    futures.append(executor.submit(convert_chunk_to_jsonl, chunk_data.copy(), chunk_index, output_file_template))
                    logging.info(f"🚀 Dispatched final chunk {chunk_index} with {len(chunk_data)} records")

                # Wait for all threads
                for future in concurrent.futures.as_completed(futures):
                    try:
                        future.result()
                    except Exception as e:
                        logging.error(f"❌ Thread error: {e}")

        total_time = time.time() - start_time
        logging.info(f"✅ Finished processing in {total_time:.2f} seconds")

    except Exception as e:
        logging.error(f"❌ Failed to process input file: {e}")

# === Run Config (Optimized for 28-core / 80GB VM) ===
input_file = 'E:\elite data\galaxy.json.gz'
output_base_folder = 'E:\elite data'
chunk_size = 250_000
max_threads = 24

process_json_array_multithreaded(input_file, output_base_folder, chunk_size, max_threads)