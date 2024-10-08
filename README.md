# JP Morgan Chase & Co. Quantitative Research

Un dépôt du travail effectué pour le programme d'expérience professionnelle en recherche quantitative de JP Morgan Chase & Co. via Forage. Ce programme a enseigné des compétences clés en analyse de données, programmation et mathématiques financières. Les tâches accomplies étaient :

1. **Investigation et Analyse des Données de Prix :** Apprendre sur les marchés des matières premières et démontrer des compétences en analyse de données.

2. **Évaluation d'un Contrat de Stockage de Matières Premières :** Démontrer la compréhension des marchés financiers et de la tarification des dérivés.

3. **Analyse du Risque de Crédit :** Analyser un portefeuille de prêts pour estimer la probabilité de défaut d'un client.

4. **Catégorisation des Scores FICO :** Utiliser la programmation dynamique pour convertir les scores FICO en données catégorielles afin de prédire les défauts.

Les principales fonctions de réponse à chaque problème ont été enregistrées dans des fichiers Python séparés et un Jupyter notebook résume les réponses. Les données brutes utilisées pour tous les problèmes et un certificat de réussite ont également été inclus.

**Mots Clés :** Programmation, Analyse de Données, Dérivés, Matières Premières, Pensée Critique, Statistiques, Risque de Crédit

## Structure du Projet

### Fichiers Python

- `task1.py` : Investigation et analyse des données de prix.
- `task2.py` : Évaluation d'un contrat de stockage de matières premières.
- `task3.py` : Analyse du risque de crédit.
- `task4.py` : Catégorisation des scores FICO.

### Jupyter Notebook

- `summary.ipynb` : Résumé des réponses aux problèmes.

### Données

- `data/Task 3 and 4_Loan_Data.csv` : Fichier CSV contenant les données de prêt utilisées pour les tâches 3 et 4.

## Utilisation

### Prérequis

Assurez-vous d'avoir les bibliothèques suivantes installées :

- `numpy`
- `pandas`
- `scikit-learn`

Vous pouvez les installer en utilisant pip :

```sh
pip install numpy pandas scikit-learn
```

### Exemple d'utilisation pour task2.py
Code : 

```sh
import unittest
from datetime import date
from task2 import contrat_prix

class TestContratPrix(unittest.TestCase):

    def test_injection_et_retrait(self):
        dates_injection = [date(2023, 1, 1), date(2023, 2, 1)]
        prix_injection = [10, 12]
        dates_retrait = [date(2023, 3, 1), date(2023, 4, 1)]
        prix_retrait = [15, 18]
        taux = 100
        taux_cout_stockage = 5
        volume_total = 500
        taux_cout_injection_retrait = 1

        valeur_contrat = contrat_prix(dates_injection, prix_injection, dates_retrait, prix_retrait, taux, taux_cout_stockage, volume_total, taux_cout_injection_retrait)
        
        # Vérifiez que la valeur du contrat est correcte
        self.assertEqual(valeur_contrat, 500)  # Remplacez 500 par la valeur attendue

if __name__ == '__main__':
    unittest.main()
```
### Auteur :
Simon HAMELIN
