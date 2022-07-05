import csv
import json
import argparse

# --path 読み込むCSVファイルのパスを指定
# --save Jsonを保存するディレクトリのパス。デフォルトは./Json
parser = argparse.ArgumentParser(description='')
parser.add_argument('--path', required=True,help= 'Path of CSV file to be read.') 
parser.add_argument('--save', default="./Output/Metadata",help= 'Path of the directory where the Json is output.') 

if __name__ == "__main__":

    count = 1
    csv_path = parser.parse_args().path
    json_path = parser.parse_args().save

    with open(csv_path) as f:
        for line in csv.DictReader(f , delimiter = "\t"):
            # print(line)
            json_name= json_path+"/"+str(count)+'.json'
            json_file = open(json_name, 'w')
            attributes=json.loads(line["attributes"])
            line["attributes"]=attributes
            json.dump(line, json_file)
            count = count+1
            