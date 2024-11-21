import streamlit as st
import textwrap

# Configuration de la page
st.set_page_config(page_title="Présentation des Outils Streamlit", layout="wide")

# Titre de l'application
st.title("Présentation des Composants Streamlit avec Exemples Visuels")
st.write("Explorez les exemples de tous les outils Streamlit avec des descriptions, des exemples fonctionnels et des extraits de code. Voir un aperçu en direct de chaque outil directement dans l'application.")

# Onglets pour organisation
tabs = st.tabs(["Composants Textuels", "Widgets de Saisie", "Médias", "Mises en Page", "Autres Outils"])

# Fonction d'assistance pour afficher des exemples avec aperçus visuels
def show_example(description, code, render_function):
    # Exemple Visuel
    st.markdown(f"### Exemple Visuel")
    render_function()
    
    # Description et Code
    st.markdown(f"**Description :** {description}")
    st.markdown("**Code :**")
    code_snippet = textwrap.dedent(code).strip()
    st.code(code_snippet, language="python")
    st.button("Copier le Code", key=code_snippet)  # Placeholder pour le bouton de copie

# Onglet Composants Textuels
with tabs[0]:
    st.header("Composants Textuels")
    
    show_example(
        "Affiche un grand titre pour les sections.",
        """
        st.header("Un Grand Titre")
        """,
        lambda: st.header("Un Grand Titre")
    )
    
    show_example(
        "Utilisez Markdown pour formater du texte riche comme **gras**, *italique*, ou des [liens](https://streamlit.io).",
        """
        st.markdown("Markdown est **gras**, *italique*, ou possède des [liens](https://streamlit.io).")
        """,
        lambda: st.markdown("Markdown est **gras**, *italique*, ou possède des [liens](https://streamlit.io).")
    )
    
    show_example(
        "Affichez des blocs de code Python avec surlignage de syntaxe.",
        """
        st.code("print('Bonjour, Streamlit!')", language="python")
        """,
        lambda: st.code("print('Bonjour, Streamlit!')", language="python")
    )
    
    show_example(
        "Affichez des équations mathématiques en utilisant la syntaxe LaTeX.",
        """
        st.latex(r"a^2 + b^2 = c^2")
        """,
        lambda: st.latex(r"a^2 + b^2 = c^2")
    )

# Onglet Widgets de Saisie
with tabs[1]:
    st.header("Widgets de Saisie")
    
    show_example(
        "Créez un champ de saisie pour les données utilisateur.",
        """
        name = st.text_input("Entrez votre nom :")
        """,
        lambda: st.text_input("Entrez votre nom :")
    )
    
    show_example(
        "Ajoutez une case à cocher pour basculer des options.",
        """
        agree = st.checkbox("J'accepte les termes et conditions")
        """,
        lambda: st.checkbox("J'accepte les termes et conditions")
    )
    
    show_example(
        "Sélectionnez une option parmi un groupe à l'aide de boutons radio.",
        """
        choice = st.radio("Choisissez une option :", ["Option 1", "Option 2", "Option 3"])
        """,
        lambda: st.radio("Choisissez une option :", ["Option 1", "Option 2", "Option 3"])
    )
    
    show_example(
        "Utilisez un curseur pour choisir une valeur numérique.",
        """
        value = st.slider("Choisissez une valeur :", 0, 100, 50)
        """,
        lambda: st.slider("Choisissez une valeur :", 0, 100, 50)
    )

# Onglet Médias
with tabs[2]:
    st.header("Médias")
    
    show_example(
        "Affichez une image avec une légende facultative.",
        """
        st.image("https://via.placeholder.com/300", caption="Image Exemple")
        """,
        lambda: st.image("https://via.placeholder.com/300", caption="Image Exemple")
    )
    
    show_example(
        "Lisez un fichier audio directement dans l'application.",
        """
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
        """,
        lambda: st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    )
    
    show_example(
        "Intégrez une vidéo que les utilisateurs peuvent lire.",
        """
        st.video("https://www.w3schools.com/html/mov_bbb.mp4")
        """,
        lambda: st.video("https://www.w3schools.com/html/mov_bbb.mp4")
    )

# Onglet Mises en Page
with tabs[3]:
    st.header("Mises en Page")
    
    show_example(
        "Créez des mises en page côte à côte à l'aide de colonnes.",
        """
        col1, col2 = st.columns(2)
        with col1:
            st.write("Ceci est la colonne 1")
        with col2:
            st.write("Ceci est la colonne 2")
        """,
        lambda: (
            st.columns(2)[0].write("Ceci est la colonne 1"),
            st.columns(2)[1].write("Ceci est la colonne 2"),
        )
    )
    
    show_example(
        "Ajoutez des sections repliables avec des expanseurs.",
        """
        with st.expander("Développez pour plus d'infos"):
            st.write("Ceci est à l'intérieur d'un expandeur.")
        """,
        lambda: st.expander("Développez pour plus d'infos").write("Ceci est à l'intérieur d'un expandeur.")
    )


# Onglet Autres Outils
with tabs[4]:
    st.header("Autres Outils Utiles")
    
    show_example(
        "Affichez une barre de progression pour les tâches.",
        """
        st.progress(70)
        """,
        lambda: st.progress(70)
    )

    
    show_example(
        "Affichez un spinner pendant l'attente d'une tâche.",
        """
        with st.spinner("Chargement..."):
            st.success("Tâche terminée !")
        """,
        # Utilisation correcte : pas de lambda nécessaire, exécuter directement avec le bloc
        lambda: (
            st.spinner("Chargement..."),
            st.success("Tâche terminée !")
        )
    )
    
    show_example(
        "Affichez des messages d'erreur, d'avertissement ou d'information.",
        """
        st.error("Ceci est un message d'erreur.")
        st.warning("Ceci est un message d'avertissement.")
        st.info("Ceci est un message informatif.")
        """,
        lambda: (
            st.error("Ceci est un message d'erreur."),
            st.warning("Ceci est un message d'avertissement."),
            st.info("Ceci est un message informatif.")
        )
    )
