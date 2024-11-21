import os
import glob

# Chemin du dossier contenant les fichiers Python
folder_path = r"C:\Users\henri\OneDrive\Documents\Cours Diginamic\30.  Projet - Conception et développement d'IA 3J\TP_Projet_ML\Modules"

# Recherche de tous les fichiers Python dans le dossier
python_files = glob.glob(os.path.join(folder_path, "*.py"))

# Fonction pour convertir un fichier Python en fichier texte
def convert_to_text(python_file):
    with open(python_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Création du nom du fichier texte
    text_file = os.path.splitext(python_file)[0] + ".txt"
    
    # Écriture du contenu dans le fichier texte
    with open(text_file, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f"Converti : {os.path.basename(python_file)} -> {os.path.basename(text_file)}")

# Conversion de chaque fichier Python trouvé
for python_file in python_files:
    convert_to_text(python_file)

print("Conversion terminée.")
