## Anagram check between two strings


def Anagram_check_func(x,y):
    if len(x) != len(y):
        print(f"{x} and {y} are not a anagram")
        return
    elif len(x) == len(y) and sorted(x) == sorted(y):
        print(f"{x} and {y} are  a anagram")
        return
    else:
        print(f"{x} and {y} are not a anagram")
        return


   
print(Anagram_check_func("sonam","snoa"))  