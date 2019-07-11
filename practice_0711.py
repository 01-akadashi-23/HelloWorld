def main():
    input_line = input()
    use_in(input_line)
    use_enumerate(input_line)

def use_in(s):
    items = s.rstrip().split(' ')
    for i in range(len(items)):
        if isinstance(items[i],str):
            if 'a' in items[i]:
                print('Found \"a\"! >>'+items[i])
            else:
                print('Not found \"a\"…')
        else:
            continue

def use_enumerate(s):
    s = s.rstrip().split(' ')
    for cnt,item in enumerate(s):
        print(cnt,item)

if __name__ == '__main__':
    main()
