# Classification-Challenge-KNN


## I-  Introduction 

Dans ce projet, notre objectif est d’implémenter un algorithme de Machine Learning KNN en classification pour déterminer les labels du fichier « FinalTest.txt » fourni. 

## II-  Structuration du projet 

Pour ce faire nous avons choisi de structurer notre projet sous forme de deux classes : 

- **Individu :** 

Un individu est composé d’un label et d’une valeur. Dans ce projet les labels des points sont alternativement ‘0’ ou ‘1’. Dans le cas ou le label d’un individu est inconnu (comme dans le fichier « finalTest.txt », ce dernier vaudra ‘unknown’.  

Par ailleurs, dans ce projet la valeur d’un individu est représentée par un vecteur de 9 valeurs, donnant un point dans un espace de dimension 9. On peut donc résumer un individu comme suit : 



- **Knn :** 

La seconde classe de ce projet est en réalité son élément principal. Le constructeur d’un Knn prend en paramètre une matrice d’entrainement (labélisée) et une matrice de test (non- labelisée). Cette implémentation est très ergonomique pour un utilisateur potentiel du fait des différentes fonctions que nous y avons implémentées : 

- **Solve :** 

Renvoie les labels probables selon le modèle des différents points du set de test. 

- **Export :** 

Permet d’enregistrer les labels trouvés dans un fichier texte selon le format imposé par le cahier des charges. 

- **Error :** 

Dans le cas où l’on possède les labels des individus ayant été traités. Cette fonction évaluera l’efficacité du KNN en comparant les labels trouvés aux véritables. Il calculera ainsi la matrice de confusion et le pourcentage d’erreur fait par le programme. 

## III-  Tutorial - Lancer notre programme sur votre poste 

- Ouvrir le fichier « KNN.py » : 
- Se rendre dans le main se situant en bas de page. 
- Dans le main se trouve un paramètre action pouvant prendre 3 valeurs. En fonction de la valeur de ce paramètre, des actions différentes s’exécutent : 
- **Action = « train » :** 

Dans ce cas, le programme va s’effectuer sur les individus labélisé à sa disposition. Il divisera ce groupe d’individu en train et test puis effectuera le KNN. A l’issue de cela, on pourra utiliser la fonction « Error » présentée plus tôt afin de constater la pertinence du modèle sur les données. 

- **Action = « test » :** 

Dans ce cas, le set de train sera consisté de l’ensemble des données labélisés et le set de test, quant à lui, contiendra les individus sans label. Dans ce cas, il sera impossible d’obtenir l’erreur du programme étant donné que les véritables labels ne sont pas connus. 

- **Action = « merge » :** 

Permet de fusionner des fichiers txt. Cette option n’est pas utile à l’utilisateur mais nous à permis d’éprouver notre modèle au travers de tests empiriques. 

IV-  Conclusion 

Pour conclure, nous tenons à discuter des performances de notre modèle. Au travers de nos tests, nous avons remarqué que la répartition entre les points labélisés ‘1’ et ‘0’ n’était pas équitable dans le fichier data. En effet, il y a significativement plus de ‘0’ que de ‘1’. Cette information est d’une extrême importance puisqu’une telle disparité dans les données peut entrainer un biais sur le modèle. 

Pour ce qui est de notre algorithme, ses performances sont répertoriées dans le tableau suivant : 



|Fichier utilisé |Pourcentage d’erreur |
| - | - |
|Data.txt |Entre 20 et 25 % |
|PreTest.txt |Entre 25 et 30 % |
Ces performances indiquent le bon fonctionnement de notre KNN même si ces résultats pourraient très certainement être améliorés avec l’utilisation de modèles plus complexes. 
