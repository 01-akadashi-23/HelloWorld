def main():
    print(to_lower('A'))
    print(to_lower('PYTHON'))

    a = ['abc','def','BCD','EFG']
    a.sort()
    print(a)

    a.sort(key = to_lower)
    print(a)
    # 反転
    a.reverse()
    print(a)
    # 要素の削除
    a.remove('BCD')
    print(a)
    # 要素・シーケンスの追加
    a.append('ghi')
    a.append(['あいうえお','かきくけこ'])
    a.extend(['one','two','three'])
    print(a)
    # 要素を１つ取り除く
    a.pop() # 指定がない場合は末尾
    a.pop(0)
    a.pop(3)
    print(a)

    # set型 「集合」・スライス、インデックスは使えない
    print('↓set型のデータ操作練習')
    s = {1,2,3,4}
    n = {1,3,5,7,9}
    print(s)
    s.add(5)
    s.add(2)# ・同じ要素は追加できない。
    print(s)
    # [&],[|]を使って演算が可能
    print(s & {2,3,'four','five'}) # 共通する要素のコピーを返す
    # 以下のメソッドは使ったset型は書き換えない
    print(s.union(n)) # 和集合(s | n)。重複しない要素を持つ集合を返す
    print(s.intersection(n)) # 共通集合(s & n)。どちらにもある要素を持つ集合を返す
    print(s.difference(n)) # 差集合(s - n)。sからnの重複する要素を除いた集合を返す
    print(s.symmetric_difference(n)) # 対照的差集合(s ^ n)。s・nどちらか一方に含まれる要素を集めた集合を返す


def to_lower(s):
    return s.lower()

if __name__ == '__main__':
    main()
