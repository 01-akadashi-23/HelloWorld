def main():
    print('名前を入力してね')
    input_line = input()
    oracle = uranai(input_line)
    print(oracle)

def uranai(name,hero='Pythonマスター'):
    recipes = ['スパム','豚肉と煮豆とスパム','スパムと卵']
    result = name + 'さんは'
    result += recipes[ord(name[0]) % len(recipes)]
    result += 'を食べると、'+hero+'になれます！'
    return result

if __name__ == '__main__':
    main()
