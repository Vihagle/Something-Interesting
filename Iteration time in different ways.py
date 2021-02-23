import time
def time_count(func):
    def wrapper(*args):
        start = time.perf_counter()
        func(*args)
        end = time.perf_counter()
        print(f'It costs {end-start}s')
    return wrapper

#Method 1
@time_count
def iterate_1(var):
    ls = []
    for i in range(len(var)):
        ls.append(var[i].upper())
    print(ls)

#Method 2    
@time_count
def iterate_2(var):
    res = list(map(lambda x:x.upper(),var))
    print(res)

#Method 3
@time_count
def iterate_3(var):
    res_1 = [fruit.upper() for fruit in var]
    print(res_1)

var = ['apple','pear','orange','banana']
iterate_1(var)
iterate_2(var)
iterate_3(var)
