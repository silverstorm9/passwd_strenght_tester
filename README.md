# passwd_strenght_tester

**Description**

Cet outil codé sous Python 3.8.3 permet de calculer la complexité ainsi que la force d'un mot de passe selon sa composition en caractères et sa longueur.

**Installation**

L'outil s'installe via la commande :
`git clone https://github.com/silverstorm9/passwd_strenght_tester.git`

**Utilisation**

Lancer le fichier main.py

`cd passwd_strenght_tester/`

`python3 ./main.py`

Entrer un mot de passe, à savoir qu'il est noté en clair puis le résultat s'affiche :

```
password > test

Lenght : 4
Possible characters : ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Number of possible characters : 26
Complexity : 456976 (=26^4)
Strenght : 19 bits (2^18 <= 456976 < 2^19)
```
