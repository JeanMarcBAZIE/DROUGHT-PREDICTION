# Drought Prediction Project

Ce projet a pour objectif de prédire les épisodes de sécheresse au Sahel, particulièrement au Burkina Faso, en utilisant des données climatiques et des algorithmes de Machine Learning. À travers une analyse approfondie des données météorologiques et climatiques, ce projet vise à fournir des outils de prévision pour anticiper les périodes de sécheresse, un enjeu crucial pour les régions affectées par le changement climatique.

## Structure du Projet

Le projet est structuré en plusieurs notebooks, chacun représentant une étape clé du pipeline de données, depuis le traitement des données brutes jusqu'à l’entraînement et l’évaluation de modèles de Machine Learning.

## Notebooks dans le Dossier `script`

1. ### `1_fusion_plu_etp.ipynb`
   - **Objectif** : Préparer les données de pluie et d’évapotranspiration pour chaque station météorologique.
   - **Étapes principales** :
     - **Import et transformation des données** : Les données sont importées depuis des fichiers Excel, puis transformées pour standardiser leur format. Les noms des stations sont uniformisés pour faciliter les analyses ultérieures.
     - **Création d'une série temporelle** : Les colonnes `Annee`, `Mois` et `Jour` sont combinées pour créer une colonne de date exploitable en tant qu'index temporel, essentielle pour l’analyse séquentielle.
   - **Résultat attendu** : Un DataFrame de données de pluie prêt à être utilisé dans l’analyse de la saisonnalité et des indices de sécheresse.

2. ### `2_saison_pluie.ipynb`
   - **Objectif** : Déterminer la période des saisons des pluies pour chaque station et chaque année.
   - **Méthodologie** :
     - **Détection de la saison des pluies** : Selon la méthode de Dr. SALACK et al., les jours de début et de fin de la saison des pluies sont identifiés pour chaque station, en fonction des seuils de précipitation.
     - **Étiquetage temporel** : Chaque jour est marqué comme étant dans la saison des pluies ou non, avec une catégorisation par décennie, trimestre et semestre.
   - **Résultat attendu** : Un DataFrame indiquant pour chaque jour s’il appartient à la saison des pluies, permettant d’analyser les variations saisonnières de la pluie.

3. ### `3_drought_index.ipynb`
   - **Objectif** : Calculer et catégoriser les indices de sécheresse (SPEI) pour évaluer l’intensité de la sécheresse.
   - **Étapes principales** :
     - **Transformation et transposition** : Les données de sécheresse sont transposées pour faciliter la visualisation.
     - **Catégorisation de la sécheresse** : Les indices sont classés en catégories (extrême, sévère, modérée, etc.) et étiquetés pour chaque station et chaque jour.
   - **Résultat attendu** : Un DataFrame prêt pour la visualisation et l’analyse des périodes de sécheresse selon leur intensité, pour chaque station.

4. ### `4_download_Era5_decadaire.ipynb`
   - **Objectif** : Télécharger les données climatiques ERA5 à une échelle temporelle de 10 jours.
   - **Méthodologie** :
     - **Téléchargement via CDS API** : Les données ERA5 sont récupérées pour différentes zones géographiques (Burkina Faso, océans) pour les périodes et les variables climatiques d'intérêt.
     - **Gestion des téléchargements parallèles** : Un pool de threads est utilisé pour accélérer les téléchargements en parallèle.
   - **Résultat attendu** : Les fichiers NetCDF contenant les données climatiques brutes, disponibles pour l’étape de traitement.

5. ### `5_processing_ERA5_data.ipynb`
   - **Objectif** : Traiter et organiser les données ERA5 pour qu’elles soient prêtes à être analysées et utilisées dans les modèles.
   - **Étapes principales** :
     - **Concaténation des fichiers NetCDF** : Les fichiers sont combinés en une seule série temporelle.
     - **Gestion des valeurs manquantes** : Les données manquantes sont remplacées pour assurer la continuité de la série.
   - **Résultat attendu** : Deux ensembles de données consolidées (décadaires et mensuels) pour une analyse climatique et météorologique.

6. ### `6_final_dataframe.ipynb`
   - **Objectif** : Intégrer les différents datasets traités en un seul dataset final pour l’apprentissage des modèles.
   - **Étapes** :
     - **Normalisation et étiquetage** : Les variables sont normalisées et les valeurs manquantes sont gérées pour éviter les biais dans l’entraînement des modèles.
     - **Calcul de moyennes roulantes** : Des moyennes mobiles sont calculées pour capturer les tendances dans les séries temporelles.
   - **Résultat attendu** : Un dataset complet et nettoyé, combinant toutes les variables climatiques, prêt pour l’entraînement des modèles.

7. ### `7_training_model.ipynb`
   - **Objectif** : Entraîner des modèles de Machine Learning pour prédire la sécheresse.
   - **Méthodologie** :
     - **Séparation des données** : Les données sont divisées en ensembles d’entraînement et de test.
     - **Entraînement de différents modèles** : Divers modèles, incluant Random Forest, Gradient Boosting, et RNN (LSTM), sont testés pour identifier les meilleures performances.
     - **Évaluation des modèles** : Les modèles sont évalués avec des métriques adaptées aux données déséquilibrées.
   - **Résultat attendu** : Des modèles entraînés et évalués, prêts pour des prédictions sur de nouvelles données.

8. ### `8_gestion_fichier_resultat.ipynb`
   - **Objectif** : Organiser et sauvegarder les résultats des modèles pour une analyse approfondie.
   - **Étapes** :
     - **Organisation des fichiers de résultats** : Les résultats sont stockés dans des répertoires spécifiques, et des formats compatibles avec LaTeX sont générés pour faciliter la présentation.
   - **Résultat attendu** : Un ensemble de fichiers bien structurés et organisés pour l’analyse des performances et la présentation des résultats finaux.

## Installation et Utilisation

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/JeanMarcBAZIE/DROUGHT-PREDICTION.git
