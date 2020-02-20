n_dict = [1,2,3,4,5,6,7,8,9,10]
result = []
import copy

def power_set(set_, i):
    if sum(set_)>10:
        return
    if i==10:
        result.append(set_)
        return
    else:
        a = copy.copy(set_)
        b = copy.copy(set_)
        a.append(n_dict[i])
        return power_set(a, i+1), power_set(b, i+1)

power_set([],0)

for i in result:
    print(i)