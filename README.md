# Cryptanalyse de RSA


Ce dépôt rassemble les implémentations réalisés dans le cadre de mon **TIPE** (Travail d'Initiative Personnelle Encadré) portant sur la sécurité du chiffrement asymétrique RSA. L'objectif de cette étude est d'analyser et d'évaluer la robustesse de RSA face à différentes vulnérabilités mathématiques et structurelles.

---

## 🔬 Problématique et Objectifs du TIPE

> **Problématique :** Dans quelles conditions le chiffrement RSA peut-il être compromis, et quelles sont les attaques les plus efficaces contre sa sécurité ?

Le projet s'articule autour de quatre axes majeurs :
1. **Implémentation du cœur RSA** (génération de clés sur 512 bits via des tests de primalité probabilistes, chiffrement, déchiffrement).
2. **Étude et développement de trois attaques majeures** ciblant des faiblesses distinctes du cryptosystème.
3. **Analyse comparative** des performances et du temps d'exécution des algorithmes de cryptanalyse.
4. **Déduction des contre-mesures** concrètes pour sécuriser l'implémentation de RSA.

---

## 🛠️ Architecture du Code & Attaques Étudiées

Le projet est modulaire et se divise en plusieurs scripts Python :

### 1. Génération et Utilitaires (`utilitaires.py`, `main.py`)
* **Test de primalité de Miller-Rabin :** Permet de certifier de grands nombres premiers de manière probabiliste avec une probabilité d'erreur négligeable.
* **Algorithme d'Euclide étendu :** Utilisé pour calculer l'identité de Bézout et l'inverse modulaire nécessaire à la création du couple de clés.
* **Génération de clés :** Production de clés publiques $(e, N)$ et privées $(d, N)$.

### 2. Attaque de Håstad (`Hastad.py`) – *Faiblesse de l'exposant public*
* **Principe :** Cette attaque s'appuie sur le **Théorème des Restes Chinois**. Si un même message est envoyé à plusieurs destinataires (au moins $e$) possédant des modules $N_i$ premiers entre eux avec un petit exposant public $e$ (ex: $e = 7$), le message peut être intercepté et déchiffré sans connaître les clés privées.

### 3. Attaque $p-1$ de Pollard (`Pollard.py`) – *Faiblesse de la factorisation*
* **Principe :** Cet algorithme permet de factoriser le module $N = p \times q$ si l'un des facteurs premiers (par exemple $p-1$) est **lisse**, c'est-à-dire s'il est composé uniquement de petits facteurs premiers. Dès que le PGCD entre $a^{B!} - 1$ et $N$ devient strictement supérieur à 1, la structure du module s'effondre.

### 4. Attaque de Wiener (`Wiener.py`) – *Faiblesse de l'exposant privé*
* **Principe :** Fondée sur le développement en **fractions continues** de $\frac{e}{N}$. Elle permet de retrouver efficacement la clé secrète $d$ si celle-ci est trop petite par rapport au module, plus précisément lorsque :
  $$d < \frac{1}{3}N^{\frac{1}{4}}$$

---

## 🚀 Utilisation et Tests

### Prérequis
Avoir Python 3 installé avec ses bibliothèques standards (`math`, `time`, `random`).

### Lancement des simulations
Le fichier `main.py` fait office de point d'entrée global pour tester le bon fonctionnement de la génération des clés ainsi que les performances de l'attaque d'Håstad. On pourra modifier le fichier `main.py` pour tester les deux autres attaques.

```bash
python3 main.py
```
