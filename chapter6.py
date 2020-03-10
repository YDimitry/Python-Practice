# def paths_count(x, y):
#     r =[]
#     c = 1
#     if x > 0:
#         r += [(x-1,y)]
#     if y > 0:
#         r += [(x,y-1)]
#     if r:
#         c = 0
#         for t in r:
#             c += paths_count(*t)
#     return c


# print(*accumulate([(1,0),(0,1)],partial(map,sub)))

# def first(*args,**kwargs):
#     if args:
#         return args[0]
#     if kwargs:
#         return kwargs[sorted(kwargs.keys())[0]]
#     return None

# def call(fun, *args,**kwargs):
#     return fun(*args, **kwargs)

# def header(text,level=1):
#     return f"{'#'*(level>6 and 6 or level if level else 1)} {text}"

# def add(a, b):
#     return a + b

# def f_map(func, l):
#     return map(func, l)

# def header(text,level=1):
#     return f"{'#'*(level>6 and 6 or level if level else 1)} {text}"

# def percent(share, round_digits=None):
    # return f"{round_digits and round(share*100,round_digits) or int(share*100)}%"
    # return f"{round(share*100,round_digits)}%"

# def concat(*str,sep=' '):
#     return sep.join(str)

# from operator import concat as conc
# from functools import reduce
# def concat(*str):
#     return reduce(conc, str)

# def sq_sum(*numbers):
#     return sum(map(flip(pow)(2), numbers))

# def mean(*numbers):
#     return sum(numbers)/len(numbers)


# def func(l):
#     res =[]
#     for i in l:
#         if i not in res:
#             res.append(i)
#     return res

# print(func([1, 2, 2, 3, 4, 3, 6, 2]))

# def func(l1, l2):
#     res = l1[::]
#     for i in l2:
#         if i in res:
#             res.remove(i)
#     return res

# print(func([1, 3, 2, 4, 2], [2, 5]))
# def is_prime(a):
#     return all(map(lambda x: a % x, range(2, int(a**0.5+1))))

# def increase_g():
#     pass
#
# def fahrenheit_to_celcius(degree):
#     return (degree - 32) *5/9
#
# def celcius_to_fahrenheit(degree):
#     return degree *9/5 +32
#
# def multiply(a, b):
#     return a*b
#
# def add_2(a):
#     return a+2
# input = 'l r r * d d # r # l l l d'
# d = {'l':(-1,0,0),'u':(0,1,0),'d':(0,-1,0),'r':(1,0,0),'*':(0,0,1),'#':(0,0,-1)}
# c = map(lambda x:d[x], input.split())
# res = reduce(lambda a,x: a[2]!=0 and tuple(partial(map, add)(a,x)) or a, c, (0,0,1))
# res = reduce(partial(map, add), takewhile(lambda a:a[2],c), (0,0,1))
# print('{} {}\n{}'.format(*res))
# res = reduce(lambda a,x: a[2] and tuple(partial(map, add)(a,x)) or a, c, (0,0,1))
# acc = takewhile(lambda a: a[2]>=0, accumulate(compose(tuple, partial(map,add)), c, (0,0,1)))
# print('{} {}\n{}'.format(*res))

# f = map(curry(flip(get))(d), input.split())
# print(*f)

# print(tuple(partial(map,add)((1,2,3),(1,1,1))))

# a = reduce(partial(map,add),)

# op = {'-':sub,'+':add,'*':mul,'/':truediv}
# l = map(lambda x:curry(flip(op[x[0]]))(float(x[2:])), iter(input,'.'))
# print(reduce(lambda a, f: f(a), list(l), float(input())))


# op = {'-':sub,'+':add,'*':mul,'/':truediv}
# l = list(map(compose(lambda x:curry(flip(op[x[0]]))(float(x[1])), methodcaller('split')), iter(input,'.')))
# print(reduce(lambda a, f: f(a), l, float(input())))

# n = int(input())
# map(lambda x:)
#
# print(*l,n)




# l = iter(input,'.')
# res = list(map(lambda x:x[:-5], filter(lambda x:'true' in x,l)))
# print(*res)
# print(len(res))

# print(*map(lambda x:x[-4:]=='true' and x[:-5],l))


# n = 4
# print(*map(lambda x: ' '*(n-x-1)+'#'*(1+x*2), range(n)),sep='\n')

# i = 'camelCase'
# print(''.join(map(lambda x: x.isupper() and '_'+x.lower() or x, list(i))))
# print(''.join(map(lambda x: ord(x) in range(65,91) and '_'+chr(ord(x)+32) or x,list(i))))

# 97 - 122 a-z
# 65 - 90 A-Z
# print(ord(i))
# print(ord(i) in range(65,91) and chr(ord(i)+32) or i)

# i = 'snake_case'
# l = i.split('_')
# for i in range(1,len(l)):
#     l[i] = l[i].capitalize()
# print(''.join(l))

# h = """ .-.  .-.
# |   \/   |
# \        /
#  `\    /`
#    `\/`   """
#
# k = int(input())
# for i in h.split('\n'):
#     print(i*k)


