import csv
from Class.Class_Entity_Stats import Entity_stats
def parse_value(value):
    if value is None or value == "":
        return None

    v = value.strip()

    if v.lower() in ("true", "false"):
        return v.lower() == "true"

    try:
        if "." in v:
            return float(v)
        return int(v)
    except ValueError:
        pass

    if ";" in v:
        return v.split(";")

    return v


def load_entity_stats(path, only_hero=False):
    entities = []

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            # Filtre Hero
            if only_hero and row.get("Type") != "Hero":
                continue

            # Conversion des types
            parsed_row = {
                key: parse_value(value)
                for key, value in row.items()
            }

            # Création de l'entity
            entity = Entity_stats(**parsed_row)
            entities.append(entity)

    return entities

with open("clean/characters_clean.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        parsed_row = {k: parse_value(v) for k, v in row.items()}
        print(parsed_row.keys())  # ✅ Ici parsed_row est défini
        break  # juste pour tester la première ligne