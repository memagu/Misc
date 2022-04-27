class Element:
    def __init__(self, label, protons, nucleons, mass, half_life, decay):
        self.label = label
        self.protons = protons
        self.nucleons = nucleons
        self.electrons = protons
        self.neutrons = nucleons - protons
        self.mass = mass
        self.mass_kg = mass * (1.6605402 * 10 ** -27)
        self.half_life = half_life
        self.decay = decay

    def __str__(self):
        return f"{self.protons} {self.label}"

    def __repr__(self):
        return str(self.__dict__)

    def __add__(self, other):
        return get_element(self.protons + other.protons, self.nucleons + other.nucleons)

    def __sub__(self, other):
        return get_element(self.protons - other.protons, self.nucleons - other.nucleons)

    @staticmethod
    def usage_help():
        print("label = label of element")
        print("protons = number of protons")
        print("nucleons = sum of protons and neutrons")
        print("nuclear_mass = mass of element")
        print("half_life = time for half of the particles to decay")
        print("decay = decay method")



# n = Element("n", 0, 1, 1.0086649158, 613.8, "β-")
#
# H1 = Element("H1", 1, 1, 1.0078250322, 0, "stable")
# H2 = Element("H2", 1, 2, 2.0141017781, 0, "stable")
# H3 = Element("H3", 1, 3, 3.0160492820, 3.90683*10**8, "β-")
#
# He1 = Element("He1", 2, 3, 3.0160293227, 0, "stable")
# He2 = Element("He2", 2, 4, 4.0026032541, 0, "stable")
# He3 = Element("He3", 2, 5, 5.012057, 7*10**-22, "n")
# He4 = Element("He4", 2, 6, 6.0188859, 0.8067, "β-")
#
# Li5 = Element("Li5", 3, 5, 5.0125540, 3.7*10**-22, "p")
# Li6 = Element("Li6", 3, 6, 6.015122887, 0, "stable")
# Li7 = Element("Li6", 3, 7, 7.01600334, 0, "stable")
# Li8 = Element("Li6", 3, 8, 8.02248625, 0.8403, "β-")
#
# Be7 = Element("Be7", 4, 7, 7.01692872, 4598208, "ε, γ")
# Be8 = Element("Be8", 4, 8, 8.00530510, 6.7*10**-17, "α")
# Be9 = Element("Be9", 4, 9, 9.0121831, 0, "stable")
# Be10 = Element("Be10", 4, 10, 10.0135347, 4.76509582*10**13, "β-")

e = Element('e', -1, 0, 0.00054858, None, 'None')
p = Element('e', 1, 1, 1.007276, None, 'None')
n = Element('e', 0, 1, 1.0086649, 613.9, 'Beta-')

H1 = Element('H1', 1, 1, 1.00782503223, 0, None)
H2 = Element('H2', 1, 2, 2.01410177812, 0, None)
H3 = Element('H3', 1, 3, 3.0160492779, 388523520.0, 'beta-')
H4 = Element('H4', 1, 4, 4.02643, None, 'n')

He3 = Element('He3', 2, 3, 3.0160293201, 0, None)
He4 = Element('He4', 2, 4, 4.00260325413, 0, None)
He5 = Element('He5', 2, 5, 5.012057, None, 'n, alpha')
He6 = Element('He6', 2, 6, 6.018885891, None, 'beta-')

Li5 = Element('Li5', 3, 5, 5.012538, None, 'P')
Li6 = Element('Li6', 3, 6, 6.0151228874, 0, None)
Li7 = Element('Li7', 3, 7, 7.0160034366, 0, None)
Li8 = Element('Li8', 3, 8, 8.022486246, 0.8399, 'beta-')

Be7 = Element('Be7', 4, 7, 7.016928717, 4598208.0, 'epsilon')
Be8 = Element('Be8', 4, 8, 8.005305102, None, 'alpha')
Be9 = Element('Be9', 4, 9, 9.012183065, 0, None)
Be10 = Element('Be10', 4, 10, 10.013534695, 47619360000000.0, 'beta-')

B8 = Element('B8', 5, 8, 8.0246073, 0.77, 'beta+')
B9 = Element('B9', 5, 9, 9.01332965, None, 'P')
B10 = Element('B10', 5, 10, 10.01293695, 0, None)
B11 = Element('B11', 5, 11, 11.00930536, 0, None)
B12 = Element('B12', 5, 12, 12.0143527, 0.0202, 'beta-')

C10 = Element('C10', 6, 10, 10.01685331, 19.308, 'beta+')
C11 = Element('C11', 6, 11, 11.0114336, 1221.8400000000001, 'beta+')
C12 = Element('C12', 6, 12, 12.0, 0, None)
C13 = Element('C13', 6, 13, 13.00335483507, 0, None)
C14 = Element('C14', 6, 14, 14.0032419884, 179755200000.0, 'beta-')
C15 = Element('C15', 6, 15, 15.01059926, 2.449, 'beta-')

N13 = Element('N13', 7, 13, 13.00573861, 597.9, 'beta+')
N14 = Element('N14', 7, 14, 14.00307400443, 0, None)
N15 = Element('N15', 7, 15, 15.00010889888, 0, None)
N16 = Element('N16', 7, 16, 16.0061019, 7.13, 'beta-')
N17 = Element('N17', 7, 17, 17.008449, 4.171, 'beta-')
N18 = Element('N18', 7, 18, 18.014078, 0.619, 'beta-')

O14 = Element('O14', 8, 14, 14.00859636, 70.62, 'beta+')
O15 = Element('O15', 8, 15, 15.00306562, 122.24, 'beta+')
O16 = Element('O16', 8, 16, 15.99491461957, 0, None)
O17 = Element('O17', 8, 17, 16.9991317565, 0, None)
O18 = Element('O18', 8, 18, 17.99915961286, 0, None)
O19 = Element('O19', 8, 19, 19.003578, 26.88, 'beta-')

F17 = Element('F17', 9, 17, 17.00209524, 64.49, 'beta+')
F18 = Element('F18', 9, 18, 18.00093733, 6586.2, 'beta+')
F19 = Element('F19', 9, 19, 18.99840316273, 0, None)
F20 = Element('F20', 9, 20, 19.999981252, 11.07, 'beta-')

Ne19 = Element('Ne19', 10, 19, 19.00188091, 17.22, 'beta+')
Ne20 = Element('Ne20', 10, 20, 19.9924401762, 0, None)
Ne21 = Element('Ne21', 10, 21, 20.993846685, 0, None)
Ne22 = Element('Ne22', 10, 22, 21.991385114, 0, None)
Ne23 = Element('Ne23', 10, 23, 22.99446691, 37.24, 'beta-')
Ne24 = Element('Ne24', 10, 24, 23.99361065, 202.79999999999998, 'beta-')

Na21 = Element('Na21', 11, 21, 20.99765469, 22.49, 'beta+')
Na22 = Element('Na22', 11, 22, 21.99443741, 82050364.8, 'beta+')
Na23 = Element('Na23', 11, 23, 22.989769282, 0, None)
Na24 = Element('Na24', 11, 24, 23.99096295, 53989.2, 'beta-')
Na25 = Element('Na25', 11, 25, 24.989954, 59.1, 'beta-')

Mg22 = Element('Mg22', 12, 22, 21.99957065, 3.8755, 'beta+')
Mg23 = Element('Mg23', 12, 23, 22.99412421, 11.317, 'beta+')
Mg24 = Element('Mg24', 12, 24, 23.985041697, 0, None)
Mg25 = Element('Mg25', 12, 25, 24.985836976, 0, None)
Mg26 = Element('Mg26', 12, 26, 25.982592968, 0, None)
Mg27 = Element('Mg27', 12, 27, 26.984340624, 567.48, 'beta-')

Al25 = Element('Al25', 13, 25, 24.9904281, 7.183, 'beta+')
Al26 = Element('Al26', 13, 26, 25.986891904, 22611312000000.0, 'beta+')
Al27 = Element('Al27', 13, 27, 26.98153853, 0, None)
Al28 = Element('Al28', 13, 28, 27.98191021, 134.70000000000002, 'beta-')

Si26 = Element('Si26', 14, 26, 25.99233384, 2.2453, 'beta+')
Si27 = Element('Si27', 14, 27, 26.98670481, 4.15, 'beta+')
Si28 = Element('Si28', 14, 28, 27.97692653465, 0, None)
Si29 = Element('Si29', 14, 29, 28.9764946649, 0, None)
Si30 = Element('Si30', 14, 30, 29.973770136, 0, None)
Si31 = Element('Si31', 14, 31, 30.975363194, 9441.6, 'beta-')

P30 = Element('P30', 15, 30, 29.97831375, 149.88000000000002, 'beta+')
P31 = Element('P31', 15, 31, 30.97376199842, 0, None)
P32 = Element('P32', 15, 32, 31.973907643, 1232755.2, 'beta-')
P33 = Element('P33', 15, 33, 32.9717257, 2190240.0, 'beta-')
P34 = Element('P34', 15, 34, 33.97364589, 12.43, 'beta-')

S31 = Element('S31', 16, 31, 30.97955701, 2.5534, 'beta+')
S32 = Element('S32', 16, 32, 31.9720711744, 0, None)
S33 = Element('S33', 16, 33, 32.9714589098, 0, None)
S34 = Element('S34', 16, 34, 33.967867004, 0, None)
S35 = Element('S35', 16, 35, 34.96903231, 7548768.0, 'beta-')
S36 = Element('S36', 16, 36, 35.96708071, 0, None)

Cl35 = Element('Cl35', 17, 35, 34.968852682, 0, None)
Cl36 = Element('Cl36', 17, 36, 35.968306809, 9492336000000.0, 'beta-, beta+')
Cl37 = Element('Cl37', 17, 37, 36.965902602, 0, None)
Cl38 = Element('Cl38', 17, 38, 37.96801044, 2234.4, 'beta-')

