# step 2
def line_count(filename):
    return len(open(filename, encoding='utf-8').readlines())

# step 3
def char_count(filename):
    return len(open(filename, encoding='utf-8').read())
# print(char_count('README.md'))

# step 4
def sum_numbers(filename):
    return sum(map(int, open(filename, encoding='utf-8').read().split()))

# step 5
def write_message(filename, message):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(message)

# step 6
def log(filename, message):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(message+'\n')

# step 7
def total_sum(filename):
    return sum(map(float, open(filename, encoding='utf-8').read().split()))
# print(total_sum('testflie'))

# step 8
def minmax_coords(filename):
    a, b = zip(*[map(int,line.split()) for line in open(filename, encoding='utf-8').readlines()])
    return min(a),max(a),min(b),max(b)

# print(minmax_coords('testflie'))

# step 9
# step 10
from itertools import groupby
from operator import itemgetter

def solved_tasks(filename):
    with open(filename, encoding='utf-8') as f:
        li = [list(map(int,line.split(','))) for line in f.readlines()]
        return {k:len({x[1] for x in v}) for k,v in groupby(li,key=itemgetter(0))}


# step 11
# функция возвращает среднюю длину лепестка (petal.length)
import pandas as pd

def mean_petal(filename, variety):
    data = pd.read_csv(filename)
    return data[data.variety == variety]['petal.length'].mean()

def mean_petal(filename, variety):
    li = open(filename, encoding='utf-8').readlines()
    a = [float(line.split(',')[2]) for line in li[1:] if variety in line]
    return sum(a)/len(a)
