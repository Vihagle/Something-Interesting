ls = [7,3,5,2,6,1]
m = len(ls)
def compare(ls,m):
        for i in range(m-1):
            for j in range(i+1,m):
                res = max(ls[i],ls[j])
                if res == ls[i]:
                    ls[i],ls[j] = ls[j],ls[i]
                    return compare(ls,m)
                else:
                    continue
        return ls

print(compare(ls,m))