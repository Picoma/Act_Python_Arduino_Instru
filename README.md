# Activité : Communication entre Python et Arduino : 

Prototype d'activité visant à faire communiquer, **dans le but de réaliser une prise de mesure**.

# Pourquoi cette activité ?

**TL;DR** : Car l'informatique est une science à part entière, que l'on s'en rende compte ou pas.

-----------

Au cours de mon expérience dans l'enseignement, une question récurrente que l'on me posait était "Pourquoi enseigne-t-on Python aux élèves ? On arrivait très bien à enseigner la physique sans, avant." 

Une réponse possible, ma préférée, est la suivante : l'informatique s'inscrit désormais dans le champ de connaissances et le patrimoine humain ; elle possède sa propre science, ses domaines d'applications, ses conséquences économiques et philosophiques ; elle influence la littérature (cf. William Gibson), les arts (cf. les générateurs d'images basés sur des réseaux de neurones, comme Stable Diffusion),... .

En ce sens, ce patrimoine doit être transféré aux nouvelles générations ; c'est le sens des institutions éducatives.

-----------

Cette activité est une application particulière de l'informatique dans le domaine de la physique : l'**instrumentation**. La plupart des appareils de mesure modernes (même ceux utilisés en classe !) possèdent au moins un petit logiciel (appelé microcode), mais peu d'élèves (et de gens, en général...) en ont conscience.

C'est bien cette prise de conscience qui est visée ici : les élèves ont a disposition le microcode téléversé sur l'Arduino (même s'il n'est pas prévu de le modifier ; mais l'élève curieux souhaitera le voir !), et peuvent interagir avec lui via un protocole simple.
Puis, partant de ces interactions élémentaires, il pourra construire une interaction plus complexe : la mise en place d'une chaine de mesure automatisée.

# Utilisation
Je suppose qu'un environnement Python existe et fonctionne ; de même pour Arduino.

Pour mettre en place l'activité :

- En amont :
  1. Installer les dépendances sur les ordinateurs des élèves :
    - `pyserial`
    - `notebook` (paquet pour le notebook Jupyter ; probablement déjà installé et utilisable par les élèves)
- Pendant la séance :
  2. Brancher les Arduinos aux ordinateurs des élèves ; téléverser le code `Code Arduino/sketch/sketch.ino`
  3. Lancer Jupyter Notebook, et ouvrir le notebook `Code Python/Presentation.ipynb`
  4. Suivre les consignes du notebook.
