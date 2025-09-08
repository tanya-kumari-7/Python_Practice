## Compress a string (with run-length encoding)


def compress_string_func(x):
    dic_box = ''
    count = 1
    for i  in range(1,len(x)) :
        if x[i] == x[i-1]:
            count += 1
        else:
            dic_box += x[i-1] + str(count)
            count = 1
    dic_box += x[-1] + str(count)
    return dic_box

print(compress_string_func('sssoonnaammm'))
    