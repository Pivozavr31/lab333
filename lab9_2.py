from itertools import permutations
def chekwrd(arr):
    for p in permutations(arr):
        f = True
        for i in range(len(p) - 1):
            x = p[i]
            y = p[i+1]
            if x[-1] != y[0]:
                f = False
                break
        if f:
            return True
    return False
truuue = ['excavate','endure','desire','screen','theater','excess','night']
print(chekwrd(truuue))
falsee = ['trade','pole','view','grave','ladder','mushroom','president']
print(chekwrd(falsee))
