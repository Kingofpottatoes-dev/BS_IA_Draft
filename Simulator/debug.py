import csv
import os

INPUT_CSV = "assets/maps.csv"
OUTPUT_DIR = "txt_maps"

os.makedirs(OUTPUT_DIR, exist_ok=True)

current_map = None
current_rows = []

def get_prefix(map_name):
    """Retourne le préfixe avant '_' ou le nom entier"""
    return map_name.split("_")[0]

with open(INPUT_CSV, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        map_name = row["Map"].strip() if row["Map"] else ""
        data = row["Data"]

        # Nouvelle map détectée
        if map_name:
            # Sauvegarder la map précédente
            if current_map:
                prefix = get_prefix(current_map)
                save_dir = os.path.join(OUTPUT_DIR, prefix)
                os.makedirs(save_dir, exist_ok=True)

                with open(os.path.join(save_dir, f"{current_map}.txt"), "w") as out:
                    out.write("\n".join(current_rows))

            # Reset pour la nouvelle map
            current_map = map_name
            current_rows = []

        # Ajouter la ligne de grille
        if data:
            clean_line = data.strip().strip(",").strip('"')
            current_rows.append(clean_line)

# Sauvegarde de la dernière map
if current_map and current_rows:
    prefix = get_prefix(current_map)
    save_dir = os.path.join(OUTPUT_DIR, prefix)
    os.makedirs(save_dir, exist_ok=True)

    with open(os.path.join(save_dir, f"{current_map}.txt"), "w") as out:
        out.write("\n".join(current_rows))

print("✅ Maps exportées et regroupées par préfixe")