Ar35 = Element('Ar35', 18, 35, 34.97525759, 1.7756, 'beta+')
Ar36 = Element('Ar36', 18, 36, 35.967545105, 0, None)
Ar37 = Element('Ar37', 18, 37, 36.96677633, 3027456.0, 'epsilon')
Ar38 = Element('Ar38', 18, 38, 37.96273211, 0, None)
Ar39 = Element('Ar39', 18, 39, 38.964313, 8483184000.0, 'beta-')
Ar40 = Element('Ar40', 18, 40, 39.9623831237, 0, None)

K38 = Element('K38', 19, 38, 37.96908112, 458.16, 'beta+')
K39 = Element('K39', 19, 39, 38.9637064864, 0, None)
K40 = Element('K40', 19, 40, 39.963998166, 3.9356928e+16, 'beta-')
K41 = Element('K41', 19, 41, 40.9618252579, 0, None)
K42 = Element('K42', 19, 42, 41.96240231, 44478.0, 'beta-')
K43 = Element('K43', 19, 43, 42.9607347, 80280.0, 'beta-')

Ca39 = Element('Ca39', 20, 39, 38.97071081, 0.8596, 'beta+')
Ca40 = Element('Ca40', 20, 40, 39.962590863, 9.4608e+28, '2 beta+')
Ca41 = Element('Ca41', 20, 41, 40.96227792, 3134678400000.0, 'epsilon')
Ca42 = Element('Ca42', 20, 42, 41.95861783, 0, None)
Ca43 = Element('Ca43', 20, 43, 42.95876644, 0, None)
Ca44 = Element('Ca44', 20, 44, 43.95548156, 0, None)
Ca45 = Element('Ca45', 20, 45, 44.95618635, 14049504.000000002, 'beta-')
Ca46 = Element('Ca46', 20, 46, 45.953689, 8.83008e+22, '2beta-')
Ca47 = Element('Ca47', 20, 47, 46.9545424, 391910.39999999997, 'beta-')
Ca48 = Element('Ca48', 20, 48, 47.95252276, 1.8290879999999998e+30, '2beta-')
Ca49 = Element('Ca49', 20, 49, 48.95566274, 523.08, 'beta-')
Ca50 = Element('Ca50', 20, 50, 49.9574992, 13.9, 'beta-')

Sc44 = Element('Sc44', 21, 44, 43.9594029, 14292.0, 'beta+')
Sc45 = Element('Sc45', 21, 45, 44.95590828, 0, None)
Sc46 = Element('Sc46', 21, 46, 45.95516826, 7239456.000000001, 'beta-')
Sc47 = Element('Sc47', 21, 47, 46.9524037, 289370.88, 'beta-')

Ti44 = Element('Ti44', 22, 44, 43.95968995, 1892160000.0, 'epsilon')
Ti45 = Element('Ti45', 22, 45, 44.95812198, 11088.0, 'beta+')
Ti46 = Element('Ti46', 22, 46, 45.95262772, 0, None)
Ti47 = Element('Ti47', 22, 47, 46.95175879, 0, None)
Ti48 = Element('Ti48', 22, 48, 47.94794198, 0, None)
Ti49 = Element('Ti49', 22, 49, 48.94786568, 0, None)
Ti50 = Element('Ti50', 22, 50, 49.94478689, 0, None)
Ti51 = Element('Ti51', 22, 51, 50.94661065, 345.59999999999997, 'beta-')

V48 = Element('V48', 23, 48, 47.9522522, 1380110.4, 'beta+')
V49 = Element('V49', 23, 49, 48.9485118, 28512000.0, 'epsilon')
V50 = Element('V50', 23, 50, 49.94715601, 6.62256e+24, 'beta+ , beta-')
V51 = Element('V51', 23, 51, 50.94395704, 0, None)
V52 = Element('V52', 23, 52, 51.94477301, 224.57999999999998, 'beta-')

Cr49 = Element('Cr49', 24, 49, 48.9513333, 2538.0, 'beta+')
Cr50 = Element('Cr50', 24, 50, 49.94604183, 4.09968e+25, '2beta+')
Cr51 = Element('Cr51', 24, 51, 50.94476502, 2393496.0, 'epsilon')
Cr52 = Element('Cr52', 24, 52, 51.94050623, 0, None)
Cr53 = Element('Cr53', 24, 53, 52.94064815, 0, None)
Cr54 = Element('Cr54', 24, 54, 53.93887916, 0, None)
Cr55 = Element('Cr55', 24, 55, 54.94083843, 209.82, 'beta-')
Cr56 = Element('Cr56', 24, 56, 55.9406531, 356.40000000000003, 'beta-')

Mn52 = Element('Mn52', 25, 52, 51.9455639, 483062.4, 'beta+')
Mn53 = Element('Mn53', 25, 53, 52.94128889, 117944640000000.0, 'epsilon')
Mn54 = Element('Mn54', 25, 54, 53.9403576, 26974080.0, 'epsilon')
Mn55 = Element('Mn55', 25, 55, 54.93804391, 0, None)
Mn56 = Element('Mn56', 25, 56, 55.93890369, 9284.039999999999, 'beta-')

Fe53 = Element('Fe53', 26, 53, 52.9453064, 510.59999999999997, 'beta+')
Fe54 = Element('Fe54', 26, 54, 53.93960899, 0, None)
Fe55 = Element('Fe55', 26, 55, 54.93829199, 86534784.0, 'epsilon')
Fe56 = Element('Fe56', 26, 56, 55.93493633, 0, None)
Fe57 = Element('Fe57', 26, 57, 56.93539284, 0, None)
Fe58 = Element('Fe58', 26, 58, 57.93327443, 0, None)
Fe59 = Element('Fe59', 26, 59, 58.93487434, 3844368.0, 'beta-')
Fe60 = Element('Fe60', 26, 60, 59.9340711, 82624320000000.0, 'beta-')

Co56 = Element('Co56', 27, 56, 55.9398388, 6673190.4, 'beta+')
Co57 = Element('Co57', 27, 57, 56.93629057, 23478336.0, 'epsilon')
Co58 = Element('Co58', 27, 58, 57.9357521, 6122304.0, 'beta+')
Co59 = Element('Co59', 27, 59, 58.93319429, 0, None)
Co60 = Element('Co60', 27, 60, 59.9338163, 166344192.0, 'beta-')

Ni57 = Element('Ni57', 28, 57, 56.93979218, 128160.0, 'beta+')
Ni58 = Element('Ni58', 28, 58, 57.93534241, 0, None)
Ni59 = Element('Ni59', 28, 59, 58.9343462, 2396736000000.0, 'beta+')
Ni60 = Element('Ni60', 28, 60, 59.93078588, 0, None)
Ni61 = Element('Ni61', 28, 61, 60.93105557, 0, None)
Ni62 = Element('Ni62', 28, 62, 61.92834537, 0, None)
Ni63 = Element('Ni63', 28, 63, 62.92966963, 3191443200.0, 'beta-')
Ni64 = Element('Ni64', 28, 64, 63.92796682, 0, None)
Ni65 = Element('Ni65', 28, 65, 64.93008517, 9063.0, 'beta-')

Cu62 = Element('Cu62', 29, 62, 61.93259541, 580.38, 'beta+')
Cu63 = Element('Cu63', 29, 63, 62.92959772, 0, None)
Cu64 = Element('Cu64', 29, 64, 63.92976434, 45723.6, 'beta+ , beta-')
Cu65 = Element('Cu65', 29, 65, 64.9277897, 0, None)
Cu66 = Element('Cu66', 29, 66, 65.92886903, 307.2, 'beta-')

Zn63 = Element('Zn63', 30, 63, 62.9332115, 2308.2, 'beta+')
Zn64 = Element('Zn64', 30, 64, 63.92914201, 2.20752e+28, '2beta+')
Zn65 = Element('Zn65', 30, 65, 64.92924077, 21075552.0, 'beta+')
Zn66 = Element('Zn66', 30, 66, 65.92603381, 0, None)
Zn67 = Element('Zn67', 30, 67, 66.92712775, 0, None)
Zn68 = Element('Zn68', 30, 68, 67.92484455, 0, None)
Zn69 = Element('Zn69', 30, 69, 68.9265507, 3384.0, 'beta-')
Zn70 = Element('Zn70', 30, 70, 69.9253192, 7.25328e+24, '2beta-')
Zn71 = Element('Zn71', 30, 71, 70.9277196, 147.0, 'beta-')

Ga68 = Element('Ga68', 31, 68, 67.9279805, 4062.5999999999995, 'beta+')
Ga69 = Element('Ga69', 31, 69, 68.9255735, 0, None)
Ga70 = Element('Ga70', 31, 70, 69.9260219, 1268.4, 'beta-')
Ga71 = Element('Ga71', 31, 71, 70.92470258, 0, None)
Ga72 = Element('Ga72', 31, 72, 71.92636747, 50760.0, 'beta-')

Ge69 = Element('Ge69', 32, 69, 68.9279645, 140580.0, 'beta+')
Ge70 = Element('Ge70', 32, 70, 69.92424875, 0, None)
Ge71 = Element('Ge71', 32, 71, 70.92495233, 987552.0, 'epsilon')
Ge72 = Element('Ge72', 32, 72, 71.922075826, 0, None)
Ge73 = Element('Ge73', 32, 73, 72.923458956, 0, None)
Ge74 = Element('Ge74', 32, 74, 73.921177761, 0, None)
Ge75 = Element('Ge75', 32, 75, 74.92285837, 4966.8, 'beta-')
Ge76 = Element('Ge76', 32, 76, 75.921402726, 0, None)
Ge77 = Element('Ge77', 32, 77, 76.923549843, 40680.0, 'beta-')

As73 = Element('As73', 33, 73, 72.9238291, 6937920.0, 'epsilon')
As74 = Element('As74', 33, 74, 73.9239286, 1535328.0, 'beta+ , beta-')
As75 = Element('As75', 33, 75, 74.92159457, 0, None)
As76 = Element('As76', 33, 76, 75.92239202, 94538.88, 'beta-')

