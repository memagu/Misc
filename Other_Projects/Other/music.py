import winsound

C = [16, 33, 65, 131, 262, 523, 1047, 2093, 4186]
Cs = [17, 35, 69, 139, 277, 554, 1109, 2217, 4435]
D = [18, 37, 73, 147, 294, 587, 1175, 2349, 4699]
Ds = [19, 39, 78, 156, 311, 622, 1245, 2489, 4978]
E = [21, 41, 82, 165, 330, 659, 1319, 2637, 5274]
F = [22, 44, 87, 175, 349, 698, 1397, 2794, 5588]
Fs = [23, 46, 93, 185, 370, 740, 1480, 2960, 5920]
G = [25, 49, 98, 196, 392, 784, 1568, 3136, 6272]
Gs = [26, 52, 104, 208, 415, 831, 1661, 3322, 6645]
A = [28, 55, 110, 220, 440, 880, 1760, 3520, 7040]
As = [29, 58, 117, 233, 466, 932, 1865, 3729, 7459]
B = [31, 62, 123, 247, 494, 988, 1976, 3951, 7902]

ms = 400


def thunderstruck():
    for i in range(2):
        for j in range(4):
            winsound.Beep(E[6], ms)
            winsound.Beep(Gs[6], ms)
            winsound.Beep(E[6], ms)
            winsound.Beep(B[6], ms)

        for j in range(4):
            winsound.Beep(E[6], ms)
            winsound.Beep(A[6], ms)
            winsound.Beep(E[6], ms)
            winsound.Beep(C[7], ms)

    for i in range(2):
        winsound.Beep(E[7], ms)
        winsound.Beep(E[6], ms)

        winsound.Beep(D[7], ms)
        winsound.Beep(E[6], ms)

        winsound.Beep(Cs[7], ms)
        winsound.Beep(E[6], ms)

        winsound.Beep(D[7], ms)
        winsound.Beep(E[6], ms)

        winsound.Beep(B[6], ms)
        winsound.Beep(E[6], ms)

        winsound.Beep(Cs[7], ms)
        winsound.Beep(E[6], ms)

        winsound.Beep(A[6], ms)
        winsound.Beep(E[6], ms)

        winsound.Beep(B[6], ms)
        winsound.Beep(E[6], ms)

        for j in range(4):
            winsound.Beep(Gs[6], ms)
            winsound.Beep(A[6], ms)

    # e d cs d b d a


def sub_bass():
    winsound.Beep(D[1], 2000)
    winsound.Beep(F[1], 2000)
    winsound.Beep(A[1], 2000)
    winsound.Beep(F[1], 2000)


thunderstruck()

