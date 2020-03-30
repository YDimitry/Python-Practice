# 10.1 Генераторы (comprehensions)

# step 10
def simple_gen(n):
    num = 2
    num_list = []
    while n:
        yield num
        num_list.append(num)
        while any(map(lambda x: not num % x, num_list)):
            num += 1
        n -= 1

# print(*simple_gen(200))

# step 1
# a = [i for i in range(1,2001)]

# step 2
# a = [i for i in range(1,10001) if not i % 3]

# step 3
# a = [int(i) for i in input().split()]

# step 4
# a = [pow(int(i),2) for i in input().split()]

# step 5
# a = {i: pow(int(n), 2) for i, n in enumerate(input().split())}

# step 6
# a = [i.split(':')[1] for i in input().split()]

# step 7
# a = {int(s.split(':')[0]):s.split(':')[1] for s in input().split()}

# step 8
# print(sum(map(int,[input() for _ in range(int(input()))])))

# step 9
# [print(*[j%10 for j in range(i,10+i)],sep='') for i in range(10)]

# step 10
# a = [i for i in range(2,1000) if all(map(lambda x: i % x, range(2,int(pow(i,0.5))+1)))]