Se73 = Element('Se73', 34, 73, 72.9267549, 25740.0, 'beta+')
Se74 = Element('Se74', 34, 74, 73.922475934, 0, None)
Se75 = Element('Se75', 34, 75, 74.92252287, 10348992.0, 'epsilon')
Se76 = Element('Se76', 34, 76, 75.919213704, 0, None)
Se77 = Element('Se77', 34, 77, 76.919914154, 0, None)
Se78 = Element('Se78', 34, 78, 77.91730928, 0, None)
Se79 = Element('Se79', 34, 79, 78.91849929, 10280736000000.0, 'beta-')
Se80 = Element('Se80', 34, 80, 79.9165218, 0, '2beta-')
Se81 = Element('Se81', 34, 81, 80.917993, 1107.0, 'beta-')
Se82 = Element('Se82', 34, 82, 81.9166995, 0, None)
Se83 = Element('Se83', 34, 83, 82.9191186, 70.1, 'beta-')

Br78 = Element('Br78', 35, 78, 77.9211459, 387.0, 'beta+ , beta-')
Br79 = Element('Br79', 35, 79, 78.9183376, 0, None)
Br80 = Element('Br80', 35, 80, 79.9185298, 1060.8, 'beta-, beta+')
Br81 = Element('Br81', 35, 81, 80.9162897, 0, None)
Br82 = Element('Br82', 35, 82, 81.9168032, 127015.19999999998, 'beta-')

Kr78 = Element('Kr78', 36, 78, 77.92036494, 4.7304e+28, '2beta+')
Kr79 = Element('Kr79', 36, 79, 78.9200829, 126144.0, 'beta+')
Kr80 = Element('Kr80', 36, 80, 79.91637808, 0, None)
Kr81 = Element('Kr81', 36, 81, 80.9165912, 7221744000000.0, 'epsilon')
Kr82 = Element('Kr82', 36, 82, 81.91348273, 0, None)
Kr83 = Element('Kr83', 36, 83, 82.91412716, 0, None)
Kr84 = Element('Kr84', 36, 84, 83.9114977282, 0, None)
Kr85 = Element('Kr85', 36, 85, 84.9125273, 338665104.0, 'beta-')
Kr86 = Element('Kr86', 36, 86, 85.9106106269, 0, None)
Kr87 = Element('Kr87', 36, 87, 86.91335476, 4578.0, 'beta-')
Kr88 = Element('Kr88', 36, 88, 87.9144479, 10170.0, 'beta-')
Kr89 = Element('Kr89', 36, 89, 88.9178355, 189.0, 'beta-')
Kr90 = Element('Kr90', 36, 90, 89.9195279, 32.32, 'beta-')
Kr91 = Element('Kr91', 36, 91, 90.9238063, 8.57, 'beta-')
Kr92 = Element('Kr92', 36, 92, 91.9261731, 1.84, 'beta-')

Rb84 = Element('Rb84', 37, 84, 83.9143752, 2835648.0, 'beta+ , beta-')
Rb85 = Element('Rb85', 37, 85, 84.9117897379, 0, None)
Rb86 = Element('Rb86', 37, 86, 85.91116743, 1610668.8, 'beta-, epsilon')
Rb87 = Element('Rb87', 37, 87, 86.909180531, 1.5673392e+18, 'beta-')

Sr84 = Element('Sr84', 38, 84, 83.9134191, 0, None)
Sr85 = Element('Sr85', 38, 85, 84.912932, 5602953.600000001, 'epsilon')
Sr86 = Element('Sr86', 38, 86, 85.9092606, 0, None)
Sr87 = Element('Sr87', 38, 87, 86.9088775, 0, None)
Sr88 = Element('Sr88', 38, 88, 87.9056125, 0, None)
Sr89 = Element('Sr89', 38, 89, 88.9074511, 4368643.2, 'beta-')
Sr90 = Element('Sr90', 38, 90, 89.90773, 911390400.0, 'beta-')
Sr91 = Element('Sr91', 38, 91, 90.9101954, 34740.0, 'beta-')
Sr92 = Element('Sr92', 38, 92, 91.9110382, 9576.0, 'beta-')
Sr93 = Element('Sr93', 38, 93, 92.9140242, 445.79999999999995, 'beta-')
Sr94 = Element('Sr94', 38, 94, 93.9153556, 75.3, 'beta-')

Y88 = Element('Y88', 39, 88, 87.9095016, 9212486.4, 'beta+')
Y89 = Element('Y89', 39, 89, 88.9058403, 0, None)
Y90 = Element('Y90', 39, 90, 89.9071439, 230590.8, 'beta-')
Y91 = Element('Y91', 39, 91, 90.9072974, 5055264.0, 'beta-')
Y92 = Element('Y92', 39, 92, 91.9089451, 12744.0, 'beta-')
Y93 = Element('Y93', 39, 93, 92.909578, 36648.0, 'beta-')
Y94 = Element('Y94', 39, 94, 93.9115906, 1122.0, 'beta-')
Y95 = Element('Y95', 39, 95, 94.9128161, 618.0, 'beta-')

Zr89 = Element('Zr89', 40, 89, 88.9088814, 282276.0, 'beta+')
Zr90 = Element('Zr90', 40, 90, 89.9046977, 0, None)
Zr91 = Element('Zr91', 40, 91, 90.9056396, 0, None)
Zr92 = Element('Zr92', 40, 92, 91.9050347, 0, None)
Zr93 = Element('Zr93', 40, 93, 92.9064699, 50772960000000.0, 'beta-')
Zr94 = Element('Zr94', 40, 94, 93.9063108, 0, None)
Zr95 = Element('Zr95', 40, 95, 94.9080385, 5532364.8, 'beta-')
Zr96 = Element('Zr96', 40, 96, 95.9082714, 7.41096e+26, '2beta-')

Nb90 = Element('Nb90', 41, 90, 89.9112584, 52560.0, 'beta+')
Nb91 = Element('Nb91', 41, 91, 90.9069897, 21444480000.0, 'epsilon')
Nb92 = Element('Nb92', 41, 92, 91.9071881, 1094299200000000.0, 'beta+ , beta-')
Nb93 = Element('Nb93', 41, 93, 92.906373, 0, None)
Nb94 = Element('Nb94', 41, 94, 93.9072788, 640180800000.0, 'beta-')

Mo92 = Element('Mo92', 42, 92, 91.90680796, 0, None)
Mo93 = Element('Mo93', 42, 93, 92.90680958, 126144000000.0, 'epsilon')
Mo94 = Element('Mo94', 42, 94, 93.9050849, 0, None)
Mo95 = Element('Mo95', 42, 95, 94.90583877, 0, None)
Mo96 = Element('Mo96', 42, 96, 95.90467612, 0, None)
Mo97 = Element('Mo97', 42, 97, 96.90601812, 0, None)
Mo98 = Element('Mo98', 42, 98, 97.90540482, 0, None)
Mo99 = Element('Mo99', 42, 99, 98.90770851, 237513.6, 'beta-')
Mo100 = Element('Mo100', 42, 100, 99.9074718, 2.302128e+26, '2beta-')

Tc96 = Element('Tc96', 43, 96, 95.907868, 369792.0, 'beta+')
Tc97 = Element('Tc97', 43, 97, 96.9063667, 132766560000000.0, 'epsilon')
Tc98 = Element('Tc98', 43, 98, 97.9072124, 132451200000000.0, 'beta-')
Tc99 = Element('Tc99', 43, 99, 98.9062508, 6657249600000.0, 'beta-')
Tc100 = Element('Tc100', 43, 100, 99.9076539, 15.46, 'beta-, epsilon')

Ru95 = Element('Ru95', 44, 95, 94.910406, 5914.8, 'beta+')
Ru96 = Element('Ru96', 44, 96, 95.90759025, 0, None)
Ru97 = Element('Ru97', 44, 97, 96.9075471, 244512.0, 'beta+')
Ru98 = Element('Ru98', 44, 98, 97.9052868, 0, None)
Ru99 = Element('Ru99', 44, 99, 98.9059341, 0, None)
Ru100 = Element('Ru100', 44, 100, 99.9042143, 0, None)
Ru101 = Element('Ru101', 44, 101, 100.9055769, 0, None)
Ru102 = Element('Ru102', 44, 102, 101.9043441, 0, None)
Ru103 = Element('Ru103', 44, 103, 102.9063186, 3390940.8, 'beta-')
Ru104 = Element('Ru104', 44, 104, 103.9054275, 0, None)
Ru105 = Element('Ru105', 44, 105, 104.9077476, 15984.000000000002, 'beta-')
Ru106 = Element('Ru106', 44, 106, 105.9073291, 32123520.0, 'beta-')

Rh101 = Element('Rh101', 45, 101, 100.9061606, 104068800.0, 'epsilon')
Rh102 = Element('Rh102', 45, 102, 101.9068374, 17910720.0, 'beta+ , beta-')
Rh103 = Element('Rh103', 45, 103, 102.905498, 0, None)
Rh104 = Element('Rh104', 45, 104, 103.9066492, 42.3, 'beta-, beta+')

Pd100 = Element('Pd100', 46, 100, 99.908505, 313632.0, 'epsilon')
Pd101 = Element('Pd101', 46, 101, 100.9082864, 30492.000000000004, 'beta+')
Pd102 = Element('Pd102', 46, 102, 101.9056022, 0, None)
Pd103 = Element('Pd103', 46, 103, 102.9060809, 1468022.4, 'epsilon')
Pd104 = Element('Pd104', 46, 104, 103.9040305, 0, None)
Pd105 = Element('Pd105', 46, 105, 104.9050796, 0, None)
Pd106 = Element('Pd106', 46, 106, 105.9034804, 0, None)
Pd107 = Element('Pd107', 46, 107, 106.9051282, 204984000000000.0, 'beta-')
Pd108 = Element('Pd108', 46, 108, 107.9038916, 0, None)
Pd109 = Element('Pd109', 46, 109, 108.9059504, 49324.32, 'beta-')
Pd110 = Element('Pd110', 46, 110, 109.9051722, 0, None)

