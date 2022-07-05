import sys
import yaml
from PIL import Image
import csv
import time
import argparse

## --config configファイルのパス

parser = argparse.ArgumentParser()
parser.add_argument('--config', default='./Config/config.yaml')
args = parser.parse_args()

def main(argv):

    try:
        # Config読み込み
        with open(args.config,'r') as file:
            obj = yaml.safe_load(file)
            # print((obj)['parts'])
            
    except Exception as e:
        print('Exception occurred while loading YAML...', file=sys.stderr)
        print(e, file=sys.stderr)
        sys.exit(1)
        return 0

    count = 0
    # traits読み込み

    with open(obj["traits"]["path"]) as f:
        for line in csv.DictReader(f , delimiter = "\t"):
            count +=1
            # print(line)

        
            # 各パーツの重ね合わせ
            for i in obj['parts']:
                # print(obj['image'][i['name']])

                parts_name = i['name']

                try:
                    if line[parts_name] == "None":
                        continue
                except Exception as e:                    
                    print(e, file=sys.stderr)
                    continue

                if obj['image'][parts_name]['skip'] is True:
                    continue

                condition = obj['image'][parts_name]['condition']

                if condition is True:
                    
                    related_parts = obj['image'][parts_name]['related_parts']
                    path = obj['image'][parts_name]['path'][line[related_parts]]
                    # print(path)

                else:
                    path = obj['image'][parts_name]['path']
                    #  print(path)

                file_path = path+'/'+line[parts_name]+'.png'

                try:
                    Image.open(file_path)
                except Exception as e:                    
                    print(e, file=sys.stderr)
                    pass
                # print(file_path)

                

      
if __name__ == '__main__':
    sys.exit(main(sys.argv))
