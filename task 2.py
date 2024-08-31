from datetime import date
import math

def contrat_prix(dates_injection, prix_injection, dates_retrait, prix_retrait, taux, taux_cout_stockage, volume_total, taux_cout_injection_retrait):
    
    volume = 0
    cout_achat = 0
    encaissement = 0
    derniere_date = min(min(dates_injection), min(dates_retrait))
    
    # Assurer que les dates sont en séquence
    toutes_dates = sorted(set(dates_injection + dates_retrait))
    
    for i in range(len(toutes_dates)):
        # traitement pour chaque date
        date_debut = toutes_dates[i]

        if date_debut in dates_injection:
            # Injecter à ces dates et additionner les flux de trésorerie
            if volume <= volume_total - taux:
                volume += taux

                # Coût d'achat du gaz
                cout_achat += taux * prix_injection[dates_injection.index(date_debut)]
                # Coût d'injection
                cout_injection = taux * taux_cout_injection_retrait
                cout_achat += cout_injection
                print('Gaz injecté le %s à un prix de %s' % (date_debut, prix_injection[dates_injection.index(date_debut)]))

            else:
                # Nous ne voulons pas injecter lorsque le taux est supérieur au volume total moins le volume
                print('L\'injection n\'est pas possible à la date %s car il n\'y a pas assez d\'espace dans l\'installation de stockage' % date_debut)
        elif date_debut in dates_retrait:
            # Retirer à ces dates et additionner les flux de trésorerie
            if volume >= taux:
                volume -= taux
                encaissement += taux * prix_retrait[dates_retrait.index(date_debut)]
                # Coût de retrait
                cout_retrait = taux * taux_cout_injection_retrait
                encaissement -= cout_retrait
                print('Gaz extrait le %s à un prix de %s' % (date_debut, prix_retrait[dates_retrait.index(date_debut)]))
            else:
                # Nous ne pouvons pas retirer plus de gaz que ce qui est effectivement stocké
                print('L\'extraction n\'est pas possible à la date %s car il n\'y a pas assez de volume de gaz stocké' % date_debut)
                
    cout_stockage = math.ceil((max(dates_retrait) - min(dates_injection)).days // 30) * taux_cout_stockage

    return cout_stockage