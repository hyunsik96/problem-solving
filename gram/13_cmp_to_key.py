from functools import cmp_to_key

def compare(x, y):
    if x+y > y+x:
        return -1
    elif x+y == y+x:
        return 0
    else:
    	return 1

l = ['34', '37', '9', '31', '3']

print(sorted(l, key=cmp_to_key(compare)))
#['9', '37', '34', '3', '31']