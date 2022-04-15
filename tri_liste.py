#rft = regle fusion terminale
def rft(l1: list, l2: list, l3: list) -> list:
    if not (l1 and l2): return l3 + l1 + l2
    else:
        if l1[0] < l2[0]: return rft(l1, l2, l3 + [l1.pop(0)])
        else: return rft(l1, l2, l3 + [l2.pop(0)])

def rftl(l1: list, l2: list, l3: list) -> list: return l3 + l1 + l2 if not (l1 and l2) else (rftl(l1, l2, l3 + [l1.pop(0)]) if l1[0] < l2[0] else rftl(l1, l2, l3 + [l2.pop(0)]))

def tri(l: list, d: int, f: int) -> list:
    """l est votre liste, d défini le début (a logiquement mettre a 0) \nf défini la fin de la liste (a logiquement mettre a taille de la liste -1)"""
    if d == f: return [l[d]]
    else:
        m = (d+f)//2
        x = tri(l, d, m)
        y = tri(l, m+1, f)
        return rftl(x, y, [])

a = [4, 12, 3, 0, -4]
print(tri(a, 0, len(a)-1))
