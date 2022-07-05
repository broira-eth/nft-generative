import sys
import yaml
from PIL import Image
import csv
import time
import argparse

## --config configファイルのパス

parser = argparse.ArgumentParser()
parser.add_argument('--config', default='./Config/config.yaml')
parser.add_argument('--save', required=True,help= 'Path of the file to be saved') 
args = parser.parse_args()

def main(argv):

    save_file_path = parser.parse_args().save
    start = time.perf_counter()
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
            print(line)
 
            img_last = Image.new("RGBA", (obj["size"]["height"],obj["size"]["width"]))
            
            # 各パーツの重ね合わせ
            for i in obj['parts']:
                # print(obj['image'][i['name']])

                parts_name = i['name']

                if line[parts_name] == "None":
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
                # print(file_path)

                # 画像読み込み＆合成
                img = Image.open(file_path).convert('RGBA')
                img_last = Image.alpha_composite(img_last, img)

            save_file_name = str(count).zfill(4)+'.png'
            img_last.save( save_file_path+"/"+save_file_name)
               
            t = time.perf_counter() - start
            print(save_file_name+" "+ str('{:.1f}'.format(t))+"s")
        
if __name__ == '__main__':
    sys.exit(main(sys.argv))
