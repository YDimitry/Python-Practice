from functools import partial
from operator import add, sub, truediv, mul



# def fix_duplicates(ids):
#     return [ids[:i].count(v) and f"{v}_{ids[:i].count(v)}" or v for i, v in enumerate(ids)]

# d = {'+':add,'-':sub,'/':div,'*':mul}

# def calc(a, op, b):
#     return d[op](a,b)

# def average_attempts(attempts, names):
#     iddic = {id:name for id,name in names}
#     res = dict()
#     for id,p_id,a in attempts:
#         lst = res.setdefault(iddic[id],[])
#         lst += [a]
#     for name,at in res.items():
#         res[name] = sum(at)/len(at)
#     return res

# average_attempts(attempts, names) # {'Random': 23.0, 'Arkady': 0.0}

# d = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
#
# def code_number(num):
#     return ' '.join(map(lambda n: d[int(n)], str(num)))

# def dog_owners(pets):
#     res = dict()
#     for el in pets:
#         a = res.setdefault(el[1:], [])
#         a += [el[0]]
#     return res


# def update_age(owners, owner, new_age):
#     owners[owner[:2] + (new_age,)] = owners.pop(owner)


# def max_par(a, b, c):
#     return a < 0 and (-b/(2*a),c-b**2/(4*a)) or None

# def character_count(s):
#     return {e:s.count(e) for e in s}

# def vector_sum(v1, v2):
#     return tuple(partial(map, add)(v1, v2))


