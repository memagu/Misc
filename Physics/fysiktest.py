m1 = 3
m2 = 4.5

F1 = m1 * -9.82
F2 = m2 * 9.82

Fres = F2 + F1

a = Fres / (m1 + m2)

print(f"acceleration :{a}\n")

Fres1 = a * m1
Fres2 = a * m2

Fs1 = -1 * F1 + Fres1
Fs2 = F2 - Fres2

print(f"Spännkraft beräknand utifrån negativ respektive positiv riktning: {Fs1, Fs2}\n")

Fsres1_1 = Fs1 + F1
Fsres1_2 = Fs2 + F1

Fsres2_1 = F2 - Fs1
Fsres2_2 = F2 - Fs2

print(f"Bräknad resulterande kraft på massan {m1} med vardera spännkraftsberäkning {Fsres1_1, Fsres1_2}")
print(f"Bräknad resulterande kraft på massan {m2} med vardera spännkraftsberäkning {Fsres2_1, Fsres2_2}\n")

a1_1 = Fsres1_1 / m1
a1_2 = Fsres1_2 / m1

a2_1 = Fsres2_1 / m2
a2_2 = Fsres2_2 / m2

print(f"Bräknad acceleration hos massan {m1} med vardera resultantkraftberäking: {a1_1, a1_2}")
print(f"Bräknad acceleration hos på massan {m2} med vardera resultantkraftberäking: {a2_1, a2_2}")
