from pathlib import Path
import json
from typing import Dict, List
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--json_dir",
        type=str,
        default="./model_cards/timm",
        help="The directory containing the json files",
    )
    parser.add_argument(
        "--jsonl_path",
        type=str,
        default='./test.jsonl',
        help="jsonl ooutput path",
    )
    return parser.parse_args()

def list2jsonl(json_list: List[Dict], output: str):
    with open(output, 'w') as file:
        for item in json_list:
            json.dump(item, file)
            file.write('\n')

def main():
    args = parse_arguments()
    json_dir = Path(args.json_dir)
    jsonl_path = Path(args.jsonl_path)

    json_list = []
    for json_path in json_dir.rglob("*.json"):
        json_content = json_path.read_text()
        try:
            json_dict = json.loads(json_content)
            json_dict["model_name"] = json_path.stem
            json_dict["json_path"] = str(json_path)
            json_list.append(json_dict)
        except Exception as e:
            print(json_path, e)

    list2jsonl(json_list, jsonl_path)
    
if __name__ == "__main__":
    main()


    

    

