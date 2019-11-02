# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

string1 = "パトカー"
string2 = "タクシー"
connect_string = ""
for char1,char2 in zip(string1,string2):
    connect_string += char1 + char2

print(connect_string)
