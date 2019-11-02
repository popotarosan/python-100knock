# 03. 円周率
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
# 文に分割
string_sentence_arr = string.split(".")
# 最後は空白ができるので削除
string_sentence_arr.pop(-1)
# 文字数を格納する配列を初期化
string_wordnum_arr = []
for sentence in string_sentence_arr:
    sentence_word_arr = sentence.split(" ")
    for word in sentence_word_arr:
        string_wordnum_arr.append(len(word))
print(string_wordnum_arr)