Ag105 = Element('Ag105', 47, 105, 104.9065256, 3567456.0, 'beta+')
Ag106 = Element('Ag106', 47, 106, 105.9066636, 1437.6000000000001, 'beta+ , beta-')
Ag107 = Element('Ag107', 47, 107, 106.9050916, 0, None)
Ag108 = Element('Ag108', 47, 108, 107.9059503, 142.92000000000002, 'beta-, beta+')
Ag109 = Element('Ag109', 47, 109, 108.9047553, 0, None)
Ag110 = Element('Ag110', 47, 110, 109.9061102, 24.6, 'beta-, epsilon')

Cd105 = Element('Cd105', 48, 105, 104.9094639, 3330.0, 'beta+')
Cd106 = Element('Cd106', 48, 106, 105.9064599, 1.135296e+28, '2beta+')
Cd107 = Element('Cd107', 48, 107, 106.9066121, 23400.0, 'beta+')
Cd108 = Element('Cd108', 48, 108, 107.9041834, 5.99184e+25, '2beta+')
Cd109 = Element('Cd109', 48, 109, 108.9049867, 39864960.0, 'epsilon')
Cd110 = Element('Cd110', 48, 110, 109.90300661, 0, None)
Cd111 = Element('Cd111', 48, 111, 110.90418287, 0, None)
Cd112 = Element('Cd112', 48, 112, 111.90276287, 0, None)
Cd113 = Element('Cd113', 48, 113, 112.90440813, 2.52288e+23, 'beta-')
Cd114 = Element('Cd114', 48, 114, 113.90336509, 6.62256e+25, '2beta-')
Cd115 = Element('Cd115', 48, 115, 114.90543751, 192456.0, 'beta-')
Cd116 = Element('Cd116', 48, 116, 115.90476315, 1.040688e+27, '2beta-')

In112 = Element('In112', 49, 112, 111.9055377, 892.8000000000001, 'beta+ , beta-')
In113 = Element('In113', 49, 113, 112.90406184, 0, None)
In114 = Element('In114', 49, 114, 113.90491791, 71.9, 'beta-, beta+')
In115 = Element('In115', 49, 115, 114.903878776, 1.3907376e+22, 'beta-')

Sn112 = Element('Sn112', 50, 112, 111.90482387, 4.09968e+28, '2beta+')
Sn113 = Element('Sn113', 50, 113, 112.9051757, 9943776.0, 'beta+')
Sn114 = Element('Sn114', 50, 114, 113.9027827, 0, None)
Sn115 = Element('Sn115', 50, 115, 114.903344699, 0, None)
Sn116 = Element('Sn116', 50, 116, 115.9017428, 0, None)
Sn117 = Element('Sn117', 50, 117, 116.90295398, 0, None)
Sn118 = Element('Sn118', 50, 118, 117.90160657, 0, None)
Sn119 = Element('Sn119', 50, 119, 118.90331117, 0, None)
Sn120 = Element('Sn120', 50, 120, 119.90220163, 0, None)
Sn121 = Element('Sn121', 50, 121, 120.9042426, 97308.0, 'beta-')
Sn122 = Element('Sn122', 50, 122, 121.9034438, 0, None)
Sn123 = Element('Sn123', 50, 123, 122.9057252, 11162879.999999998, 'beta-')
Sn124 = Element('Sn124', 50, 124, 123.9052766, 3.78432e+28, '2beta-')

Sb120 = Element('Sb120', 51, 120, 119.9050794, 953.4000000000001, 'beta+')
Sb121 = Element('Sb121', 51, 121, 120.903812, 0, None)
Sb122 = Element('Sb122', 51, 122, 121.9051699, 235336.32, 'beta-, beta+')
Sb123 = Element('Sb123', 51, 123, 122.9042132, 0, None)
Sb124 = Element('Sb124', 51, 124, 123.905935, 5201280.0, 'beta-')
Sb125 = Element('Sb125', 51, 125, 124.905253, 86993948.16000001, 'beta-')

Te120 = Element('Te120', 52, 120, 119.9040593, 0, None)
Te121 = Element('Te121', 52, 121, 120.904944, 1656288.0000000002, 'beta+')
Te122 = Element('Te122', 52, 122, 121.9030435, 0, None)
Te123 = Element('Te123', 52, 123, 122.9042698, 2.901312e+24, 'epsilon')
Te124 = Element('Te124', 52, 124, 123.9028171, 0, None)
Te125 = Element('Te125', 52, 125, 124.9044299, 0, None)
Te126 = Element('Te126', 52, 126, 125.9033109, 0, None)
Te127 = Element('Te127', 52, 127, 126.9052257, 33660.0, 'beta-')
Te128 = Element('Te128', 52, 128, 127.90446128, 7.600176e+31, '2beta-')
Te129 = Element('Te129', 52, 129, 128.90659646, 4194.0, 'beta-')
Te130 = Element('Te130', 52, 130, 129.906222748, 9.4608e+31, '2beta-')

I125 = Element('I125', 53, 125, 124.9046294, 5132764.8, 'epsilon')
I126 = Element('I126', 53, 126, 125.9056233, 1117152.0, 'beta+ , beta-')
I127 = Element('I127', 53, 127, 126.9044719, 0, None)
I128 = Element('I128', 53, 128, 127.9058086, 1499.3999999999999, 'beta-, beta+')
I129 = Element('I129', 53, 129, 128.9049837, 495115200000000.0, 'beta-')
I130 = Element('I130', 53, 130, 129.9066702, 44496.0, 'beta-')
I131 = Element('I131', 53, 131, 130.9061263, 693377.28, 'beta-')
I132 = Element('I132', 53, 132, 131.9079935, 8262.0, 'beta-')
I133 = Element('I133', 53, 133, 132.907797, 74988.0, 'beta-')
I134 = Element('I134', 53, 134, 133.9097588, 3150.0, 'beta-')
I135 = Element('I135', 53, 135, 134.9100488, 23688.0, 'beta-')
I136 = Element('I136', 53, 136, 135.914604, 83.4, 'beta-')

Xe124 = Element('Xe124', 54, 124, 123.905892, 5.04576e+21, '2beta+')
Xe125 = Element('Xe125', 54, 125, 124.9063944, 60839.99999999999, 'beta+')
Xe126 = Element('Xe126', 54, 126, 125.9042983, 0, None)
Xe127 = Element('Xe127', 54, 127, 126.9051829, 3140294.4, 'epsilon')
Xe128 = Element('Xe128', 54, 128, 127.903531, 0, None)
Xe129 = Element('Xe129', 54, 129, 128.9047808611, 0, None)
Xe130 = Element('Xe130', 54, 130, 129.903509349, 0, None)
Xe131 = Element('Xe131', 54, 131, 130.90508406, 0, None)
Xe132 = Element('Xe132', 54, 132, 131.9041550856, 0, None)
Xe133 = Element('Xe133', 54, 133, 132.9059108, 453383.99999999994, 'beta-')
Xe134 = Element('Xe134', 54, 134, 133.90539466, 1.8290879999999998e+30, '2beta-')
Xe135 = Element('Xe135', 54, 135, 134.9072278, 32904.0, 'beta-')
Xe136 = Element('Xe136', 54, 136, 135.907214484, 7.56864e+28, '2beta-')

Cs132 = Element('Cs132', 55, 132, 131.9064339, 559872.0, 'beta+ , beta-')
Cs133 = Element('Cs133', 55, 133, 132.905451961, 0, None)
Cs134 = Element('Cs134', 55, 134, 133.906718503, 65128147.199999996, 'beta-, epsilon')
Cs135 = Element('Cs135', 55, 135, 134.905977, 72532800000000.0, 'beta-')
Cs136 = Element('Cs136', 55, 136, 135.9073114, 1126656.0, 'beta-')
Cs137 = Element('Cs137', 55, 137, 136.90708923, 948602880.0, 'beta-')

Ba130 = Element('Ba130', 56, 130, 129.9063207, 0, '2beta+')
Ba131 = Element('Ba131', 56, 131, 130.906941, 993600.0, 'beta+')
Ba132 = Element('Ba132', 56, 132, 131.9050611, 9.4608e+28, '2beta+')
Ba133 = Element('Ba133', 56, 133, 132.9060074, 332736336.0, 'epsilon')
Ba134 = Element('Ba134', 56, 134, 133.90450818, 0, None)
Ba135 = Element('Ba135', 56, 135, 134.90568838, 0, None)
Ba136 = Element('Ba136', 56, 136, 135.90457573, 0, None)
Ba137 = Element('Ba137', 56, 137, 136.90582714, 0, None)
Ba138 = Element('Ba138', 56, 138, 137.905247, 0, None)
Ba139 = Element('Ba139', 56, 139, 138.9088411, 4983.6, 'beta-')
Ba140 = Element('Ba140', 56, 140, 139.9106057, 1101833.28, 'beta-')
Ba141 = Element('Ba141', 56, 141, 140.9144033, 1096.2, 'beta-')
Ba142 = Element('Ba142', 56, 142, 141.9164324, 636.0, 'beta-')
Ba143 = Element('Ba143', 56, 143, 142.9206253, 14.5, 'beta-')

La137 = Element('La137', 57, 137, 136.9064504, 1892160000000.0, 'epsilon')
La138 = Element('La138', 57, 138, 137.9071149, 3.216672e+18, 'beta+ , beta-')
La139 = Element('La139', 57, 139, 138.9063563, 0, None)
La140 = Element('La140', 57, 140, 139.9094806, 145026.72, 'beta-')

