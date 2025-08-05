## First non-repeating character


def no_reoeat_char_func(x):
    container = {}
    for i in x:
        if i not in container:
            container[i] = 1
        else:
            container[i] += 1
    for i in x:
        if container[i] == 1:
            return i
 
print(no_reoeat_char_func("ssnoam"))  