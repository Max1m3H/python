def mini(l: list) -> int:
    """Retourne le minimum d'une liste"""
    if isinstance(l, list):
        if len(l) == 1:
            return l[0]
        else:
            if l[0] < l[-1]:
                return mini(l[:-1])
            else:
                return mini(l[1:])

def m(l: list) -> int: return l[0] if len(l) <= 1 else (m(l[:-1]) if l[0] < l[-1] else m(l[1:])) if isinstance(l, list) else -1

def mm(l: list) -> int: return (l[0] if len(l) <= 1 else mm(l[not (n := (l[0] < l[-1])) : -n or None])) if hasattr(l, "__getitem__") else -1

def cm(k: list, j = []) -> list:
    l = k.copy()
    for i in k:
        a = mm(k)
        l.remove(a)
        j.append(a)
        return cm(l)
    return j
