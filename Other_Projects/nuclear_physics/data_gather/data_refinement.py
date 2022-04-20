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
            decay = line_list[5]

            result = f"{current_label}{nucleons} = Element('{current_label}{nucleons}', {current_protons}, {nucleons}, {mass}, '{half_life}', '{decay}')" + "\n"

            f_out.write(result)

        f_out.write(str(elements).replace("'", ""))


