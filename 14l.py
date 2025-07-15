def reverseString(s):
    l = 0
    r = len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return s

input_str = ['h', 'e', 'l', 'l', 'o']
reversed_str = reverseString(input_str)
print("Reversed string:", reversed_str)
