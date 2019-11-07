# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．

if __name__ == '__main__':
    count = 0
    with open("hightemp.txt",mode="r",encoding='utf-8') as f:
        for line in f:
            count += 1
    print("htightemp.txtの行数は",count)

