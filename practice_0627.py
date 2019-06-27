def main():
    #listに対して使うappend,extend
    a = [1,2,3,4,5]
    a.append(100)
    print(a)

    a.append([200,300,400])
    print(a)

    b = [1000,2000,3000]
    a.extend(b)
    print(a)

    #ディクショナリ
    dic = {"No.025":"ピカチュウ",
           "No.151":"ミュウ"}
    print(dic["No.025"])
    dic['No.001'] = 'フシギダネ'
    del dic['No.151']
    print(dic)
    print(dic.keys())

    #タプル
    tuple = (1,2,3,4,5)
    tuple = tuple + (100,200,300)
    print(tuple)
    # ※タプルは基本的にはリストと同じだが、要素は変更できない

if __name__ == '__main__':
    main()
