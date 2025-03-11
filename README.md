# 📊 Application d'analyse Euromillions avec Streamlit

Ce projet Python utilise **Streamlit** pour offrir une analyse approfondie et interactive des résultats de l'Euromillions. L'application permet de visualiser des statistiques complètes sur les numéros et étoiles tirés historiquement, ainsi que de générer des grilles optimisées à partir des données analysées.

## 🚀 Fonctionnalités

- **Chargement automatique** de plusieurs fichiers CSV contenant les résultats de l'Euromillions.
- **Statistiques détaillées** des numéros et étoiles les plus fréquemment et les moins fréquemment tirés.
- **Identification des paires** de numéros les plus fréquentes.
- **Visualisations interactives** (graphes et tableaux clairs).
- **Génération de grilles optimisées** selon différentes stratégies :
  - **Numéros et étoiles les plus chauds** (tirés fréquemment)
  - **Numéros et étoiles les plus froids** (tirés rarement)
  - **Grilles avec les meilleures probabilités** (combinaison élargie des numéros les plus fréquents)

## 📂 Structure du projet

- `app.py`: Le fichier principal contenant l'application Streamlit.
- Dossier `in`: Contient les fichiers CSV des résultats Euromillions à analyser.

## ⚙️ Comment l'utiliser ?

1. Clone le projet :
```bash
git clone <url-de-ton-projet>
cd <nom-du-dossier>
```

2. Installe les dépendances :
```bash
pip install streamlit pandas
```

3. Lance l'application :
```bash
streamlit run app.py
```

4. Ouvre ton navigateur à l'URL indiquée par Streamlit (généralement `http://localhost:8501`).

5. Indique le chemin du dossier contenant tes fichiers CSV et clique sur **"Charger et analyser"**.

## 📈 Exemple de visualisations disponibles :
- Fréquences globales des numéros et étoiles
- Numéros et étoiles chauds/froids
- Paires fréquentes

## 🔮 Génération de grilles optimisées
Trois stratégies proposées :

- **Grilles Chaudes** : Basées sur les numéros et étoiles les plus fréquents historiquement.
- **Grilles Froides** : Basées sur les numéros et étoiles les moins fréquents historiquement.
- **Meilleures Probabilités** : Combinaison des numéros les plus fréquents pour maximiser statistiquement les chances.

---

**✨ Bonne analyse et bonne chance ! ✨**

