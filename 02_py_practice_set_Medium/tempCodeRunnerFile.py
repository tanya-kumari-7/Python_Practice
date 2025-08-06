## Compress a string (without run-length encoding)


def compress_string_func(x):
    dic_box = {}
    for i  in x :
        if i not in dic_box:
            dic_box[i] = 1
        else :
            dic_box[i] += 1
    result = ''
    for a,b in dic_box.items():
        result += a+str(b)

    return result

print(compress_string_func('sssoonnaammm'))