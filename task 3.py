from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import numpy as np
import pandas as pd

# Entraîner le classificateur en utilisant les données brutes
df = pd.read_csv('data/Task 3 and 4_Loan_Data.csv')
features = ['credit_lines_outstanding', 'dette_sur_revenu', 'paiment_sur_reven', 'years_employed', 'fico_score']
df['paiment_sur_reven'] = df['loan_amt_outstanding'] / df['income']
df['dette_sur_revenu'] = df['total_debt_outstanding'] / df['income']
clf = LogisticRegression(random_state=0, solver='liblinear', tol=1e-5, max_iter=10000).fit(df[features].values, df['default'])

# Définir le modèle de perte attendue
def expected_loss(df):
    df['paiment_sur_revenu'] = df['loan_amt_outstanding'] / df['income']
    df['dette_sur_revenu'] = df['total_debt_outstanding'] / df['income']
    default_prob = clf.predict_proba(df[features].values.reshape(1, -1))
    return  default_prob[0,1]*df['loan_amt_outstanding']*0.1  