# Tableau de Bord Power BI : Stratégie Produit & Suivi de Projet (Gantt)

## 📌 À propos du projet

Ce projet est une solution décisionnelle et analytique développée sous **Power BI** (`.pbix`). Elle a été conçue pour offrir une **vision à 360 degrés** de la planification stratégique et opérationnelle d'un portefeuille de projets. 

Il combine deux piliers majeurs du pilotage d'entreprise :
1. **Le Produit & la Stratégie (Product Strategy Canvas)** : Définition des objectifs macroscopiques, ciblage des opportunités, proposition de valeur et jalons stratégiques.
2. **Le Suivi Temporel & Opérationnel (Diagramme de Gantt)** : Suivi détaillé de l'avancement des tâches, de la chronologie des livrables, de l'allocation des ressources et de la gestion des délais.

Ce tableau de bord s'adresse aussi bien à la **direction générale**, aux **Product Managers**, aux **Chefs de Projet** qu'aux **équipes opérationnelles**.

---

## 🎯 Contexte et Enjeux

### 1. Le Contexte
Dans des environnements projets complexes ou multi-projets, les équipes font souvent face à un manque de visibilité unifiée entre la **stratégie globale** (la feuille de route / la vision produit) et l'**exécution tactique au quotidien** (qui fait quoi, quand et avec quel retard éventuel).

### 2. Les Enjeux Clés
* **Alignement Stratégique & Opérationnel** : S'assurer que chaque tâche du planning répond directement aux objectifs stratégiques définis dans le *Product Strategy Canvas*.
* **Gestion Proactive des Délais** : Identifier les goulets d'étranglement, les chevauchements critiques de ressources et les retards sur le chemin critique grâce à un visualiseur Gantt interactif.
* **Transparence et Communication** : Centraliser l'information dans un rapport unique et interactif pour éviter la dispersion des données dans des tableurs obsolètes.
* **Prise de Décision Basée sur la Donnée** : Exploiter un modèle de données structuré et des mesures DAX sur mesure pour évaluer la performance globale (taux de complétion, respect des jalons, charge de travail).

---

## 📊 Données Utilisées et Modèle de Données

Le rapport s'appuie sur une structure de données relationnelle intégrant plusieurs tables de données opérationnelles et de référentiels :

### 1. Modèle de Données (Data Model)
* **Table des Tâches / Projets (`Tasks` / `Projects`)** :
  * ID Projet / Tâche
  * Nom de la tâche / du livrable
  * Date de début & Date de fin (prévues et réelles)
  * Statut (*Non démarré*, *En cours*, *Terminé*, *En retard*)
  * Pourcentage d'avancement (%)
  * Responsables / Attributaires
* **Table Référentiel Temps (`Calendar` / `Date`)** :
  * Table de dates continue pour permettre l'analyse temporelle dynamique, le filtrage par année, trimestre, mois ou semaine.
* **Table de Stratégie Produit (`Product_Strategy`)** :
  * Objectifs clés, segments cibles, indicateurs clés de performance (KPIs) associés au Canva Stratégique.

### 2. Mesures & Calculs DAX (`DAXQueries`)
Le projet intègre des formules **DAX (Data Analysis Expressions)** dédiées à la mesure exacte de la performance :
* **Taux d'avancement global** (moyenne pondérée du pourcentage de réalisation).
* **Nombre de projets / tâches en retard** (comparaison dynamique entre la date de fin prévue et la date du jour).
* **Écart de calendrier (Variance)** : calcul du retard moyen exprimé en jours.
* **Indicateurs de statut** permettant la mise en forme conditionnelle (alertes visuelles vert/orange/rouge).

---

## 🎨 Composants Visuels du Tableau de Bord

Le rapport contient plusieurs visuels et fonctionnalités clés :

1. **Visuel Personnalisé Gantt (Custom Visual Gantt Chart)**
   * Permet la représentation graphique du calendrier du projet.
   * Visualisation des barres d'avancement, des dépendances entre tâches et des jalons principaux.
   * Filtrage dynamique par projet, membre d'équipe ou statut.

