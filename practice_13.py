# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

import pandas as pd 

if __name__ == '__main__':
    dataset1= pd.read_table("col1.txt",names=(['prefecture']))
    dataset2 = pd.read_table("col2.txt",names=(['municipalities']))
    print(dataset1)
    print(dataset2)
    merge_dataset = pd.concat([dataset1,dataset2],axis=1)
    print(merge_dataset)
    merge_dataset.to_csv('col1pluscol2.txt',header=False,index=False,sep='\t')
    