Ce136 = Element('Ce136', 58, 136, 135.90712921, 2.20752e+21, '2beta+')
Ce137 = Element('Ce137', 58, 137, 136.90776236, 32400.0, 'beta+')
Ce138 = Element('Ce138', 58, 138, 137.905991, 2.83824e+21, '2beta+')
Ce139 = Element('Ce139', 58, 139, 138.9066551, 11892182.399999999, 'epsilon')
Ce140 = Element('Ce140', 58, 140, 139.9054431, 0, None)
Ce141 = Element('Ce141', 58, 141, 140.9082807, 2808950.4000000004, 'beta-')
Ce142 = Element('Ce142', 58, 142, 141.9092504, 1.5768e+24, '2beta-')
Ce143 = Element('Ce143', 58, 143, 142.9123921, 118940.40000000001, 'beta-')

Pr140 = Element('Pr140', 59, 140, 139.9090803, 203.4, 'beta+')
Pr141 = Element('Pr141', 59, 141, 140.9076576, 0, None)
Pr142 = Element('Pr142', 59, 142, 141.9100496, 68832.0, 'beta-, epsilon')

Nd142 = Element('Nd142', 60, 142, 141.907729, 0, None)
Nd143 = Element('Nd143', 60, 143, 142.90982, 0, None)
Nd144 = Element('Nd144', 60, 144, 143.910093, 7.221744e+22, 'alpha')
Nd145 = Element('Nd145', 60, 145, 144.9125793, 0, None)
Nd146 = Element('Nd146', 60, 146, 145.9131226, 0, None)
Nd147 = Element('Nd147', 60, 147, 146.9161061, 948672.0, 'beta-')
Nd148 = Element('Nd148', 60, 148, 147.9168993, 0, None)
Nd149 = Element('Nd149', 60, 149, 148.9201548, 6220.8, 'beta-')
Nd150 = Element('Nd150', 60, 150, 149.9209022, 2.869776e+26, '2beta-')

Pm154 = Element('Pm154', 61, 154, 153.926472, 160.8, 'beta-')
Pm155 = Element('Pm155', 61, 155, 154.928137, 41.5, 'beta-')

Sm144 = Element('Sm144', 62, 144, 143.9120065, 0, None)
Sm145 = Element('Sm145', 62, 145, 144.9134173, 29376000.0, 'epsilon')
Sm146 = Element('Sm146', 62, 146, 145.913047, 3248208000000000.0, 'alpha')
Sm147 = Element('Sm147', 62, 147, 146.9149044, 3.342816e+18, 'alpha')
Sm148 = Element('Sm148', 62, 148, 147.9148292, 2.20752e+23, 'alpha')
Sm149 = Element('Sm149', 62, 149, 148.9171921, 0, None)
Sm150 = Element('Sm150', 62, 150, 149.9172829, 0, None)
Sm151 = Element('Sm151', 62, 151, 150.9199398, 2838240000.0, 'beta-')
Sm152 = Element('Sm152', 62, 152, 151.9197397, 0, None)
Sm153 = Element('Sm153', 62, 153, 152.9221047, 166622.4, 'beta-')
Sm154 = Element('Sm154', 62, 154, 153.9222169, 0, None)

Eu150 = Element('Eu150', 63, 150, 149.9197077, 1163678400.0, 'beta+')
Eu151 = Element('Eu151', 63, 151, 150.9198578, 5.36112e+25, 'alpha')
Eu152 = Element('Eu152', 63, 152, 151.9217522, 426272112.0, 'beta+ , beta-')
Eu153 = Element('Eu153', 63, 153, 152.921238, 0, None)
Eu154 = Element('Eu154', 63, 154, 153.922987, 271241136.0, 'beta-, epsilon')

Gd152 = Element('Gd152', 64, 152, 151.9197995, 3.405888e+21, 'alpha')
Gd153 = Element('Gd153', 64, 153, 152.921758, 20770560.0, 'epsilon')
Gd154 = Element('Gd154', 64, 154, 153.9208741, 0, None)
Gd155 = Element('Gd155', 64, 155, 154.9226305, 0, None)
Gd156 = Element('Gd156', 64, 156, 155.9221312, 0, None)
Gd157 = Element('Gd157', 64, 157, 156.9239686, 0, None)
Gd158 = Element('Gd158', 64, 158, 157.9241123, 0, None)
Gd159 = Element('Gd159', 64, 159, 158.926397, 66524.4, 'beta-')
Gd160 = Element('Gd160', 64, 160, 159.9270624, 9.77616e+26, '2beta-')

Tb158 = Element('Tb158', 65, 158, 157.9254209, 5676480000.0, 'beta+ , beta-')
Tb159 = Element('Tb159', 65, 159, 158.9253547, 0, None)
Tb160 = Element('Tb160', 65, 160, 159.9271756, 6246720.0, 'beta-')

Dy156 = Element('Dy156', 66, 156, 155.9242847, 0, None)
Dy157 = Element('Dy157', 66, 157, 156.9254707, 29304.000000000004, 'beta+')
Dy158 = Element('Dy158', 66, 158, 157.9244159, 0, None)
Dy159 = Element('Dy159', 66, 159, 158.925747, 12476160.0, 'epsilon')
Dy160 = Element('Dy160', 66, 160, 159.9252046, 0, None)
Dy161 = Element('Dy161', 66, 161, 160.9269405, 0, None)
Dy162 = Element('Dy162', 66, 162, 161.9268056, 0, None)
Dy163 = Element('Dy163', 66, 163, 162.9287383, 0, None)
Dy164 = Element('Dy164', 66, 164, 163.9291819, 0, None)
Dy165 = Element('Dy165', 66, 165, 164.9317105, 8402.4, 'beta-')

Ho164 = Element('Ho164', 67, 164, 163.9302403, 1740.0, 'epsilon, beta-')
Ho165 = Element('Ho165', 67, 165, 164.9303288, 0, None)
Ho166 = Element('Ho166', 67, 166, 165.9322909, 96566.40000000001, 'beta-')

Er162 = Element('Er162', 68, 162, 161.9287884, 0, None)
Er163 = Element('Er163', 68, 163, 162.9300408, 4500.0, 'beta+')
Er164 = Element('Er164', 68, 164, 163.9292088, 0, None)
Er165 = Element('Er165', 68, 165, 164.9307345, 37296.0, 'epsilon')
Er166 = Element('Er166', 68, 166, 165.9302995, 0, None)
Er167 = Element('Er167', 68, 167, 166.9320546, 0, None)
Er168 = Element('Er168', 68, 168, 167.9323767, 0, None)
Er169 = Element('Er169', 68, 169, 168.9345968, 811468.7999999999, 'beta-')
Er170 = Element('Er170', 68, 170, 169.9354702, 0, None)

Tm168 = Element('Tm168', 69, 168, 167.9341774, 8043839.999999999, 'beta+ , beta-')
Tm169 = Element('Tm169', 69, 169, 168.9342179, 0, None)
Tm170 = Element('Tm170', 69, 170, 169.935806, 11111040.0, 'beta-, epsilon')

Yb168 = Element('Yb168', 70, 168, 167.9338896, 0, None)
Yb169 = Element('Yb169', 70, 169, 168.9351825, 2766355.2, 'epsilon')
Yb170 = Element('Yb170', 70, 170, 169.9347664, 0, None)
Yb171 = Element('Yb171', 70, 171, 170.9363302, 0, None)
Yb172 = Element('Yb172', 70, 172, 171.9363859, 0, None)
Yb173 = Element('Yb173', 70, 173, 172.9382151, 0, None)
Yb174 = Element('Yb174', 70, 174, 173.9388664, 0, None)
Yb175 = Element('Yb175', 70, 175, 174.9412808, 361583.99999999994, 'beta-')
Yb176 = Element('Yb176', 70, 176, 175.9425764, 0, None)

Lu163 = Element('Lu163', 71, 163, 162.941179, 238.20000000000002, 'beta+')
Lu164 = Element('Lu164', 71, 164, 163.941339, 188.4, 'beta+')
Lu175 = Element('Lu175', 71, 175, 174.9407752, 0, None)
Lu176 = Element('Lu176', 71, 176, 175.9426897, 1.1857536e+18, 'beta-')

Hf161 = Element('Hf161', 72, 161, 160.950278, 18.4, 'beta+ , alpha')
Hf162 = Element('Hf162', 72, 162, 161.9472148, 39.4, 'beta+ , alpha')
Hf163 = Element('Hf163', 72, 163, 162.947113, 40.0, 'beta+ , alpha')
Hf164 = Element('Hf164', 72, 164, 163.944371, 111.0, 'beta+')
Hf165 = Element('Hf165', 72, 165, 164.944567, 76.0, 'beta+')
Hf166 = Element('Hf166', 72, 166, 165.94218, 406.2, 'beta+')
Hf174 = Element('Hf174', 72, 174, 173.9400461, 6.3072e+22, 'alpha')
Hf175 = Element('Hf175', 72, 175, 174.9415092, 6048000.0, 'epsilon')
Hf176 = Element('Hf176', 72, 176, 175.9414076, 0, None)
Hf177 = Element('Hf177', 72, 177, 176.9432277, 0, None)
Hf178 = Element('Hf178', 72, 178, 177.9437058, 0, None)
Hf179 = Element('Hf179', 72, 179, 178.9458232, 0, None)
Hf180 = Element('Hf180', 72, 180, 179.946557, 0, None)

Ta180 = Element('Ta180', 73, 180, 179.9474648, 29354.4, 'epsilon, beta-')
Ta181 = Element('Ta181', 73, 181, 180.9479958, 0, None)
Ta182 = Element('Ta182', 73, 182, 181.9501519, 9913536.0, 'beta-')

W179 = Element('W179', 74, 179, 178.947077, 2223.0, 'beta+')
W180 = Element('W180', 74, 180, 179.9467108, 2.081376e+25, '2beta+')
W181 = Element('W181', 74, 181, 180.9481978, 10471680.0, 'epsilon')
W182 = Element('W182', 74, 182, 181.94820394, 0, None)
W183 = Element('W183', 74, 183, 182.95022275, 2.112912e+28, 'alpha')
W184 = Element('W184', 74, 184, 183.95093092, 0, None)

