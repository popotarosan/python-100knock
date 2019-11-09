# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

import pandas as pd 

if __name__ == '__main__':
    dataset = pd.read_table("hightemp.txt",header=None)
    dataset1 = dataset.iloc[:,0]
    dataset1.to_csv('col1.txt',header=False,index=False)
    dataset1 = dataset.iloc[:,1]
    dataset1.to_csv('col2.txt',header=False,index=False,sep='\t')

