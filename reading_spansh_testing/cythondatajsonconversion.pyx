
import simplejson as json

def convert_chunk_to_jsonl(chunk_data, chunk_index: int, output_path_template: str):
    output_path = output_path_template.format(chunk_index)
    with gzip.open(output_path, 'at', encoding='utf-8') as fout:
        for obj in chunk_data:
            fout.write(json.dumps(obj, use_decimal=True) + '\n')