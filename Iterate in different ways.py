import time
def time_count(func):
    def wrapper(*args):
        start = time.perf_counter()
        func(*args)
        end = time.perf_counter()
        print(f'It costs {end-start}s')
    return wrapper

@time_count
def iterate_1(var):
    ls = []
    for i in range(len(var)):
        ls.append(var[i].upper())
    print(ls)

@time_count
def iterate_2(var):
    res = list(map(lambda x:x.upper(),var))
    print(res)