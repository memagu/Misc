converter = {"Ys": 10**24,
                    "Zs": 10**21,
                    "Es": 10**18,
                    "Ps": 10**15,
                    "Ts": 10**12,
                    "Gs": 10**9,
                    "Ms": 10**6,
                    "ks": 10**3,
                    "hs": 10**2,
                    "das": 10 ** 1,
                    "s": 10 ** 0,
                    "ds": 10 ** -1,
                    "cs": 10 ** -2,
                    "ms": 10 ** -3,
                    "micros": 10 ** -6,
                    "ns": 10 ** -9,
                    "ps": 10 ** -12,
                    "fs": 10 ** -15,
                    "as": 10 ** -18,
                    "zs": 10 ** -21,
                    "ys": 10 ** -24,
                    "m": 60,
                    "h": 3600,
                    "d": 86400,
                    "years": 31536000}

with open("out.txt", "w") as f_out:
    with open("structured.txt", "r") as f:
        lines = f.readlines()
        current_label = ""
        current_protons = ""
        elements = []
        for line in lines:
            line = line.strip()
            line_list = line.split("\t")
            if line_list[0] != "None":
                current_label = line_list[1]
                current_protons = int(line_list[0])
                f_out.write("\n")
            nucleons = int(line_list[2])
            elements.append(f"{current_label}{nucleons}")
            mass = float("".join([char for char in line_list[3] if char != " "]).replace(",", "."))
            half_life = line_list[4].replace(",", ".")
            if half_life == "None":
                half_life = None
            elif half_life == "stable":
                half_life = 0
            else:
                half_life = half_life.split()
                half_life = float(half_life[0]) * converter[half_life[1]]

            #print(line_list[5])
            decay = f"'{line_list[5]}'" if line_list[5] != "None" else line_list[5]

            result = f"{current_label}{nucleons} = Element('{current_label}{nucleons}', {current_protons}, {nucleons}, {mass}, {half_life}, {decay})" + "\n"

            f_out.write(result)

        f_out.write(str(elements).replace("'", ""))

