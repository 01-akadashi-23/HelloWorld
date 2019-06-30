def main():
    print(add_tax("Goods 1000 2019/06/30"))
    print('文字列を入力してください（半角英数のみ）')
    input_line = input()
    print(oftenUseMethods(input_line))

def add_tax(astring):
    items = astring.split()
    price = int(items[1]) * 1.1 #消費税の追加…ってか１０％に引き上げるな
    items[1] = str(int(price))
    return " ".join(items)

def oftenUseMethods(s):
    return s
    # NOTE: ここから先のメソッドは、ただのメモ書きです
    s.find('abc',[0],[len(s)]) #最初に見つかった位置を0から始まるインデックスとして返す。rfindで末尾（右）から検索する
    s.index('def',[0],[len(s)]) #find()と同じように動作する。見つからなかった場合ValueErrorを返す。rindexで末尾（右）から
    s.endwith('ghi',[0],[len(s)]) #検索した文字列で終わっていた場合、Trueを返す
    s.startwith('jkl',[0],[len(s)]) #検索した文字列で始まっていた場合、Trueを返す
    s.split(' ',[0]) #指定した文字列で区切り、そのリストを返す。分割数を指定できる。rsplitで末尾（右）から分割できる（要分割数指定）
    s.join(['abc','def','ghi']) #シーケンス内の要素（文字列）を s で連結し、そのコピーを返す
    s.strip('jkl') # s から指定した文字列を削除し、そのコピーを返す（指定がない場合は空白を削除）。lstripは先頭のみ、rstripは末尾のみ対象
    s.upper() # s の英字小文字を大文字に変換、そのコピーを返す
    s.lower() # s の英字大文字を小文字に変換、そのコピーを返す
    s.ljust(10) # s の幅（数値）を考慮して左寄せ、そのコピーを返す。長さが幅に満たない場合、空白（もしくは指定文字列）で埋める。
    s.rjust(20,'w') # 同様に右寄せ、そのコピーを返す。center()は中央寄せを行う

if __name__ == '__main__':
    main()
