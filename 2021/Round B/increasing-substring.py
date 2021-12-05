def increasing_substrings(s):
    arr = []
    t = ""
    for c in s:
        if (len(t) == 0 or c > t[-1]): t += c
        else: t = c
        arr.append(len(t))
    return arr

num_cases = int(input())
for i in range(1, num_cases + 1):
    _ = input()
    s = input()
    print("Case #" + str(i) + ":", end = "")
    for x in increasing_substrings(s):
        print(" " + str(x), end = "")
    print()