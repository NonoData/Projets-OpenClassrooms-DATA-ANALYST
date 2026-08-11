# 📊 Tableau de Bord Power BI — Suivi de Projet & Diagramme de Gantt

Bienvenue sur le répertorie du projet de **Tableau de Bord de Pilotage de Projet & Suivi de Gantt (Power BI)**. 

Ce document a pour objectif de présenter le projet, ses objectifs stratégiques, la structure des données utilisées et son fonctionnement, de manière simple et accessible à tous, même sans expérience préalable en gestion de projet ou en analyse de données.

---

## 🎯 1. Présentation du Projet

### Qu'est-ce que ce projet ?
Ce projet est un **outil d'aide à la décision et de pilotage interactif** conçu sous **Power BI**. Il permet de visualiser en temps réel la progression des différents projets d'une organisation, les étapes clés (jalons), les échéances et l'affectation des ressources.

Grâce à des visuels sur mesure — notamment des **diagrammes de Gantt interactifs** (*Gantt Chart by MAQ Software* et visuels personnalisés) — ce tableau de bord offre une vue d'ensemble claire de l'état de santé de chaque projet.

### Pourquoi avoir développé cet outil ?
Dans une entreprise ou une organisation, plusieurs projets se déroulent souvent en parallèle. Sans outil centralisé :
* Il est difficile de savoir si les projets respectent le planning prévu.
* Les retards sont identifiés trop tard.
* La répartition du travail entre les équipes manque de visibilité.
* La communication entre les chefs de projet, la direction et les équipes métier est parfois complexe.

Ce tableau de bord résout ces problèmes en consolidant toutes les informations au même endroit de façon visuelle et synthétique.

---

## 💡 2. Les Enjeux et Objets Stratégiques

| Enjeu | Description & Impact |
| :--- | :--- |
| **⏱️ Respect des Délais** | Identifier immédiatement les tâches en retard ou à risque afin de réajuster les plannings avant qu'un délai critique ne soit dépassé. |
| **👥 Gestion des Ressources** | Consulter la charge de travail attribuée à chaque personne ou équipe pour éviter la surcharge ou la sous-utilisation. |
| **📈 Transparence & Reporting** | Offrir aux décideurs (direction, comités de pilotage) une vision globale et actualisée de l'avancement sans multiplier les réunions statutaires. |
| **🎯 Suivi des Jalons Étape par Étape** | S'assurer que les livrables clés et phases majeures (ex: conception, développement, validation, déploiement) sont validés dans les temps. |
| **🤝 Alignement des Équipes** | Permettre à chaque membre d'équipe de comprendre sa contribution, ses priorités et les dépendances avec d'autres tâches. |

---

## 🗂️ 3. Origine et Structure des Données Utilisées

Le modèle de données (*DataModel*) sous-jacent centralise les informations essentielles à la conduite de projet. Voici les principales catégories de données exploitées :

### A. Données relatives aux Projets & Phases
* **Identifiant du projet (`Project ID / Name`)** : Nom unique et code de référence de chaque projet.
* **Catégorie / Portefeuille (`Portfolio / Category`)** : Regroupement thématique ou départemental des projets.
* **Statut global (`Project Status`)** : *Non démarré*, *En cours*, *En pause*, *Terminé*, *En retard*.

### B. Données relatives aux Tâches & Planning
* **Nom de la tâche (`Task Name`)** : Libellé de l'action à réaliser.
* **Date de début & Date de fin prévues (`Start Date / End Date`)** : Échéancier initial théorique.
* **Date de fin réelle (`Actual End Date`)** : Date effective de réalisation pour calculer les écarts.
* **Durée & Taux d'avancement (`Duration / % Complete`)** : Pourcentage de réalisation de chaque tâche (de 0% à 100%).
* **Prédécesseurs & Dépendances (`Dependencies`)** : Liens logiques entre les tâches (ex : la tâche B ne peut démarrer que lorsque la tâche A est terminée).

### C. Données sur les Ressources & Équipes
* **Responsable / Assigné à (`Resource / Owner`)** : Personne ou équipe en charge de l'exécution.
* **Rôle / Département (`Role / Dept`)** : Fonction de la ressource dans l'organisation.

---

## 🛠️ 4. Fonctionnalités Principales du Tableau de Bord

1. **Diagramme de Gantt Interactif** :
   * Visualisation chronologique des barres de tâches sur une frise temporelle (jours, semaines, mois).
   * Code couleur selon le statut ou le niveau de risque de la tâche.
   * Indicateur visuel d'avancement au sein de chaque barre de tâche.

2. **Filtres Dynamiques (Slicers)** :
   * Filtrage par projet, chef de projet, période, statut ou département en un seul clic.

3. **Indicateurs Clés de Performance (KPIs)** :
   * Nombre total de projets actifs.
   * Taux moyen d'avancement global.
   * Nombre de projets en retard ou nécessitant une attention immédiate.

---

## 🚀 5. Guide de Prise en Main Rapide

### Prérequis
* **Power BI Desktop** (version récente) pour ouvrir, modifier ou publier le fichier `.pbix`.
* Un navigateur web (Edge, Chrome) pour consulter le rapport s'il est publié sur le service **Power BI Service (Cloud)**.

### Comment utiliser ce rapport ?
1. **Ouvrir le fichier** dans Power BI Desktop ou accéder au lien du rapport en ligne.
2. **Utiliser le panneau de filtres** en haut ou à gauche pour sélectionner le projet ou la période qui vous intéresse.
3. **Consulter le Diagramme de Gantt** pour observer le déroulement temporel et repérer les barres rouges/orange signifiant un retard.
4. **Survoler les éléments (Tooltips)** avec la souris pour afficher les détails d'une tâche (responsable, dates exactes, % d'avancement).

---

## 📝 Glossary / Lexique Simple pour Débutants

* **Diagramme de Gantt** : Graphique en barres horizontales qui illustre le planning d'un projet dans le temps.
* **Jalon (Milestone)** : Événement important ou livraison clé dans un projet (représenté souvent par un losange).
* **Dépendance** : Relation entre deux tâches où le début d'une tâche dépend de la fin d'une autre.
* **Power BI** : Outil d'analyse de données de Microsoft permettant d'afficher des graphiques interactifs.

---

*Ce document README a été généré pour fournir une documentation claire, structurée et accessible à l'ensemble des intervenants du projet.*
