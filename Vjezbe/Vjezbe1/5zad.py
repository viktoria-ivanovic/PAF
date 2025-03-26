import matplotlib.pyplot as plt

def unesite_koordinate():
    while True:
        try:
            return list(map(float, input("Unesite x i y koordinate (odvojene razmakom): ").split()))
        except ValueError:
            print("Pogrešan unos.")

def jednadzba_pravca(t1, t2):
    x1, y1 = t1
    x2, y2 = t2
    if x1 == x2:
        print(f"Jednadžba pravca: x = {x1}")
        return None, None
    k = (y2 - y1) / (x2 - x1)
    n = y1 - k * x1
    print(f"Jednadžba pravca: y = {k:.2f}x + {n:.2f}")
    return k, n

def nacrtaj_graf(t1, t2, k, n):
    x1, y1 = t1
    x2, y2 = t2
    x_vals = [x1 - 1, x2 + 1]
    y_vals = [k * x + n for x in x_vals] if k is not None else [y1, y2]
    
    plt.plot(x_vals, y_vals, 'b-')
    plt.scatter([x1, x2], [y1, y2], color='red')
    plt.grid()
    
    if input("Spremiti graf kao PDF?: ").lower() == 'da':
        plt.savefig(input("Naziv datoteke: ") + ".pdf")
    else:
        plt.show()

def main():
    print("Unesite koordinate za dvije točke.")
    t1 = list(unesite_koordinate())
    t2 = list(unesite_koordinate())
    if t1 == t2:
        print("Nema pravca.")
    else:
        k, n = jednadzba_pravca(t1, t2)
        nacrtaj_graf(t1, t2, k, n)

if __name__ == "__main__":
    main()