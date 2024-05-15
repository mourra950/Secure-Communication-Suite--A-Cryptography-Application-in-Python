t = dict()
print(t)
# t['omar']
if 'omar' in t:
    print('found')
else:
    print('not found')
    t['omar'] = []
    t['omar'].append(('hello1',1))
    t['omar'].append(('hello2',2))
    t['omar'].append(('hello3',2))
    t['omar'].append(('hello4',2))
    t['omar'].append(('hello5',2))
    t['omar'].append(('hello6',2))
    t['omar'].append(('hello7',2))
    


if 'omar' in t:
    for i in t['omar']:
        print(i)
else:
    print('no omar')
