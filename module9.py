# 9.1 Множества

# step 1
# print(*set(input()))

# step 2
# a, b = [set(input().split(', ')) for _ in range(2)]
# print(', '.join([m for m in set(a) if m in b]))
# print(', '.join(a & b))

# step 3
# a, b = [set(input().split()) for _ in range(2)]
# print(a == b and 'YES' or 'NO')

# step 4
# a, b = [set(input().split(', ')) for _ in range(2)]
# print(', '.join(a | b))

# step 5
# n = int(input())
# a, b = [set(input().split(', ')) for _ in range(2)]
# print(n - len(a|b))

# step 6
# a, b = [set(input().split(', ')) for _ in range(2)]
# print(', '.join(a - b))

# step 7
# a, b = [set(input().split(', ')) for _ in range(2)]
# print((a-b)|(b-a))
# print((a|b)-(a&b))
# print(a^b)

# step 8
# def friends(pairs):
#     d = {}
#     for a, b in pairs:
#         for _ in range(2):
#             d.setdefault(a, set()).add(b)
#             a, b = b, a
#     return d
# print(friends([("Ivan", "Maria"),("Ella", "Ivan"),("Ivan", "Oleg")]))