Re183 = Element('Re183', 75, 183, 182.9508196, 6048000.0, 'epsilon')
Re184 = Element('Re184', 75, 184, 183.9525228, 3058560.0, 'beta+')
Re185 = Element('Re185', 75, 185, 184.9529545, 0, None)
Re186 = Element('Re186', 75, 186, 185.9549856, 321287.04, 'beta-, epsilon')
Re187 = Element('Re187', 75, 187, 186.9557501, 1.3655088e+18, 'beta-, alpha')

Os184 = Element('Os184', 76, 184, 183.9524885, 1.766016e+21, 'alpha')
Os185 = Element('Os185', 76, 185, 184.9540417, 8087039.999999999, 'epsilon')
Os186 = Element('Os186', 76, 186, 185.953835, 6.3072e+22, 'alpha')
Os187 = Element('Os187', 76, 187, 186.9557474, 0, None)
Os188 = Element('Os188', 76, 188, 187.9558352, 0, None)
Os189 = Element('Os189', 76, 189, 188.9581442, 0, None)
Os190 = Element('Os190', 76, 190, 189.9584437, 0, None)
Os191 = Element('Os191', 76, 191, 190.9609264, 1330560.0, 'beta-')
Os192 = Element('Os192', 76, 192, 191.961477, 0, None)

Ir190 = Element('Ir190', 77, 190, 189.9605412, 1017792.0, 'beta+')
Ir191 = Element('Ir191', 77, 191, 190.9605893, 0, None)
Ir192 = Element('Ir192', 77, 192, 191.9626002, 6378825.6, 'beta-, epsilon')
Ir193 = Element('Ir193', 77, 193, 192.9629216, 0, None)

Pt190 = Element('Pt190', 78, 190, 189.9599297, 2.04984e+19, 'alpha')
Pt191 = Element('Pt191', 78, 191, 190.9616729, 244512.0, 'epsilon')
Pt192 = Element('Pt192', 78, 192, 191.9610387, 0, None)
Pt193 = Element('Pt193', 78, 193, 192.9629824, 1576800000.0, 'epsilon')
Pt194 = Element('Pt194', 78, 194, 193.9626809, 0, None)
Pt195 = Element('Pt195', 78, 195, 194.9647917, 0, None)
Pt196 = Element('Pt196', 78, 196, 195.96495209, 0, None)
Pt197 = Element('Pt197', 78, 197, 196.96734069, 71609.40000000001, 'beta-')
Pt198 = Element('Pt198', 78, 198, 197.9678949, 0, None)

Au196 = Element('Au196', 79, 196, 195.9665699, 532820.16, 'beta+ , beta-')
Au197 = Element('Au197', 79, 197, 196.96656879, 0, None)
Au198 = Element('Au198', 79, 198, 197.96824242, 232770.24000000002, 'beta-')

Hg196 = Element('Hg196', 80, 196, 195.9658326, 0, None)
Hg197 = Element('Hg197', 80, 197, 196.9672128, 230904.0, 'epsilon')
Hg198 = Element('Hg198', 80, 198, 197.9667686, 0, None)
Hg199 = Element('Hg199', 80, 199, 198.96828064, 0, None)
Hg200 = Element('Hg200', 80, 200, 199.96832659, 0, None)
Hg201 = Element('Hg201', 80, 201, 200.97030284, 0, None)
Hg202 = Element('Hg202', 80, 202, 201.9706434, 0, None)
Hg203 = Element('Hg203', 80, 203, 202.9728728, 4025721.6, 'beta-')
Hg204 = Element('Hg204', 80, 204, 203.97349398, 0, None)

Tl202 = Element('Tl202', 81, 202, 201.972102, 1063584.0, 'beta+')
Tl203 = Element('Tl203', 81, 203, 202.9723446, 0, None)
Tl204 = Element('Tl204', 81, 204, 203.9738639, 119300688.0, 'beta-, epsilon')
Tl205 = Element('Tl205', 81, 205, 204.9744278, 0, None)

Pb203 = Element('Pb203', 82, 203, 202.9733911, 186912.0, 'epsilon')
Pb204 = Element('Pb204', 82, 204, 203.973044, 4.41504e+24, 'alpha')
Pb205 = Element('Pb205', 82, 205, 204.9744822, 545572800000000.0, 'epsilon')
Pb206 = Element('Pb206', 82, 206, 205.9744657, 0, None)
Pb207 = Element('Pb207', 82, 207, 206.9758973, 0, None)
Pb208 = Element('Pb208', 82, 208, 207.9766525, 0, None)
Pb209 = Element('Pb209', 82, 209, 208.9810905, 11642.4, 'beta-')
Pb210 = Element('Pb210', 82, 210, 209.9841889, 700099200.0, 'beta-, alpha')

Bi206 = Element('Bi206', 83, 206, 205.9784993, 539395.2000000001, 'beta+')
Bi207 = Element('Bi207', 83, 207, 206.978471, 994960800.0, 'beta+')
Bi208 = Element('Bi208', 83, 208, 207.9797425, 11605248000000.0, 'beta+')
Bi209 = Element('Bi209', 83, 209, 208.9803991, 0, None)
Bi210 = Element('Bi210', 83, 210, 209.9841207, 433036.8, 'beta-, alpha')
Bi211 = Element('Bi211', 83, 211, 210.9872697, 128.4, 'alpha, beta-')

Po207 = Element('Po207', 84, 207, 206.9815938, 20880.0, 'beta+ , alpha')
Po208 = Element('Po208', 84, 208, 207.9812461, 91391328.0, 'alpha, beta+')
Po209 = Element('Po209', 84, 209, 208.9824308, 3910464000.0, 'alpha, beta+')
Po210 = Element('Po210', 84, 210, 209.9828741, 11955686.4, 'alpha')
Po211 = Element('Po211', 84, 211, 210.9866536, 0.516, 'alpha')
Po212 = Element('Po212', 84, 212, 211.9888684, 2.9899999999999996e-07, 'alpha')
Po213 = Element('Po213', 84, 213, 212.9928576, 3.72e-06, 'alpha')
Po214 = Element('Po214', 84, 214, 213.9952017, 0.0001636, 'alpha')
Po215 = Element('Po215', 84, 215, 214.9994201, 0.001781, 'alpha, beta-')
Po216 = Element('Po216', 84, 216, 216.0019152, 0.145, 'alpha')

At210 = Element('At210', 85, 210, 209.9871479, 29160.0, 'beta+ , alpha')
At211 = Element('At211', 85, 211, 210.9874966, 25970.4, 'epsilon, alpha')
At212 = Element('At212', 85, 212, 211.9907377, 0.314, 'alpha, beta+ , beta-')
At213 = Element('At213', 85, 213, 212.992937, 1.2500000000000002e-07, 'alpha')
At214 = Element('At214', 85, 214, 213.9963721, 5.58e-07, 'alpha')
At215 = Element('At215', 85, 215, 214.9986528, 0.0001, 'alpha')

Rn220 = Element('Rn220', 86, 220, 220.0113941, 55.6, 'alpha')
Rn221 = Element('Rn221', 86, 221, 221.0155371, 1500.0, 'beta-, alpha')
Rn222 = Element('Rn222', 86, 222, 222.0175782, 330350.4, 'alpha')
Rn223 = Element('Rn223', 86, 223, 223.0218893, 1458.0, 'beta-')

Fr221 = Element('Fr221', 87, 221, 221.0142552, 286.1, 'alpha, beta-')
Fr222 = Element('Fr222', 87, 222, 222.017552, 852.0, 'beta-')
Fr223 = Element('Fr223', 87, 223, 223.019736, 1320.0, 'beta-, alpha')
Fr224 = Element('Fr224', 87, 224, 224.023398, 199.8, 'beta-')
Fr225 = Element('Fr225', 87, 225, 225.025573, 237.0, 'beta-')
Fr226 = Element('Fr226', 87, 226, 226.029566, 49.0, 'beta-')

Ra222 = Element('Ra222', 88, 222, 222.0153748, 38.0, 'alpha, 14C')
Ra223 = Element('Ra223', 88, 223, 223.0185023, 987552.0, 'alpha, 14C')
Ra224 = Element('Ra224', 88, 224, 224.020212, 313796.16, 'alpha, 14C')
Ra225 = Element('Ra225', 88, 225, 225.0236119, 1287360.0, 'beta-')
Ra226 = Element('Ra226', 88, 226, 226.0254103, 50457600000.0, 'alpha, 14C')
Ra227 = Element('Ra227', 88, 227, 227.0291783, 2532.0, 'beta-')
Ra228 = Element('Ra228', 88, 228, 228.0310707, 181332000.0, 'beta-')
Ra229 = Element('Ra229', 88, 229, 229.034942, 240.0, 'beta-')

Ac224 = Element('Ac224', 89, 224, 224.0217232, 10008.0, 'beta+ , alpha')
Ac225 = Element('Ac225', 89, 225, 225.02323, 864000.0, 'alpha, 14C')
Ac226 = Element('Ac226', 89, 226, 226.0260984, 105732.0, 'beta-, epsilon, alpha')
Ac227 = Element('Ac227', 89, 227, 227.0277523, 686601792.0, 'beta-, alpha')
Ac228 = Element('Ac228', 89, 228, 228.0310215, 22140.0, 'beta-')
Ac229 = Element('Ac229', 89, 229, 229.032956, 3762.0, 'beta-')

