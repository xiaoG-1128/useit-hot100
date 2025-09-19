from operator import ifloordiv


def min_window(s:str,t:str)-> str:
    from collections import Counter

    need = Counter(t)
    window = {}
    left = right = valid = 0
    start,min_length = 0,flaot('inf')

    while right < len(s):
        c =  s[right]
        right +=1

        if c in need:
            window[c] = window.get(c,0) + 1
            if window[c] == valid:
                valid += 1

        while valid == len(need):
            if right-left < min_length:
                start, min_length = left, right-left

            d = s[left]
            left += 1

            if d in need:
                if window[d]==valid:
                    valid -= 1
                    window[d] -=1

    return ""if min_length == float('inf')else s[start:start + min_length]

