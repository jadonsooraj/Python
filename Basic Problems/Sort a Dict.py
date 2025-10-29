def reverse_dict(dict1:dict)->dict:
    sorted(dict1.items(), key=lambda x: x[0])  # by key
    sorted(dict1.items(), key=lambda x: x[1])  # by value
if __name__=='__main__':
    dict1={'gfg' : 4, 'is' : 2, 'best' : 5}
    print(f'Dictionary: {dict1}')
    print(f'Sort by value: {sorted(dict1,reverse=True)}')
    print(dict1.items())