# a = input
# print(a.isnumeric() and int(a)*2 or a*2)
# print(*reversed(list(map(int,input.split()))))
# """
# в пустой (мёртвой) клетке, рядом с которой ровно три живые клетки, зарождается жизнь;
# если у живой клетки есть две или три живые соседки, то эта клетка продолжает жить;
# в противном случае, если соседей меньше двух или больше трёх, клетка умирает
# """

# def live_or_die(i,j):
#     c = 0
#     for k,l  in [(1,0),(1,1)]:
#         for n in range(4):
#             if -1 < i+k <10 and -1 < j+l <10:
#                 c += init[i+k][j+l] == '#'
#             k, l = -l, k
#     return '.#'[init[i][j]=='.' and c == 3 or init[i][j]=='#' and 1 < c < 4]

# init = [['.', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
#         ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
#         ['#', '#', '#', '.', '.', '.', '.', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]

# for _ in range(15):
#     init = [[live_or_die(i,j) for j in range(10)] for i in range(10)]
#
# print(*init,sep='\n')

# print(init[i][j],end='')
# print()

# init = '#....#'
# elem = lambda seq: map(lambda x: x=='#','.'+seq+'.')
# live_or_die = lambda x: (x[0] ^ x[2]) or (not x[1] and x[0] and x[2])
# for _ in range(int(input())):
#     init = reduce(lambda a, x: a+'.#'[live_or_die(x)], sliding_window(3,elem(init)),'')
#
# print(list(init))

# lst = list(map(int,iter(input,'.')))
# print(list(filter(lambda x: x<3,lst))+list(filter(lambda x:x>=3,lst)))
# n = int(input())
# print(*[['#']*n]*n,sep='\n')

# print(list(concat(juxt(curry(filter)(lambda x: x<3),curry(filter)(lambda x:x>=3))(list(map(int,iter(input,'.')))))))
# print(*map(juxt(curry(filter)(lambda x: x<3),curry(filter)(lambda x:x>=3)),tee(map(int,iter(input,'.')),2)))

# lst = list(map(int,iter(input,'.')))
# lst2 = topk(3,lst)
# # print(list(concat([reversed(lst2),filter(lambda x: x not in lst2, lst)])))
# for i in lst2:
#     lst.remove(i)
# print(list(lst2)+lst)

# lst = list(map(int,iter(input,'.')))
# m = max(lst)
# lst.remove(m)
# lst.insert(0,m)
# print(lst)

# print(list(filter(identity,concat(zip_longest(*[input() for _ in range(2)])))))
# print(list(map(compose(flip(truediv)(2),sum),sliding_window(2,map(int,input)))))
# print(list(accumulate(map(int,input),compose(flip(truediv)(2),add))))
# print(truediv(*reduce(partial(map,add),zip(input,repeat(1)))))
# print(list(map(int,input)))


# print(pow(sum(map(curry(flip(pow)(2)), coord)), 0.5))
# print(("NO","YES")[float(input())>pow(sum(map(curry(flip(pow)(2)), coord)), 0.5)])
# print(("NO","YES")[eq(*partition(2,map(curry(lt)(0),[float(input()) for _ in range(4)])))])
# print('1423'[int(''.join(map(lambda x:str(int(x<0)),coord)),2)])
# print(truediv(*reduce(partial(map,add),zip(map(int,iter(input, '.')), repeat(1)), (0,0))))
# print(sum(map(curry(flip(pow))(2),map(int,iter(input, '.')))))
# print(*map(curry(pow)(2),map(float,['3','4'])))

# print(max(map(float, iter(input, '.'))))
# print(sorted(map(float, iter(input, '.')))[-2])

# print(max(remove(lambda x: x==max(seq),seq)))
# print(sum(take_nth(2, map(float, iter(input, '.')))))
# fib = list(takewhile(curry(ge)(n), map(item(0), accumulate(repeat((0, 1)), lambda a, _: juxt(item(1), sum)(a)))))
# print(reduce(lambda a,_:juxt(item(1),sum)(a), range(8),(0,1)))
# print(("prime", "composite")[any(map(lambda x:not a%x, range(2,a)))])
# print(compose(sum,partial(map,curry(flip(pow))(2)))(range(1,6)))
# print(sum(filter(lambda x:x%2,range(1,2*2))))
# print(sum(range(1,int(input())+1)))
# a = int(input())
# print(*[a] if a%3 and a%5 else ['Fizz','Buzz'][1-(not a%3):1+(not a%5)])
# print(sorted(map(int, [input() for _ in range(3)])), sep='\n')
# print(('BLACK','WHITE')[(x-1)%2 ^ (y-1)%2])
# coord = partition(2,list(map(int, input.split())))
# print(("NO", "YES")[max(partial(map, compose(abs,sub))(*coord))==1])
# print(max(map(int,[input() for _ in range(3)])))

# s = input()
# if int(s[-1]) in [0,range(5, 10)] or len(s)>1 and int(s[-2]) == 1:
#     print(s,"studentov")
# elif int(s[-1]) in range(2,5):
#     print(s,"studenta")
# else:
#     print(s,"student")

# print(['zero','one','two','three','four','five','six','seven','eight','nine'][int(input())])

# s = [int(input()) for _ in range(2)]
# print(0 if s == s[::-1] else s.index(max(s))+1)

# s = int(input())
# print(0 if s == 0 else s//abs(s))