def is_possible_to_transform(a, b):
    if len(a) != len(b):
        return "NO"

    count_a = [0] * 26
    count_b = [0] * 26

    for char in a:
        count_a[ord(char) - ord('a')] += 1

    for char in b:
        count_b[ord(char) - ord('a')] += 1

    if count_a != count_b:
        return "NO"

    n = len(a)
    odd_a = set()
    odd_b = set()

    for i in range(n):
        if i % 2 == 0:
            odd_a.add(a[i])
            odd_b.add(b[i])

    if odd_a != odd_b:
        return "NO"

    return "YES"

# Main function
t = int(input())

for _ in range(t):
    a = input()
    b = input()
    print(is_possible_to_transform(a, b))