# Projet d'Analyse de Vin avec Machine Learning

Ce projet consiste en une application web interactive pour analyser des données de vin et construire des modèles de Machine Learning. L'application est développée avec Streamlit et permet aux utilisateurs de charger des données, les visualiser, les traiter, entraîner des modèles et évaluer leurs performances.

# I. Lancer l'application

### 1. Assurez-vous d'avoir installé Python version 3.12.7

``python --version``

_Ou rendez-vous sur [le site officiel pour télécharger](https://www.python.org/downloads/release/python-3127/) :_

### 2. Installer les dépendances requises

``pip install -r ./requirements.txt``

### 3. Lancer l'application en local

``python -m streamlit run ./app.py``

### 4. Ouvrir avec votre navigateur le lien localhost indiqué

_Exemple : http://localhost:8501_

---

# II. Mode d'emploi

1. **Chargement des données** : Utilisez l'onglet "Chargement des données" pour importer votre fichier CSV.
2. **Visualisation & Traitement des données** : Explorez vos données avec des graphiques et gérez les valeurs manquantes.
3. **Machine Learning** : Sélectionnez un algorithme (Régression Logistique, Random Forest, SVM, KNN) et entraînez votre modèle.
4. **Évaluation** : Visualisez les performances de votre modèle avec des métriques et une matrice de confusion.

---

# III. Notes sur le processus

Le projet est divisé en plusieurs modules :

* **chargement_donnees.py** : Gère le chargement des fichiers CSV.
* **procession_donnees.py** : Contient des fonctions pour l'analyse et le traitement des données.
* **pipeline.py** : Définit le pipeline de Machine Learning.
* **evaluation.py** : Évalue le modèle entraîné.

---

# IV. A propos

### L'équipe

_Angela Cruz, David Biron, Henri Pierre, Mohammed Wasin Al Shami_

### Répartition du travail

Application Streamlit : Henri Pierre et Mohammed Wasin Al Shami

Partie AI : Angela Cruz et David Biron

## Choix techniques

* **Architecture** : Application Streamlit avec structure modulaire
* **Interface** : Utilisation d'onglets pour une navigation claire
* **Algorithmes ML** : Choix entre plusieurs algorithmes classiques de classification
