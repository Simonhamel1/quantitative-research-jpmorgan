import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from datetime import date, timedelta

# Charger les données dans un dataframe pandas
date_debut = date(2020, 10, 31)
date_fin = date(2024, 9, 30)
date_extrap = date(2025, 9, 30)
date_temps = ["10-2020", "11-2020", "12-2020"]
date_temps = pd.to_datetime(date_temps)
data = [1, 2, 3]
df = pd.read_csv('./data/nat_gas.csv', parse_dates=['Dates'])
prix = df['Prices'].values
dates = df['Dates'].values

# Convertir les dates en jours depuis le début
mois = []
annee = date_debut.year
mois_actuel = date_debut.month + 1
while True:
    courant = date(annee, mois_actuel, 1) + timedelta(days=-1)
    mois.append(courant)
    if courant.month == date_fin.month and courant.year == date_fin.year:
        break
    else:
        mois_actuel = ((mois_actuel + 1) % 12) or 12
        if mois_actuel == 1:
            annee += 1        
jours_depuis_debut = [(jour - date_debut).days for jour in mois]

# Ajustement par régression linéaire
def regression_simple(x, y):
    xbar = np.mean(x)
    ybar = np.mean(y)
    pente = np.sum((x - xbar) * (y - ybar)) / np.sum((x - xbar)**2)
    intercept = ybar - pente * xbar
    return pente, intercept

temps = np.array(jours_depuis_debut)
pente, intercept = regression_simple(temps, prix)

# Utiliser la régression bilinéaire, sans intercept, pour résoudre u = Acos(z), w = Asin(z)
sin_prix = prix - (temps * pente + intercept)
sin_temps = np.sin(temps * 2 * np.pi / 365)
cos_temps = np.cos(temps * 2 * np.pi / 365)

def regression_bilineaire(y, x1, x2):
    # La régression bilinéaire sans intercept revient à projeter sur les vecteurs x
    pente1 = np.sum(y * x1) / np.sum(x1 ** 2)
    pente2 = np.sum(y * x2) / np.sum(x2 ** 2)
    return pente1, pente2

pente1, pente2 = regression_bilineaire(sin_prix, sin_temps, cos_temps)
amplitude = np.sqrt(pente1 ** 2 + pente2 ** 2)
decalage = np.arctan2(pente2, pente1)

# Définir la fonction d'interpolation/extrapolation
def interpoler(date):
    jours = (date - pd.Timestamp(date_debut)).days
    if jours in jours_depuis_debut:
        # Correspondance exacte trouvée dans les données
        return prix[jours_depuis_debut.index(jours)]
    else:
        # Interpoler/extrapoler en utilisant le modèle sin/cos
        return amplitude * np.sin(jours * 2 * np.pi / 365 + decalage) + jours * pente + intercept

def fonction_prix_futur(date_debut, date_extrap):
    x = np.array(jours_depuis_debut)
    y = np.array(prix)
    amplitude_fit = np.sqrt(pente1 ** 2 + pente2 ** 2)
    decalage_fit = np.arctan2(pente2, pente1)
    pente_fit, intercept_fit = regression_simple(x, y - amplitude_fit * np.sin(x * 2 * np.pi / 365 + decalage_fit))
    dates_continues = pd.date_range(start=pd.Timestamp(date_debut), end=pd.Timestamp(date_extrap), freq='D')
    prix_fit = amplitude_fit * np.sin((dates_continues - pd.Timestamp(date_debut)).days * 2 * np.pi / 365 + decalage_fit) + (dates_continues - pd.Timestamp(date_debut)).days * pente_fit + intercept_fit
    return dates_continues, prix_fit