2. **Canvas de Stratégie Produit (Product Strategy Canvas)**
   * Intégration visuelle du cadre stratégique du projet (`Product_Strategy_Canva`).
   * Permet de contextualiser les données quantitatives avec les enjeux business et la vision produit.

3. **Indicateurs Clés de Performance (KPI Cards)**
   * Nombre total de tâches.
   * Taux de réalisation global.
   * Nombre de tâches critiques ou en retard.

4. **Filtres Dynamiques (Slicers)**
   * Filtrage par plage de dates.
   * Filtrage par responsable / département.
   * Filtrage par niveau de priorité ou phase du projet.

---

## 🏗️ Structure Technologique du Fichier (`.pbix`)

Le projet Power BI est structuré sous forme d'une archive décompressée comprenant les éléments techniques suivants :

```text
├── [Content_Types].xml        # Définition des types de contenus du package Power BI
├── DataModel                  # Modèle de données compressé (Moteur VertiPaq)
├── SecurityBindings           # Paramètres de sécurité et autorisations
├── DAXQueries/                # Requêtes et scripts DAX personnalisés
│   ├── .pbi/daxQueries.json
│   └── Requête 1.dax
├── Report/                    # Structure visuelle du rapport
│   ├── Layout                 # Disposition visuelle, filtres et connecteurs
│   ├── LinguisticSchema       # Schéma linguistique pour les questions/réponses (Q&A)
│   ├── Settings               # Configuration globale du rapport
│   ├── Metadata               # Métadonnées du projet
│   ├── CustomVisuals/         # Visuals personnalisés intégrés
│   │   └── Gantt1448688115699/ # Module du visuel Gantt (package & config JSON)
│   └── StaticResources/       # Ressources graphiques enregistrées
│       ├── RegisteredResources/
│       │   ├── Product_Strategy_Canva...png  # Image du Canvas de Stratégie Produit
│       │   └── Sans_titre_...bmp
│       └── SharedResources/
│           └── BaseThemes/     # Thème graphique et charte de couleurs (CY26SU02)
```

---

## 🚀 Guide de Prise en Main et Utilisation

### Prérequis
* **Power BI Desktop** (version récente recommandée) pour ouvrir, modifier et publier le fichier `.pbix`.
* Accès aux sources de données sous-jacentes (Base de données, fichier Excel, SharePoint ou flux OData) si un rafraîchissement des données est nécessaire.

### Procédure d'Ouverture
1. Si vous disposez du fichier réempaqueté `.pbix`, double-cliquez dessus pour l'ouvrir directement dans **Power BI Desktop**.
2. Si vous explorez le dossier extrait :
   * Recompilez le dossier au format `.pbix` ou importez les requêtes DAX et le modèle de données dans votre environnement Power BI.

### Consultation du Rapport
* **Navigation** : Utilisez les onglets du rapport pour passer de la **Vue Stratégique** (Canvas) à la **Vue Opérationnelle** (Planning Gantt).
* **Interactivité** : Cliquez sur un élément d'un visuel (par exemple une barre du Gantt ou un statut dans une carte) pour filtrer automatiquement l'ensemble du tableau de bord.
* **Export & Partage** : Publiez le rapport sur le **Power BI Service** pour autoriser le partage avec les parties prenantes et configurer les rafraîchissements automatiques.

---

## 🔮 Évolutions Futures et Améliorations Envisagées

* **Ajustement de la charge de travail (Resource Leveling)** : Intégration d'un visuel de suivi de la capacité/charge des collaborateurs.
* **Connexion en Temps Réel** : Mise en place d'un connecteur automatique vers un outil de gestion de projet type Jira, Azure DevOps ou Asana.
* **Scénarios What-If** : Ajout de paramètres DAX pour simuler l'impact d'un retard de livraison sur la date d'atterrissage globale du projet.

---

## 📝 Licence & Auteurs

* **Projet** : Tableau de bord de pilotage stratégique & Gantt
* **Technologie** : Power BI Desktop / DAX / Power Query
* **Support & Maintenance** : Équipe Analytics & Direction de Projet
