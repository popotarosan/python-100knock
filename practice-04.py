# 04. 元素記号
# "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

string = ("Hi He Lied Because Boron Could Not Oxidize Fluorine. "
          "New Nations Might Also Sign Peace Security Clause."
          "Arthur King Can.")
#文に区切る
word_split_sentence = string.split(".")
word_split_sentence.pop(-1)
# print(word_split_sentence)
#区切った文に対してループを回す
#先頭の空白削除
#空白で文字分割
set1 = {1,5,6,7,8,9,15,16,19}
string_dict = {}
index = 0
for sentence in word_split_sentence:
    
    if sentence[0] == " ":
        sentence = sentence[1:]
    word_arr = sentence.split(" ")
    for word in word_arr:
        index = index + 1
        if index in set1:
            string_dict[word[0]] = index
        else:
            string_dict[word[0:2]] = index

print(string_dict)