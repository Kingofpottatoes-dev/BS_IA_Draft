import csv
import os
from Class.Class_Entity_Stats import Entity_stats
def parse_value(value):
    if value is None or value == "":
        return None

    # assure qu'on a bien une chaîne
    v = str(value).strip()

    # bool
    if v.lower() == "true":
        return True
    if v.lower() == "false":
        return False

    # int / float
    try:
        if "." in v:
            return float(v)
        return int(v)
    except ValueError:
        pass

    # sinon string
    return v


def load_entity_stats(csv_path, only_hero=False):
    """Charge les entités depuis un CSV en ignorant les deux premières lignes

    - la 1ère ligne est l'entête (noms de colonnes)
    - la 2ème ligne contient les types et est ignorée

    La liste retournée `entities` est telle que `entities[i]` correspond à la
    (i+3)-ème ligne du fichier CSV (les 2 premières lignes sont l'entête et les types).
    """
    entities = []

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)

        # trouver la 1ère ligne non vide qui fait office d'entête
        fieldnames = None
        for row in reader:
            if any(str(cell).strip() for cell in row):
                fieldnames = row
                break
        if fieldnames is None:
            return entities

        # ignorer la 2ème ligne non vide (ligne des types)
        for row in reader:
            if any(str(cell).strip() for cell in row):
                # c'est la ligne des types => on la saute
                break

        # trouver l'indice de la colonne "Type" (si présent) pour le filtrage
        type_col = None
        for i, name in enumerate(fieldnames):
            if str(name).strip().lower() == "type":
                type_col = i
                break

        for row in reader:
            # ignorer les lignes totalement vides
            if not any(str(cell).strip() for cell in row):
                continue

            # s'assurer que la ligne a le bon nombre de colonnes
            if len(row) < len(fieldnames):
                row += [None] * (len(fieldnames) - len(row))

            # filtrer Hero si demandé
            if only_hero and type_col is not None:
                if str(row[type_col]).strip().lower() != "hero":
                    continue

            # créer la liste des valeurs dans le bon ordre
            values = [parse_value(row[i]) for i in range(len(fieldnames))]

            # créer l'objet Entity_stats
            entity = Entity_stats(*values)
            entities.append(entity)

    return entities
script_dir = os.path.dirname(os.path.abspath(__file__))  # dossier où est le script
csv_path = os.path.join(script_dir, "..", "clean", "characters_clean.csv")
entities = load_entity_stats(csv_path, False)