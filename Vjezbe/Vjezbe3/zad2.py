def test_preciznost(N):
    value = 5
    for _ in range(N):
        value += 1/3
    for _ in range(N):
        value -= 1/3
    return value

for n in [200, 2000, 20000]:
    result = test_preciznost(n)
    print(f"Konačni rezultat za {n} iteracija: {result}")