Th224 = Element('Th224', 90, 224, 224.021464, 1.04, 'alpha')
Th225 = Element('Th225', 90, 225, 225.0239514, 525.0, 'alpha, epsilon')
Th226 = Element('Th226', 90, 226, 226.0249034, 1834.2, 'alpha')
Th227 = Element('Th227', 90, 227, 227.0277042, 1615420.7999999998, 'alpha')
Th228 = Element('Th228', 90, 228, 228.0287413, 60312600.0, 'alpha, 20O')
Th229 = Element('Th229', 90, 229, 229.0317627, 250143552000.0, 'alpha')
Th230 = Element('Th230', 90, 230, 230.0331341, 2377814400000.0, 'alpha, 24ne, SF')
Th231 = Element('Th231', 90, 231, 231.0363046, 91872.0, 'beta-, alpha')
Th232 = Element('Th232', 90, 232, 232.0380558, 4.41504e+17, 'alpha, SF')
Th233 = Element('Th233', 90, 233, 233.0415823, 1309.8, 'beta-')
Th234 = Element('Th234', 90, 234, 234.0436014, 2082240.0000000002, 'beta-')
Th235 = Element('Th235', 90, 235, 235.047255, 426.0, 'beta-')

Pa227 = Element('Pa227', 91, 227, 227.0288054, 2298.0, 'alpha, epsilon')
Pa228 = Element('Pa228', 91, 228, 228.0310517, 79200.0, 'beta+ , alpha')
Pa229 = Element('Pa229', 91, 229, 229.0320972, 129600.0, 'epsilon, alpha')
Pa230 = Element('Pa230', 91, 230, 230.034541, 1503359.9999999998, 'beta+ , beta-, alpha')
Pa231 = Element('Pa231', 91, 231, 231.0358842, 1033119360000.0, 'alpha, SF')
Pa232 = Element('Pa232', 91, 232, 232.0385917, 114048.0, 'beta-, epsilon')
Pa233 = Element('Pa233', 91, 233, 233.0402473, 2332800.0, 'beta-')

U231 = Element('U231', 92, 231, 231.0362939, 362880.0, 'epsilon, alpha')
U232 = Element('U232', 92, 232, 232.0371563, 2172830400.0, 'alpha, SF')
U233 = Element('U233', 92, 233, 233.0396355, 5020531200000.0, 'alpha, SF')
U234 = Element('U234', 92, 234, 234.0409523, 7742088000000.0, 'alpha, SF')
U235 = Element('U235', 92, 235, 235.0439301, 2.2201344e+16, 'alpha, SF')
U236 = Element('U236', 92, 236, 236.0455682, 738573120000000.0, 'alpha, SF')
U237 = Element('U237', 92, 237, 237.0487304, 583200.0, 'beta-')
U238 = Element('U238', 92, 238, 238.0507884, 1.40902848e+17, 'alpha, SF')
U239 = Element('U239', 92, 239, 239.0542935, 1407.0, 'beta-')
U240 = Element('U240', 92, 240, 240.0565934, 50760.0, 'beta-')

Np234 = Element('Np234', 93, 234, 234.0428953, 380160.00000000006, 'beta+')
Np235 = Element('Np235', 93, 235, 235.0440635, 34223040.0, 'epsilon, alpha')
Np236 = Element('Np236', 93, 236, 236.04657, 4825008000000.0, 'epsilon, beta-, alpha')
Np237 = Element('Np237', 93, 237, 237.0481736, 67613184000000.0, 'alpha, SF')
Np238 = Element('Np238', 93, 238, 238.0509466, 182908.8, 'beta-')
Np239 = Element('Np239', 93, 239, 239.0529392, 203558.4, 'beta-')

Pu235 = Element('Pu235', 94, 235, 235.045286, 1518.0, 'beta+ , alpha')
Pu236 = Element('Pu236', 94, 236, 236.0460581, 90129888.0, 'alpha, SF')
Pu237 = Element('Pu237', 94, 237, 237.0484098, 3943296.0, 'epsilon, alpha')
Pu238 = Element('Pu238', 94, 238, 238.0495601, 2765707200.0, 'alpha, SF')
Pu239 = Element('Pu239', 94, 239, 239.0521636, 760332960000.0, 'alpha, SF')
Pu240 = Element('Pu240', 94, 240, 240.0538138, 206907696000.0, 'alpha, SF')
Pu241 = Element('Pu241', 94, 241, 241.0568517, 451879344.0, 'beta-, alpha, SF')
Pu242 = Element('Pu242', 94, 242, 242.0587428, 11826000000000.0, 'alpha, SF')
Pu243 = Element('Pu243', 94, 243, 243.0620036, 17841.600000000002, 'beta-')
Pu244 = Element('Pu244', 94, 244, 244.0642053, 2522880000000000.0, 'alpha, SF')
Pu245 = Element('Pu245', 94, 245, 245.067826, 37800.0, 'beta-')

Am240 = Element('Am240', 95, 240, 240.0553, 182880.0, 'beta+ , alpha')
Am241 = Element('Am241', 95, 241, 241.0568293, 13642473600.0, 'alpha, SF')
Am242 = Element('Am242', 95, 242, 242.0595494, 57672.0, 'beta-, epsilon')
Am243 = Element('Am243', 95, 243, 243.0613813, 232231104000.0, 'alpha, SF')
Am244 = Element('Am244', 95, 244, 244.0642851, 36360.0, 'beta-, SF')

Cm242 = Element('Cm242', 96, 242, 242.058836, 14065920.000000002, 'alpha, SF')
Cm243 = Element('Cm243', 96, 243, 243.0613893, 917697600.0, 'alpha, epsilon, SF')
Cm244 = Element('Cm244', 96, 244, 244.0627528, 570801600.0, 'alpha, SF')
Cm245 = Element('Cm245', 96, 245, 245.0654915, 265627728000.0, 'alpha, SF')
Cm246 = Element('Cm246', 96, 246, 246.0672238, 148408416000.0, 'alpha, SF')
Cm247 = Element('Cm247', 96, 247, 247.0703541, 491961600000000.0, 'alpha')
Cm248 = Element('Cm248', 96, 248, 248.0723499, 10974528000000.0, 'alpha, SF')
Cm249 = Element('Cm249', 96, 249, 249.0759548, 3849.0000000000005, 'beta-')
Cm250 = Element('Cm250', 96, 250, 250.078358, 261748800000.0, 'SF, alpha, beta-')
Cm251 = Element('Cm251', 96, 251, 251.082286, 1008.0, 'beta-')

Bk246 = Element('Bk246', 97, 246, 246.068673, 155520.0, 'beta+')
Bk247 = Element('Bk247', 97, 247, 247.0703073, 43519680000.0, 'alpha')
Bk248 = Element('Bk248', 97, 248, 248.073088, 283824000.0, 'alpha')
Bk249 = Element('Bk249', 97, 249, 249.0749877, 28512000.0, 'beta-, alpha, SF')
Bk250 = Element('Bk250', 97, 250, 250.0783167, 11563.2, 'beta-')

Cf248 = Element('Cf248', 98, 248, 248.0721851, 28814400.0, 'alpha, SF')
Cf249 = Element('Cf249', 98, 249, 249.0748539, 11069136000.0, 'alpha, SF')
Cf250 = Element('Cf250', 98, 250, 250.0764062, 412490880.0, 'alpha, SF')
Cf251 = Element('Cf251', 98, 251, 251.0795886, 28319328000.0, 'alpha, SF')
Cf252 = Element('Cf252', 98, 252, 252.0816272, 83412720.0, 'alpha, SF')
Cf253 = Element('Cf253', 98, 253, 253.0851345, 1538784.0, 'beta-, alpha')

Es251 = Element('Es251', 99, 251, 251.0799936, 118800.0, 'epsilon, alpha')
Es252 = Element('Es252', 99, 252, 252.08298, 40754880.0, 'alpha, epsilon')
Es253 = Element('Es253', 99, 253, 253.0848257, 1768608.0, 'alpha, SF')

Fm256 = Element('Fm256', 100, 256, 256.0917745, 9456.0, 'SF, alpha')
Fm257 = Element('Fm257', 100, 257, 257.0951061, 8683200.0, 'alpha, SF')
Fm258 = Element('Fm258', 100, 258, 258.09708, 0.00037, 'SF')

Md256 = Element('Md256', 101, 256, 256.09389, 4620.0, 'beta+ , alpha, SF')
Md257 = Element('Md257', 101, 257, 257.0955424, 19872.0, 'epsilon, alpha, SF')
Md258 = Element('Md258', 101, 258, 258.0984315, 4449600.0, 'alpha, beta-, beta+')
Md259 = Element('Md259', 101, 259, 259.10051, 5760.0, 'SF, alpha')

No258 = Element('No258', 102, 258, 258.09821, 0.0012, 'SF')
No259 = Element('No259', 102, 259, 259.10103, 3480.0, 'alpha, epsilon, SF')

Lr261 = Element('Lr261', 103, 261, 261.10688, 2340.0, 'SF')
Lr262 = Element('Lr262', 103, 262, 262.10961, 14400.0, 'epsilon, alpha, SF')

Rf262 = Element('Rf262', 104, 262, 262.10992, 2.3, 'SF, alpha')
Rf263 = Element('Rf263', 104, 263, 263.11249, 600.0, 'SF, alpha')
Rf264 = Element('Rf264', 104, 264, 264.11388, None, 'alpha')

Db263 = Element('Db263', 105, 263, 263.11499, 27.0, 'SF, alpha, beta+')
Db268 = Element('Db268', 105, 268, 268.12567, 115200.0, 'SF')

Sg266 = Element('Sg266', 106, 266, 266.12198, 21.0, 'alpha')
Sg271 = Element('Sg271', 106, 271, 271.13393, 144.0, 'alpha, SF')

Bh264 = Element('Bh264', 107, 264, 264.12459, 0.44, 'alpha')
Bh271 = Element('Bh271', 107, 271, 271.13526, None, 'alpha')
Bh272 = Element('Bh272', 107, 272, 272.13826, 10.0, 'alpha')

Hs269 = Element('Hs269', 108, 269, 269.13375, 9.7, 'alpha')
Hs276 = Element('Hs276', 108, 276, 276.14846, None, 'alpha, SF')
Hs277 = Element('Hs277', 108, 277, 277.1519, 0.003, 'alpha')

