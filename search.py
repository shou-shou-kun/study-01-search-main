
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

import csv

 # CSVを読み込みリストに
with open("read.csv",'r',encoding="utf-8_sig") as f:
    for row in csv.reader(f):
        source = row
        # print(source)
        # print(f"{row}")
        # print(f"{type(row)}")
        
# 検索ソース
# source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く
    
    if word in source:
        print("{}が見つかりました".format(word))
    
    else:
        print("{}は見つかりませんでした".format(word))
        
        # リストに追加する
        print("{}をリストに追加します".format(word))
        source.append(word)
        print(source)    
        
        # CSVファイルに書出し
        with open('writer.csv','w',encoding="utf-8_sig") as f:
            writer = csv.writer(f)
            writer.writerows([source])
        # with open('writer.csv','r',encoding="utf-8_sig") as f:
        #     print(f.read())    
        
if __name__ == "__main__":
    search()
