# 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

class argument_error(Exception):
    pass

def make_character_n_gram(sequence,word_count):
    """
    与えられたシーケンス（文字列やリストなど）から文字単位のn-gramを作る
    """
    try:
        if  type(sequence) is str:
            # 文字列の与え方は考慮しない
            n_gram = [sequence[index:index+word_count] for index in range(len(sequence)) if index+word_count <= len(sequence) ]

        elif type(sequence) is list:
            sequence_str = ''.join(sequence)
            n_gram = [sequence_str[index:index+word_count] for index in range(len(sequence_str)) if index+word_count <= len(sequence_str) ]

        else:
            raise argument_error
    except argument_error:
        print("引数の型が間違っています")
        return sequence
    return n_gram

def make_word_n_gram(sequence,word_count):
    """
    与えられたシーケンス（文字列やリストなど）から単語単位のn-gramを作る
    """
    try:
        if  type(sequence) is str:
            # 文字列は空白で区切られている前提
            print(sequence)
            sequence_arr = sequence.split()
            print(sequence_arr)
            n_gram = [''.join(sequence_arr[index:index+word_count]) for index,word in enumerate(sequence_arr) if index+word_count <= len(sequence_arr) ]

        elif type(sequence) is list:
            n_gram = [''.join(sequence[index:index+word_count]) for index,word in enumerate(sequence) if index+word_count <= len(sequence) ]

        else:
            raise argument_error
    except argument_error:
        print("引数の型が間違っています")
        return sequence
    return n_gram
if __name__ == "__main__":
    print("文字単位n-gramを作成します")
    input_text = input("分割したい文字列を入力してください")
    word_count = int(input("分割単位を入力してください"))
    print("文字単位n-gram\n",make_character_n_gram(input_text,word_count))
    
    print("単語単位n-gramを作成します")
    input_text = input("分割したい文字列を入力してください")
    word_count = int(input("分割単位を入力してください"))
    print("単語単位n-gram\n",make_word_n_gram(input_text,word_count))
