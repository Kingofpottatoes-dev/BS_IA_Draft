with open("txt_maps/reference_map.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

print("Nombre de lignes :", len(lines))
for i, line in enumerate(lines):
    print(i, repr(line))