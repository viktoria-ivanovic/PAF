def unesite_koordinate():
    while True:
        try:
            return list(map(float, input("Unesite x i y koordinate: ").split()))
        except ValueError:
            print("Neispravan unos.")

def jednadzba_pravac(t1, t2):
    x1, y1 = t1
    x2, y2 = t2
    if x1 == x2:
        return f"Jednadžba pravca: x = {x1}"
    k = (y2 - y1) / (x2 - x1)
    n = y1 - k * x1
    return f"Jednadžba pravca: y = {k:.2f}x + {n:.2f}"

t1 = unesite_koordinate()
t2 = unesite_koordinate()
if t1 == t2:
    print("Nije definiran pravac.")
else:
    print(jednadzba_pravac(t1, t2))


                                


