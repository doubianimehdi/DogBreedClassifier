# Description du contexte du projet
Votre mission
L'association vous demande de réaliser un algorithme de détection de la race du chien sur une photo, afin d'accélérer leur travail d’indexation.

Vous avez peu d’expérience sur le sujet, vous décidez donc de contacter un ami expert en classification d’images.

Il vous conseille dans un premier temps de pré-processer des images avec des techniques spécifiques (e.g. whitening, equalization, éventuellement modification de la taille des images) et de réaliser de la data augmentation (mirroring, cropping...).

Ensuite, il vous incite à mettre en œuvre deux approches s’appuyant sur l’état de l’art et l’utilisation de CNN (réseaux de neurones convolutionnels), que vous comparerez en termes de temps de traitement et de résultat :

Une première en réalisant votre propre réseau CNN, en vous inspirant de réseaux CNN existants. Prenez soin d'optimiser certains hyperparamètres (des layers du modèle, de la compilation du modèle et de l’exécution du modèle)
Une deuxième en utilisant le transfer learning, c’est-à-dire en utilisant un réseau déjà entraîné, et en le modifiant pour répondre à votre problème.
Concernant le transfer learning, votre ami vous précise que :

Une première chose obligatoire est de réentraîner les dernières couches pour prédire les classes qui vous intéressent seulement.
Il est également possible d’adapter la structure (supprimer certaines couches, par exemple) ou de réentraîner le modèle avec un très faible learning rate pour ajuster les poids à votre problème (plus long) et optimiser les performances.

# Classification automatique d'images de chiens

**Description du projet**:
Une association de protection des animaux a une base de données de pensionnaires qui commence à s'agrandir et ils n'ont pas 
toujours le temps de référencer les images des animaux qu'ils ont accumulées depuis plusieurs années. 
Ils aimeraient donc réaliser un index de l'ensemble de la base de données d'images, pour classer les chiens par races.

**Données**:
* [Stanford Dogs Dataset](http://vision.stanford.edu/aditya86/ImageNetDogs/): 
Contient plus de 20 000 photos de chiens, réparties sur 120 races différentes. 

**Livrables**:

*Notebooks*:
* [1_1_Size](1_1_Size.ipynb) et [1_2_Data_resizing](1_2_Data_resizing.ipynb): Re-dimensionnement des images à la même taille
* [2_Filters](2_Filters.ipynb): Etude de l'effet de différents filtres
* [3_1_SIFT_2_breeds](3_1_SIFT_2_breeds.ipynb), [3_2_SIFT_3_breeds](3_2_SIFT_3_breeds.ipynb) et [3_3_SIFT_5_breeds](3_3_SIFT_5_breeds.ipynb)
: Approche classique avec la méthode SIFT pour une classification sur 2, 3 ou 5 races
* [4_1_CNN_from_scratch](4_1_CNN_from_scratch.ipynb): Approche deep learning avec un réseau neuronal convolutif (CNN) sans pré-entraînement
* [4_2_Transfer_learning_1](4_2_Transfer_learning_1.ipynb), [4_3_Transfer_learning_2](4_3_Transfer_learning_2.ipynb) 
et [4_4_Transfer_learning_3](4_4_Transfer_learning_3.ipynb): Utilisation d'un réseau pré-entraîné (transfer learning) pour améliorer 
les performances de classification

*Code*:
* [classify_120](classify_120.py): Programme de classification parmi 120 races
* [utils](utils.py): Liste de fonctions utilitaires

Pour faire tourner ces programmes il faut aussi télécharger le modèle complet de (poids+modèle) neurones utilisés. Ils sont disponibles ici:
[Modèle à utiliser (120 races)](https://drive.google.com/open?id=1h9ZCmRurpXnjzICHjfRq_oBT1u2edNHa)

* Le fichier 'classes_encoding_120' sert de table de correspondance entre un id et le nom d'une race

*Autres*:
* [Dog Breed Recognition](Dog Breed Recognition.pdf): Support de présentation en fin de projet

