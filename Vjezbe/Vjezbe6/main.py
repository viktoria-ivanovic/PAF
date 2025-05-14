from harmonic_oscilator2 import harmonic_oscilator
import math

masa = 1.0
k = 1.0
x0 = 1.0
v0 = 0.0

oscilator = harmonic_oscilator(masa, k, x0, v0)

omega = math.sqrt(k / masa)
T_analiticki = 2 * math.pi / omega

koraci = [0.1, 0.01, 0.001]

print(f"{'dt':>10} | {'T_num (s)':>10} | {'T_ana (s)':>10} | {'Greška (%)':>12}")
print("-" * 45)

for dt in koraci:
    T_numericki = oscilator.odredi_period(dt)
    greska = abs(T_numericki - T_analiticki) / T_analiticki * 100
    print(f"{dt:10.5f} | {T_numericki:10.5f} | {T_analiticki:10.5f} | {greska:12.5f}")
