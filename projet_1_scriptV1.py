import mistletoe
from mistletoe.block_token import Heading


def creer_table_matiere(fichier):

    # Lire le fichier
    with open(fichier, "r", encoding="utf-8") as f:
        texte = f.read()

    # Vérifier si le marqueur existe
    if "**contenu:**" not in texte.lower():
        print("Aucun **contenu:** détecté.")
        return

    print("**contenu:** détecté.")

    table = "## Table des matières\n\n"

    # Parser le document
    document = mistletoe.Document(texte)

    for element in document.children:

        if isinstance(element, Heading):

            if element.level == 2 or element.level == 3 or element.level == 4 or element.level == 5 or element.level == 6:

                titre = ""

                for enfant in element.children:
                    if hasattr(enfant, "content"):
                        titre += enfant.content

                lien = titre.lower().replace(" ", "-")

                # Ajouter le titre dans la table
                if element.level == 1:
                    table += f"- [{titre}](#{lien})\n"

                elif element.level == 2:
                    table += f"  - [{titre}](#{lien})\n"

                elif element.level == 3:
                    table += f"    - [{titre}](#{lien})\n"

                elif element.level == 4:
                    table += f"      - [{titre}](#{lien})\n"

                elif element.level == 5:
                    table += f"        - [{titre}](#{lien})\n"

    # Insérer la table après le marqueur
    texte = texte.replace(
        "**contenu:**",
        "**contenu:**\n\n" + table,
        1
    )

    # Sauvegarder
    with open(fichier, "w", encoding="utf-8") as f:
        f.write(texte)

    print("Table des matières créée.")


creer_table_matiere("projet_1_markdown.md")
