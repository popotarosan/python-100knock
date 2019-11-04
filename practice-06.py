# 06. 集合
# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

class argument_error(Exception):
    pass

def make_character_n_gram(sequence,word_count):
    """
    与えられたシーケンス（文字列やリストなど）から文字単位のn-gramを作る
    """
    try:
        if  type(sequence) is str:
            # 文字列の与え方は考慮しない
            n_gram = [sequence[index:index+word_count] for index in range(len(sequence)) if index+word_count <= len(sequence)]

        elif type(sequence) is list:
            sequence_str = ''.join(sequence)
            n_gram = [sequence_str[index:index+word_count] for index in range(len(sequence_str)) if index+word_count <= len(sequence_str)]

        else:
            raise argument_error
    except argument_error:
        print("引数の型が間違っています")
        return sequence
    return n_gram
if __name__ == "__main__":
    word1 = "paraparaparadise"
    word2 = "paragraph"
    print('bi-gram1',make_character_n_gram(word1,2))
    print('bi-gram2',make_character_n_gram(word2,2))

    word1_char_bi_gram_set = set(make_character_n_gram(word1,2))
    print('X集合',word1_char_bi_gram_set)
    word2_char_bi_gram_set = set(make_character_n_gram(word2,2))
    print('Y集合',word2_char_bi_gram_set)
    print("和集合:",word1_char_bi_gram_set | word2_char_bi_gram_set)
    print("積集合:",word1_char_bi_gram_set & word2_char_bi_gram_set)
    print("差集合X-Y:",word1_char_bi_gram_set - word2_char_bi_gram_set)
    print("差集合Y-X:",word2_char_bi_gram_set - word1_char_bi_gram_set)
    if 'se' in word1_char_bi_gram_set:
        print("'se'というbi-gramはXに含まれます")
    else:
        print("'se'というbi-gramはXに含まれません")
    
    if 'se' in word2_char_bi_gram_set:
        print("'se'というbi-gramはYに含まれます")
    else:
        print("'se'というbi-gramはYに含まれません")
        
    
