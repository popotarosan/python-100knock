# 07. テンプレートによる文生成
# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
def get_templatestring(x,y,z):
    import string
    string_template = '$time時の$keyは$value'
    context = {'time':x,'key':y,'value':z}
    template = string.Template(string_template)
    template_string = template.substitute(context)
    return template_string

if __name__ == '__main__':
    template_string = get_templatestring(12,'気温',22.4)
    print(template_string)