import winsound

tones = {}
freqs = []

with open("in.txt", "r") as f:
    lines = f.readlines()
    current_note = ""
    for line in lines:
        line = line.strip()
        if line in ["A", "B", "C", "D", "E", "F", "G", "A#", "C#", "D#", "F#", "G#"]:
            tones[current_note] = freqs
            current_note = line
            freqs = []
            continue
        freqs.append(int(line))

with open("out.txt", "w") as f:
    for tone in tones:
        f.write(str(tone) + " = " +  str(tones[tone]) + "\n")
