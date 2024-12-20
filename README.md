# Projet d'Analyse de Vin avec Machine Learning

Ce projet consiste en une application web interactive pour analyser des données de vin et construire des modèles de Machine Learning. L'application est développée avec Streamlit et permet aux utilisateurs de charger des données, les visualiser, les traiter, entraîner des modèles et évaluer leurs performances.

# I. Lancer l'application

### 1. Assurez-vous d'avoir installé Python version 3.12.7

``python --version``

_Ou rendez-vous sur [le site officiel pour télécharger](https://www.python.org/downloads/release/python-3127/) :_

### 2. Installer les dépendances requises

``pip install -r ./requirements.txt``

*Streamlit doit être en version 1.31.1*

### 3. Lancer l'application en local

``python -m streamlit run ./app.py``

### 4. Ouvrir avec votre navigateur le lien localhost indiqué

_Exemple : http://localhost:8501_

---

# II. Mode d'emploi

Accéder à l'application grâce au menu latéral à gauche. Il est possible de réduire ce menu en cliquant sur la flèche, cela permet une meilleure visibilité.

#### App
1. **Chargement des données** : Utilisez l'onglet "Chargement des données" pour importer votre fichier CSV.
2. **Visualisation & Traitement des données** : Explorez vos données avec des graphiques et gérez les valeurs manquantes.
3. **Machine Learning** : Sélectionnez un algorithme (Régression Logistique, Random Forest, SVM, KNN) et entraînez votre modèle.
4. **Évaluation** : Visualisez les performances de votre modèle avec des métriques et une matrice de confusion.

#### Tools
Cette section a été créée pour tester et prendre en main _Streamlit_. Elle sert à léquipe de développeurs de _cheat-sheet_.

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

Une équipe de 4 alternants Data Engineer :

- Angela Cruz
- David Billon
- Henri Pierre
- Mohammed Wasin Al Shami

### Répartition du travail

L'équipe était en permanence en communication vocale.

Dans un premier temps, pour entamer des recherches nous avons partagé l'équipe en deux :

- Application Streamlit : Henri et Wasin
- Partie AI et Machine Learning : Angela et David

Ensuite nous avons croisé partagé nos nouvelles connaissances, nos avis et nos suggestions de ressources pour faire monter en comp&tences les autres membres de l'équipe.

Enfin, nous nous sommes partagés des tâches de développement de l'application, comme par exemple le développement de fonctionnalité, des tests, des revues de codes, des ajouts de commentaire, la rédaction de la documentation. Tout en nous entraidant en cas de doute ou de blocage.

### Choix techniques

* **Architecture** : Application Streamlit avec structure modulaire
* **Interface** : Utilisation d'onglets pour une navigation claire
* **Algorithmes ML** : Choix entre plusieurs algorithmes classiques de classification
