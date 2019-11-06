# 08. 暗号文
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．

# https://python.civic-apps.com/char-ord/
def cypher(text):
    cypher_text = ""
    for char in text:
        if char.islower():
            print(char)
            #ord:string型からアスキーコードを返す
            cypher_text = cypher_text + str(219 - ord(char))
        else:
            cypher_text += char
    return cypher_text
if __name__ == '__main__':
    input_text = input("文字列を暗号化します。文字列を入力してください")
    cypher_text= cypher(input_text)
    print(cypher_text)