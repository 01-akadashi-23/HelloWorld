def main():
    # dict_update()
    dict_methods()

def dict_update():
    rssitem = { 'title':'Pythonを勉強中',
                'link':'http://',
                'dc:date':'2019-07-09'}
    rssitem.update({'title':'Pythonを勉強中',
                    'dc:creator':'someone'})
    print(rssitem.keys())
    print(rssitem)

def dict_methods():
    s = {'one':'いち',
         'two':'に',
         'three':'さん',
         'four':'よん'}

    print(s.keys())

    print(s.get('three'))
    print(s.get('five'))
    print(s.get('five','登録されていません'))

    print(s.setdefault('one'))
    print(s.setdefault('five','ご'))
    print(s.setdefault('five','いち'))

    print(s.items())

    print(s.values())

if __name__ == '__main__':
    main()
