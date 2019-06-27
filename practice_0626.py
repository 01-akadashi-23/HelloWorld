def main():
    #文字列の変更、inの使い方
    address = 'アイウエオ'
    print(address)
    print('ア' in address)
    print('カ' in address)
    address = address.replace('イウエオ','カサタナ')
    print(address)

    #リストについて
    sample = [10,200,3000]
    print(sample)
    print(max(sample),min(sample))
    sample.sort()
    print(sample)
    sample.reverse()
    print(sample)

if __name__ == '__main__':
    main()
