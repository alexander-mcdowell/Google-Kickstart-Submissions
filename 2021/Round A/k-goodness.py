def get_min_changes(s, k):
    goodness = 0
    n = len(s)
    for i in range(int(n / 2)):
        if (s[i] != s[n - i - 1]): goodness += 1
    if (goodness == k): return 0
    else: return abs(k - goodness)

num_cases = int(input())
for i in range(num_cases):
    _, k = input().split(" ")
    k = int(k)
    s = input()
    print("Case #" + str(i + 1) + ": " + str(get_min_changes(s, k)))