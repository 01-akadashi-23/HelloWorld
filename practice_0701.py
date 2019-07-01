def main():
    f_01()
    f_02()

def f_01():

    input_line = input()
    s = input_line.split(' ')
    for i in range(len(s)):
        print("No.{0} : {1}".format(i + 1,s[i]))

def f_02():
    a = [1,2,3,4,5]
    a[2:4] = ['three','four','five']
    print(a)
    del a[2:]
    print(a)

if __name__ == '__main__':
    main()
