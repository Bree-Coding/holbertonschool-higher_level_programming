# Python Input/Output 🐍📄

## Description
Ce projet contient des exercices pour pratiquer la gestion des fichiers et les opérations d'entrée/sortie en Python.

## Table des matières
0. Lire un fichier
1. Écrire dans un fichier
2. Ajouter à un fichier
3. Vers une chaîne JSON
4. De la chaîne JSON à l'objet
5. Sauvegarder un objet dans un fichier
6. Créer un objet à partir d'un fichier JSON
7. Charger, ajouter, sauvegarder
8. Classe vers JSON
9. Étudiant vers JSON
10. Étudiant vers JSON avec filtre
11. Étudiant sur disque et recharger
12. Triangle de Pascal

## 0. Lire un fichier 📖
- Prototype : `def read_file(filename=""):`
- Utilise l'instruction `with`
- Ne gère pas les exceptions de permission de fichier ou d'absence de fichier
- Aucun module importé

## 1. Écrire dans un fichier ✍️
- Prototype : `def write_file(filename="", text=""):`
- Utilise l'instruction `with`
- Ne gère pas les exceptions de permission de fichier
- Crée le fichier s'il n'existe pas
- Remplace le contenu du fichier s'il existe déjà
- Aucun module importé

## 2. Ajouter à un fichier ➕
- Prototype : `def append_write(filename="", text=""):`
- Crée le fichier s'il n'existe pas
- Utilise l'instruction `with`
- Ne gère pas les exceptions de permission de fichier ou d'absence de fichier
- Aucun module importé

## 3. Vers une chaîne JSON 🔄
- Prototype : `def to_json_string(my_obj):`
- Ne gère pas les exceptions si l'objet ne peut pas être sérialisé

## 4. De la chaîne JSON à l'objet 🔄
- Prototype : `def from_json_string(my_str):`
- Ne gère pas les exceptions si la chaîne JSON ne représente pas un objet

## 5. Sauvegarder un objet dans un fichier 💾
- Prototype : `def save_to_json_file(my_obj, filename):`
- Utilise l'instruction `with`
- Ne gère pas les exceptions si l'objet ne peut pas être sérialisé
- Ne gère pas les exceptions de permission de fichier

## 6. Créer un objet à partir d'un fichier JSON 📂
- Prototype : `def load_from_json_file(filename):`
- Utilise l'instruction `with`
- Ne gère pas les exceptions si la chaîne JSON ne représente pas un objet
- Ne gère pas les exceptions de permission de fichier

## 7. Charger, ajouter, sauvegarder ➕💾
- Ajoute tous les arguments à une liste Python, puis les sauvegarde dans un fichier
- Utilise les fonctions `save_to_json_file` et `load_from_json_file`
- La liste est sauvegardée en tant que représentation JSON dans un fichier nommé `add_item.json`
- Crée le fichier s'il n'existe pas
- Ne gère pas les exceptions de permission de fichier

## 8. Classe vers JSON 🏫
- Prototype : `def class_to_json(obj):`
- `obj` est une instance d'une classe
- Tous les attributs de la classe `obj` sont sérialisables : liste, dictionnaire, chaîne, entier et booléen
- Aucun module importé

## 9. Étudiant vers JSON 👨‍🎓
- Classe `Student` avec les attributs publics `first_name`, `last_name`, `age`
- Méthode publique `def to_json(self):` qui récupère une représentation en dictionnaire d'une instance de `Student`
- Aucun module importé

## 10. Étudiant vers JSON avec filtre 🔍
- Classe `Student` avec les attributs publics `first_name`, `last_name`, `age`
- Méthode publique 
