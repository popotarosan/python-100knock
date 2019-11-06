# 09. Typoglycemia
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
import random

def convert_sentence(sentence):
    # まずは文を単語分割
    sentence_arr = sentence.split(" ")
    convert_sentence_arr = []
    print(sentence_arr)
    for word in sentence_arr:
        if len(word) > 4:
            new_word = ''.join(random.sample(word,len(word)))
            print(new_word)
            convert_sentence_arr.append(new_word)
        else:
            convert_sentence_arr.append(word)
    print(convert_sentence_arr)
    new_sentence = ' '.join(convert_sentence_arr)
    return new_sentence

if __name__ == '__main__':
    sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    new_sentence = convert_sentence(sentence)
    print('convert_sentence:',new_sentence)