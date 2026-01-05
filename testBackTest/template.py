#Importation des library
import pandas as pd
import numpy as np
import vectorbt as vbt
import matplotlib.pyplot as plt
import anywidget
import os


# Télécharger les données (Utilise Python Binance)
# a PARTIR D'une date jusqu'a aujourd'hui (intervale 15 minutes)
symbol = ['ETHUSDT']
time = '15m'
# Téléchargement des données
data = vbt.BinanceData.download(
    symbol, 
    start='2024-09-01', 
    interval=time
)



#Mise en forme des données
# Agencement des données + index + mis à l'heure de paris
df_raw = data.get(['Close','Open','High','Low','Volume']).copy()
df_raw.index = df_raw.index.tz_convert('Europe/Paris')
df_raw.tail()

# Separation des données en train et test (IS/OOS) (70/30%)
split_idx = int(0.7*len(df_raw))
train_data = df_raw.iloc[:split_idx]
test_data = df_raw.iloc[split_idx:]

# Affichage de la séparation des données
#plt.figure(figsize=(10, 1))
#plt.barh(['Dataset'], [len(df_raw)], color='lightgray', alpha=0.3)
#plt.barh(['Dataset'], [split_idx], color='blue', alpha=0.5, label='Train')
#plt.barh(['Dataset'], [len(df_raw)-split_idx], left=split_idx, color='orange', alpha=0.5, label='Test')
#plt.title('Train/Test Split Visualization')
#plt.legend()
#plt.show()

# Selection du train_set comme données d'entrainement
df = train_data.copy()


            #           #
############## Stratégie ##############
            #           #
            
# Description de la stratégie
                
            




# BackTest

# Lancement du backtest avec VBT
# Fonction From Signals
portfolio = vbt.Portfolio.from_signals()

stats = portfolio.stats()
# Affichage des statistiques
print(portfolio.stats())
# ajout des statistique dans un csv (les ajouter a la suite et ne pas écraser les données existantes)
stats = portfolio.stats().to_frame().T
stats.to_csv('backtest_stats.csv', mode='a',header=not os.path.exists('backtest_stats.csv'),index=False,)