import gzip
import ijson
import simplejson as json
import concurrent.futures


def convert_chunk_to_jsonl(chunk_data, chunk_index: int, output_path_template: str):
    output_path = output_path_template.format(chunk_index)
    with gzip.open(output_path, 'at', encoding='utf-8') as fout:
        for obj in chunk_data:
            fout.write(json.dumps(obj, use_decimal=True) + '\n')

def process_json_array_multithreaded(input_file: str, output_file_template: str, chunk_size:int = 100000, max_threads:int = 4):
    with gzip.open(input_file, 'rb') as fin:
        parser = ijson.items(fin, 'item')

        chunk_data = []
        chunk_index = 0

        with concurrent.futures.ThreadPoolExecutor(max_threads) as executor:
            futures = []
            for i, obj in enumerate(parser):
                chunk_data.append(obj)
                if len(chunk_data) >= chunk_size:
                    futures.append(executor.submit(convert_chunk_to_jsonl, chunk_data, chunk_index, output_file_template))

                    for future in concurrent.futures.as_completed(futures):
                        future.result()


input_file = 'E:\elite data\galaxy.json.gz'
output_file_template = 'E:\elite data\jsonl_galaxy_{:05d}.json.gz'
chunk_size = 100000
max_threads = 10

process_json_array_multithreaded(input_file, output_file_template, chunk_size, max_threads)
