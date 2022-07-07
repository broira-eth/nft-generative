import csv
import json
import argparse

# --path 読み込むCSVファイルのパスを指定
# --ignore メタデータから除外するtrait。カンマ区切りで複数指定可
# --save 保存するテキストファイルのパス
parser = argparse.ArgumentParser(description='')
parser.add_argument('--path', required=True, help='Path of the Traits file to be read.') 
parser.add_argument('--save', default="./Output/Traits/result.csv",help= 'Path of the file to be saved') 
parser.add_argument('--ignore', default=[], nargs='+', required=False,type=str, help='Traits not to be left in metadata; multiple can be specified, separated by commas.') 

if __name__ == "__main__":

    count = 0
    csv_path = parser.parse_args().path
    ignore = parser.parse_args().ignore
    ignore_tuple = tuple(ignore)
    save_path = parser.parse_args().save

    with open(csv_path) as f:
        with open(save_path, "w", newline="") as g:
            writer = csv.writer(g,quoting=csv.QUOTE_NONE,escapechar=',')

            for line in csv.DictReader(f , delimiter = "\t"):

                keys = list(line.keys())
                values = list(line.values())

                attributes= list()
                for i,(key,value) in enumerate(zip(keys,values)):
                    if key in ignore_tuple:
                        continue
                    attributes.append({"trait_type":key,"value":value})
                    # print(json.dumps(attributes))
    
                text = json.dumps(attributes)+"\n"
                g.write(text)
