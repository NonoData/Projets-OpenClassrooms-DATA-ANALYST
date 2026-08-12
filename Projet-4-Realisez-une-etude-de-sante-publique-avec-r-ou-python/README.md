# 🍴 Étude sur l'Alimentation et la Sous-Nutrition dans le Monde

## À propos du projet
Ce projet est une **étude data analytique approfondie** de la situation alimentaire mondiale à partir des données de la **FAO** (*Food and Agriculture Organization* / Organisation des Nations Unies pour l'alimentation et l'agriculture).

L'objectif principal est de comprendre les mécanismes de la **sous-nutrition à l'échelle globale**, d'analyser la disponibilité des ressources alimentaires et d'étudier la répartition et l'utilisation des récoltes (notamment les céréales et le manioc) afin d'identifier les causes profondes de la faim dans le monde.



## Enjeux & Problématique
Malgré une production agricole mondiale en croissance constante, l'insécurité alimentaire demeure un fléau majeur. Ce projet cherche à répondre aux questions fondamentales suivantes :

1. **Capacité globale :** La planète produit-elle suffisamment de nourriture pour alimenter toute la population mondiale ?
2. **Répartition & Inégalités :** Quels sont les pays et régions les plus durement touchés par la sous-nutrition et comment se répartit la disponibilité alimentaire ?
3. **Usage de la production :** Quelle est la proportion des récoltes dédiée directement à la nourriture humaine par rapport à l'alimentation animale, aux traitements industriels ou aux pertes ?
4. **Focus cas d'étude (Le paradoxe du manioc en Thaïlande) :** Comment un pays exportateur net de nourriture peut-il en même temps compter une part significative de sa population en état de sous-nutrition ?



## Données utilisées
Les données exploitées proviennent des bases de données officielles de la FAO (période d'étude principale autour de **2013-2017**) et s'articulent autour de 4 axes majeurs :

- **Population :** Nombre d'habitants par pays (ex. ~7,5 milliards d'humains en 2017).
- **Sous-nutrition :** Nombre et proportion de personnes sous-alimentées par pays.
- **Disponibilité alimentaire :** Quantités d'aliments disponibles par habitant en kilocalories (kcal/personne/jour), protéines et graisses.
- **Aide alimentaire :** Volumes de denrées acheminées aux pays en crise (en tonnes).



## Méthodologie
L'analyse a été conduite en 4 grandes étapes :

1. **Découverte des données :** Prise en main des fichiers FAO, lecture du cahier des charges et contextualisation géopolitique et économique.
2. **Nettoyage & Préparation :** Traitement des valeurs manquantes (nulles), conversion et standardisation des unités (tonnes, kg, kcal).
3. **Analyse & Calcul d'indicateurs :**
   - Calcul de la capacité théorique d'alimentation globale (base : *2500 kcal / jour / personne*).
   - Bilan de la disponibilité intérieure et de la répartition par type d'usage.
   - Évaluation de la répartition des céréales (alimentation humaine vs animale vs autres).
   - Analyse comparative des pays les plus/moins dotés.
4. **Mise en forme & Visualisation :** Création de graphiques explicitants (camemberts, diagrammes en barres, courbes d'évolution) pour rendre les résultats accessibles.
