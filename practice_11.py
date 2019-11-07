# 11. タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
if __name__ == '__main__':
    count = 0
    with open("hightemp.txt",mode="r",encoding='utf-8') as read_file:
        with open("new_hightemp.txt",mode="w",encoding='utf-8') as write_file:
            for line in read_file:
                newline = line.replace("\t"," ")
                write_file.write(newline)
    

# cat hightemp.txt | sed -e s/$'\t'/' '/g
# https://mattintosh.hatenablog.com/entry/2013/01/16/143323