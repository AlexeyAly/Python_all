mixed_list = ['a', 'ab', 3, 5, 1, 8, 0, 'c', 'ac', 'aab']
ml=map(lambda x: str(x),mixed_list)


print(*sorted(mixed_list,key=str))