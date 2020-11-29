a_str = 'abcdefg'

for i in a_str:
    print('find一个字符%s' %i)
    if i == 'd':
        break

else:
    print('走else了')