Mt268 = Element('Mt268', 109, 268, 268.13865, 0.021, 'alpha')
Mt276 = Element('Mt276', 109, 276, 276.15159, 0.72, 'alpha')
Mt277 = Element('Mt277', 109, 277, 277.15327, 5.0, 'SF, alpha')

Ds273 = Element('Ds273', 110, 273, 273.14856, 0.00017, 'alpha')
Ds280 = Element('Ds280', 110, 280, 280.16131, None, None)
Ds281 = Element('Ds281', 110, 281, 281.16451, 13.0, 'alpha, SF')

Rg280 = Element('Rg280', 111, 280, 280.16514, 3.6, 'alpha')
Rg281 = Element('Rg281', 111, 281, 281.16636, 17.0, 'SF, alpha')

Cn277 = Element('Cn277', 112, 277, 277.16364, None, None)
Cn285 = Element('Cn285', 112, 285, 285.17712, 30.0, 'alpha')

elements = [H1, H2, H3, H4, He3, He4, He5, He6, Li5, Li6, Li7, Li8, Be7, Be8, Be9, Be10, B8, B9, B10, B11, B12, C10,
            C11, C12, C13, C14, C15, N13, N14, N15, N16, N17, N18, O14, O15, O16, O17, O18, O19, F17, F18, F19, F20,
            Ne19, Ne20, Ne21, Ne22, Ne23, Ne24, Na21, Na22, Na23, Na24, Na25, Mg22, Mg23, Mg24, Mg25, Mg26, Mg27, Al25,
            Al26, Al27, Al28, Si26, Si27, Si28, Si29, Si30, Si31, P30, P31, P32, P33, P34, S31, S32, S33, S34, S35, S36,
            Cl35, Cl36, Cl37, Cl38, Ar35, Ar36, Ar37, Ar38, Ar39, Ar40, K38, K39, K40, K41, K42, K43, Ca39, Ca40, Ca41,
            Ca42, Ca43, Ca44, Ca45, Ca46, Ca47, Ca48, Ca49, Ca50, Sc44, Sc45, Sc46, Sc47, Ti44, Ti45, Ti46, Ti47, Ti48,
            Ti49, Ti50, Ti51, V48, V49, V50, V51, V52, Cr49, Cr50, Cr51, Cr52, Cr53, Cr54, Cr55, Cr56, Mn52, Mn53, Mn54,
            Mn55, Mn56, Fe53, Fe54, Fe55, Fe56, Fe57, Fe58, Fe59, Fe60, Co56, Co57, Co58, Co59, Co60, Ni57, Ni58, Ni59,
            Ni60, Ni61, Ni62, Ni63, Ni64, Ni65, Cu62, Cu63, Cu64, Cu65, Cu66, Zn63, Zn64, Zn65, Zn66, Zn67, Zn68, Zn69,
            Zn70, Zn71, Ga68, Ga69, Ga70, Ga71, Ga72, Ge69, Ge70, Ge71, Ge72, Ge73, Ge74, Ge75, Ge76, Ge77, As73, As74,
            As75, As76, Se73, Se74, Se75, Se76, Se77, Se78, Se79, Se80, Se81, Se82, Se83, Br78, Br79, Br80, Br81, Br82,
            Kr78, Kr79, Kr80, Kr81, Kr82, Kr83, Kr84, Kr85, Kr86, Kr87, Kr88, Kr89, Kr90, Kr91, Kr92, Rb84, Rb85, Rb86,
            Rb87, Sr84, Sr85, Sr86, Sr87, Sr88, Sr89, Sr90, Sr91, Sr92, Sr93, Sr94, Y88, Y89, Y90, Y91, Y92, Y93, Y94,
            Y95, Zr89, Zr90, Zr91, Zr92, Zr93, Zr94, Zr95, Zr96, Nb90, Nb91, Nb92, Nb93, Nb94, Mo92, Mo93, Mo94, Mo95,
            Mo96, Mo97, Mo98, Mo99, Mo100, Tc96, Tc97, Tc98, Tc99, Tc100, Ru95, Ru96, Ru97, Ru98, Ru99, Ru100, Ru101,
            Ru102, Ru103, Ru104, Ru105, Ru106, Rh101, Rh102, Rh103, Rh104, Pd100, Pd101, Pd102, Pd103, Pd104, Pd105,
            Pd106, Pd107, Pd108, Pd109, Pd110, Ag105, Ag106, Ag107, Ag108, Ag109, Ag110, Cd105, Cd106, Cd107, Cd108,
            Cd109, Cd110, Cd111, Cd112, Cd113, Cd114, Cd115, Cd116, In112, In113, In114, In115, Sn112, Sn113, Sn114,
            Sn115, Sn116, Sn117, Sn118, Sn119, Sn120, Sn121, Sn122, Sn123, Sn124, Sb120, Sb121, Sb122, Sb123, Sb124,
            Sb125, Te120, Te121, Te122, Te123, Te124, Te125, Te126, Te127, Te128, Te129, Te130, I125, I126, I127, I128,
            I129, I130, I131, I132, I133, I134, I135, I136, Xe124, Xe125, Xe126, Xe127, Xe128, Xe129, Xe130, Xe131,
            Xe132, Xe133, Xe134, Xe135, Xe136, Cs132, Cs133, Cs134, Cs135, Cs136, Cs137, Ba130, Ba131, Ba132, Ba133,
            Ba134, Ba135, Ba136, Ba137, Ba138, Ba139, Ba140, Ba141, Ba142, Ba143, La137, La138, La139, La140, Ce136,
            Ce137, Ce138, Ce139, Ce140, Ce141, Ce142, Ce143, Pr140, Pr141, Pr142, Nd142, Nd143, Nd144, Nd145, Nd146,
            Nd147, Nd148, Nd149, Nd150, Pm154, Pm155, Sm144, Sm145, Sm146, Sm147, Sm148, Sm149, Sm150, Sm151, Sm152,
            Sm153, Sm154, Eu150, Eu151, Eu152, Eu153, Eu154, Gd152, Gd153, Gd154, Gd155, Gd156, Gd157, Gd158, Gd159,
            Gd160, Tb158, Tb159, Tb160, Dy156, Dy157, Dy158, Dy159, Dy160, Dy161, Dy162, Dy163, Dy164, Dy165, Ho164,
            Ho165, Ho166, Er162, Er163, Er164, Er165, Er166, Er167, Er168, Er169, Er170, Tm168, Tm169, Tm170, Yb168,
            Yb169, Yb170, Yb171, Yb172, Yb173, Yb174, Yb175, Yb176, Lu163, Lu164, Lu175, Lu176, Hf161, Hf162, Hf163,
            Hf164, Hf165, Hf166, Hf174, Hf175, Hf176, Hf177, Hf178, Hf179, Hf180, Ta180, Ta181, Ta182, W179, W180, W181,
            W182, W183, W184, Re183, Re184, Re185, Re186, Re187, Os184, Os185, Os186, Os187, Os188, Os189, Os190, Os191,
            Os192, Ir190, Ir191, Ir192, Ir193, Pt190, Pt191, Pt192, Pt193, Pt194, Pt195, Pt196, Pt197, Pt198, Au196,
            Au197, Au198, Hg196, Hg197, Hg198, Hg199, Hg200, Hg201, Hg202, Hg203, Hg204, Tl202, Tl203, Tl204, Tl205,
            Pb203, Pb204, Pb205, Pb206, Pb207, Pb208, Pb209, Pb210, Bi206, Bi207, Bi208, Bi209, Bi210, Bi211, Po207,
            Po208, Po209, Po210, Po211, Po212, Po213, Po214, Po215, Po216, At210, At211, At212, At213, At214, At215,
            Rn220, Rn221, Rn222, Rn223, Fr221, Fr222, Fr223, Fr224, Fr225, Fr226, Ra222, Ra223, Ra224, Ra225, Ra226,
            Ra227, Ra228, Ra229, Ac224, Ac225, Ac226, Ac227, Ac228, Ac229, Th224, Th225, Th226, Th227, Th228, Th229,
            Th230, Th231, Th232, Th233, Th234, Th235, Pa227, Pa228, Pa229, Pa230, Pa231, Pa232, Pa233, U231, U232, U233,
            U234, U235, U236, U237, U238, U239, U240, Np234, Np235, Np236, Np237, Np238, Np239, Pu235, Pu236, Pu237,
            Pu238, Pu239, Pu240, Pu241, Pu242, Pu243, Pu244, Pu245, Am240, Am241, Am242, Am243, Am244, Cm242, Cm243,
            Cm244, Cm245, Cm246, Cm247, Cm248, Cm249, Cm250, Cm251, Bk246, Bk247, Bk248, Bk249, Bk250, Cf248, Cf249,
            Cf250, Cf251, Cf252, Cf253, Es251, Es252, Es253, Fm256, Fm257, Fm258, Md256, Md257, Md258, Md259, No258,
            No259, Lr261, Lr262, Rf262, Rf263, Rf264, Db263, Db268, Sg266, Sg271, Bh264, Bh271, Bh272, Hs269, Hs276,
            Hs277, Mt268, Mt276, Mt277, Ds273, Ds280, Ds281, Rg280, Rg281, Cn277, Cn285]


def get_element(protons, nucleons) -> Element:
    for element in elements:
        if element.protons == protons and element.nucleons == nucleons:
            return element


def alpha_decay(element: Element) -> Element:
    return get_element(element.protons - He4.protons, element.nucleons - He4.nucleons)


print(alpha_decay(U238))
print(get_element(U238.protons - He4.protons, U238.nucleons - He4.nucleons))
print(U238.mass)
print(C14.half_life)
print()
print((Ba138.mass + 94.9398 + 3 * n.mass) - (U235.mass+n.mass), "mass")

print(-((Ba138.mass + 94.9398 + 3 * n.mass) - (U235.mass+n.mass)) * (1.66054 * 10 ** -27) * 299792458 ** 2, "J")
print(-((Ba138.mass + 94.9398 + 3 * n.mass) - (U235.mass+n.mass)) * 931.49, "MeV")


