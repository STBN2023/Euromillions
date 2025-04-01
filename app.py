import streamlit as st
import pandas as pd
import glob
import random
from itertools import combinations
from collections import Counter

# Fonction pour charger les fichiers CSV
def charger_donnees(chemin):
    fichiers = glob.glob(f"{chemin}/*.csv")
    df_list = []
    for fichier in fichiers:
        df = pd.read_csv(fichier, sep=';')
        df_list.append(df)
    return pd.concat(df_list, ignore_index=True)


# commentaire
# # Traitement des données pour les statistiques
def statistiques(df):
    boules = df[['boule_1', 'boule_2', 'boule_3', 'boule_4', 'boule_5']]
    etoiles = df[['etoile_1', 'etoile_2']]

    numeros_freq = pd.Series(boules.values.flatten()).value_counts().reset_index()
    numeros_freq.columns = ['Numéro', 'Fréquence']

    etoiles_freq = pd.Series(etoiles.values.flatten()).value_counts().reset_index()
    etoiles_freq.columns = ['Étoile', 'Fréquence']

    chauds = numeros_freq.head(10)
    froids = numeros_freq.tail(10).sort_values(by='Fréquence')
    etoiles_chaudes = etoiles_freq.head(5)
    etoiles_froides = etoiles_freq.tail(5).sort_values(by='Fréquence')

    # Paires fréquentes
    pairs_counter = Counter()
    for tirage in boules.values:
        pairs_counter.update(combinations(sorted(tirage), 2))

    paires_freq = pd.DataFrame([(p[0], p[1], c) for p, c in pairs_counter.items()],
                               columns=['Numéro 1', 'Numéro 2', 'Fréquence'])
    paires_freq = paires_freq.sort_values(by='Fréquence', ascending=False).head(10)

    return numeros_freq, chauds, froids, paires_freq, etoiles_freq, etoiles_chaudes, etoiles_froides

# Générer des grilles optimisées
def generer_grilles(selection_nums, selection_etoiles, nombre_grilles=5):
    numeros = selection_nums['Numéro'].tolist()
    etoiles = selection_etoiles['Étoile'].tolist()
    grilles = []
    random.seed()
    for _ in range(nombre_grilles):
        grille_nums = random.sample(numeros, 5)
        grille_nums.sort()
        grille_etoiles = random.sample(etoiles, 2)
        grille_etoiles.sort()
        grilles.append(grille_nums + grille_etoiles)
    return pd.DataFrame(grilles, columns=['Numéro 1', 'Numéro 2', 'Numéro 3', 'Numéro 4', 'Numéro 5', 'Étoile 1', 'Étoile 2'])

# Application Streamlit
st.title("Analyse des résultats Euromillions")

# Initialisation état de session
if 'donnees_chargees' not in st.session_state:
    st.session_state['donnees_chargees'] = False

# Chargement des données
chemin_dossier = st.text_input("Chemin du dossier des fichiers CSV", "./in")

if st.button("Charger et analyser"):
    st.session_state['donnees'] = charger_donnees(chemin_dossier)
    st.session_state['numeros_freq'], st.session_state['chauds'], st.session_state['froids'], st.session_state['paires_freq'], st.session_state['etoiles_freq'], st.session_state['etoiles_chaudes'], st.session_state['etoiles_froides'] = statistiques(st.session_state['donnees'])
    st.session_state['donnees_chargees'] = True

if st.session_state['donnees_chargees']:
    st.header("Fréquence des 20 numéros les plus fréquents")
    st.bar_chart(st.session_state['numeros_freq'].set_index('Numéro').head(20)['Fréquence'])

    st.header("Top 10 des numéros les plus chauds")
    st.table(st.session_state['chauds'])

    st.header("Top 5 des étoiles les plus chaudes")
    st.table(st.session_state['etoiles_chaudes'])

    st.header("Top 10 des numéros les plus froids")
    st.table(st.session_state['froids'])
    
    st.header("Top 5 des étoiles les plus froides")
    st.table(st.session_state['etoiles_froides'])

    st.header("Top 10 des paires les plus fréquentes")
    st.table(st.session_state['paires_freq'])

    st.header("Fréquence des étoiles")
    st.bar_chart(st.session_state['etoiles_freq'].set_index('Étoile'))




    if st.button("Grilles Chaudes"):
        grilles_chaudes_df = generer_grilles(st.session_state['chauds'], st.session_state['etoiles_chaudes'])
        st.header("Grilles Numéros et Étoiles Chaudes")
        st.table(grilles_chaudes_df)

    if st.button("Grilles Froides"):
        grilles_froides_df = generer_grilles(st.session_state['froids'], st.session_state['etoiles_froides'])
        st.header("Grilles Numéros et Étoiles Froides")
        st.table(grilles_froides_df)

    if st.button("Grilles Meilleures Probabilités"):
        top_nums = st.session_state['numeros_freq'].head(20)
        top_etoiles = st.session_state['etoiles_freq'].head(5)
        meilleures_grilles_df = generer_grilles(top_nums, top_etoiles)
        st.header("Grilles avec Meilleures Probabilités")
        st.table(meilleures_grilles_df)