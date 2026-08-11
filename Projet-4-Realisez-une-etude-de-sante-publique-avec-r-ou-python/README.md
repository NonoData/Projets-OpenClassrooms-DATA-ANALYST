# Étude sur l'Alimentation et la Sous-Nutrition dans le Monde

## 📌 À propos du projet
Ce projet est une **étude data analytique approfondie** de la situation alimentaire mondiale, réalisée par **Arnaud Meloen** à partir des données de la **FAO** (*Food and Agriculture Organization* / Organisation des Nations Unies pour l'alimentation et l'agriculture).

L'objectif principal est de comprendre les mécanismes de la **sous-nutrition à l'échelle globale**, d'analyser la disponibilité des ressources alimentaires et d'étudier la répartition et l'utilisation des récoltes (notamment les céréales et le manioc) afin d'identifier les causes profondes de la faim dans le monde.

---

## 🎯 Enjeux & Problématique
Malgré une production agricole mondiale en croissance constante, l'insécurité alimentaire demeure un fléau majeur. Ce projet cherche à répondre aux questions fondamentales suivantes :

1. **Capacité globale :** La planète produit-elle suffisamment de nourriture pour alimenter toute la population mondiale ?
2. **Répartition & Inégalités :** Quels sont les pays et régions les plus durement touchés par la sous-nutrition et comment se répartit la disponibilité alimentaire ?
3. **Usage de la production :** Quelle est la proportion des récoltes dédiée directement à la nourriture humaine par rapport à l'alimentation animale, aux traitements industriels ou aux pertes ?
4. **Focus cas d'étude (Le paradoxe du manioc en Thaïlande) :** Comment un pays exportateur net de nourriture peut-il en même temps compter une part significative de sa population en état de sous-nutrition ?

---

## 📊 Données utilisées
Les données exploitées proviennent des bases de données officielles de la FAO (période d'étude principale autour de **2013-2017**) et s'articulent autour de 4 axes majeurs :

- **Population :** Nombre d'habitants par pays (ex. ~7,5 milliards d'humains en 2017).
- **Sous-nutrition :** Nombre et proportion de personnes sous-alimentées par pays.
- **Disponibilité alimentaire :** Quantités d'aliments disponibles par habitant en kilocalories (kcal/personne/jour), protéines et graisses.
- **Aide alimentaire :** Volumes de denrées acheminées aux pays en crise (en tonnes).

---

## 🛠️ Méthodologie
L'analyse a été conduite en 4 grandes étapes :

1. **Découverte des données :** Prise en main des fichiers FAO, lecture du cahier des charges et contextualisation géopolitique et économique.
2. **Nettoyage & Préparation :** Traitement des valeurs manquantes (nulles), conversion et standardisation des unités (tonnes, kg, kcal).
3. **Analyse & Calcul d'indicateurs :**
   - Calcul de la capacité théorique d'alimentation globale (base : *2500 kcal / jour / personne*).
   - Bilan de la disponibilité intérieure et de la répartition par type d'usage.
   - Évaluation de la répartition des céréales (alimentation humaine vs animale vs autres).
   - Analyse comparative des pays les plus/moins dotés.
4. **Mise en forme & Visualisation :** Création de graphiques explicitants (camemberts, diagrammes en barres, courbes d'évolution) pour rendre les résultats accessibles.

---

## 📈 Principaux Résultats & Chiffres Clés

### 1. Vue globale (2017)
- **7,10 %** de la population mondiale était en état de sous-nutrition (soit **535 millions de personnes** sur 7,5 milliards).
- **Capacité de production théorique :**
  - La disponibilité totale permettait de nourrir **8,37 milliards de personnes** (> 7,54 milliards de la population mondiale de l'époque).
  - La seule disponibilité en produits végétaux permettait de nourrir **6,90 milliards de personnes**.

### 2. Utilisation de la disponibilité intérieure
Sur l'ensemble des disponibilités alimentaires mondiales :
- **49 %** Nouveaux usages / Nourriture humaine (4 876 Mt)
- **22 %** Traitement industriel (2 205 Mt)
- **13 %** Alimentation animale (1 304 Mt)
- **9 %** Autres utilisations (865 Mt)
- **5 %** Pertes (453 Mt)
- **2 %** Semences (154 Mt)

> **Céréales :** Plus de **1/3 (36 %)** de la production de céréales est destinée à l'alimentation animale, contre **43 %** pour la nourriture humaine (le reste allant aux pertes/semences/traitements). Certaines céréales comme le maïs (57 %), l'orge (66 %) ou l'avoine (69 %) sont majoritairement consommées par le bétail.

### 3. Inégalités & Aide Alimentaire
- **Pays les plus touchés par la sous-nutrition (2017) :** Haïti (48,3 %), République populaire démocratique de Corée (47,2 %), Madagascar (41,1 %), Libéria (38,3 %), Lesotho (38,2 %).
- **Principaux bénéficiaires de l'aide alimentaire (2013-2016) :** République arabe syrienne (1,86 Mt), Éthiopie (1,38 Mt), Yémen (1,21 Mt), Soudan du Sud, Soudan.
- **Facteurs aggravants :** Conflits armés/guerres civiles, instabilités politiques, sécheresses et blocus économiques.

### 4. Focus : Le paradoxe de la Thaïlande
- En 2017, la Thaïlande comptait **6,2 millions de personnes en sous-nutrition** (9 % de sa population).
- Dans le même temps, le pays produisait une quantité massive de **manioc**, capable à elle seule de couvrir les besoins caloriques de **37,2 millions de personnes**.
- **83,4 %** du manioc produit en Thaïlande était **exporté**, tandis que seulement **2,9 %** servait de nourriture locale directe.

---

## 💡 Conclusion
1. **La production alimentaire mondiale est largement suffisante** pour nourrir l'ensemble de l'humanité.
2. La faim et la sous-nutrition ne découlent pas d'un manque de nourriture global, mais d'un **accès inégal aux ressources** et d'une **répartition inéquitable des richesses**.
3. L'aide alimentaire permet d'amortir les crises d'urgence, mais ne constitue qu'une **solution temporaire**.
4. Des **réformes structurelles** sur le commerce agricole, la souveraineté alimentaire et la gestion des cultures d'exportation sont indispensables pour éradiquer la sous-nutrition.
