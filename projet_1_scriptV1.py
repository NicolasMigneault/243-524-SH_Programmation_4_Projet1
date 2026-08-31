import mistletoe
from mistletoe.block_token import Heading


def creer_table_matiere(fichier):

    # Lire le fichier Markdown
    with open(fichier, "r", encoding="utf-8") as f:
        texte = f.read()

    table = "## Table des matières\n\n"

    # Parser le Markdown avec Mistletoe
    document = mistletoe.Document(texte)

    for element in document.children:

        # Vérifier si c'est un titre
        if isinstance(element, Heading):

            # Garder seulement les ## et ###
            if element.level == 2 or element.level == 3 or element.level == 4:

                titre = ""

                # Récupérer le texte du titre
                for enfant in element.children:
                    if hasattr(enfant, "content"):
                        titre += enfant.content

                # Créer le lien
                lien = titre.lower().replace(" ", "-")

                if element.level == 2:
                    table += f"- [{titre}](#{lien})\n"
                else:
                    table += f"  - [{titre}](#{lien})\n"

    # Ajouter la table au début du document
    nouveau_texte = table + "\n" + texte

    # Réécrire le fichier
    with open(fichier, "w", encoding="utf-8") as f:
        f.write(nouveau_texte)


# Tester avec le fichier Markdown
creer_table_matiere("projet_1_markdown.md")

print("Table des matières créée !")