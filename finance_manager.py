import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class FinMan:

    def __init__(self,stock):
        self.name = stock
        self.stock = pd.read_csv('./stocks/'+stock+'.csv')
        self.stock['Date'] = pd.to_datetime(self.stock['Date'])

        self.stock['Returns'] = self.stock['Close'].pct_change()
        
        self.stock = self.stock.dropna()

    def plot_time_series(self,attribute):
        plt.figure(figsize = (12,6))
        plt.title(f'Serie de tiempo de {self.name}')
        plt.xlabel('Fecha')
        plt.ylabel('Valor de la acción en Dolares')
        plt.plot(self.stock['Date'],self.stock[attribute],label=f'{self.name}')
        plt.legend()
        plt.show()

    def plot_histogram(self):
        plt.figure(figsize = (12,6))
        plt.title(f'Histograma de {self.name}')
        plt.hist(self.stock['Returns'],bins=20)
        plt.show()

    def plot_boxplot(self):
        plt.figure(figsize = (12,6))
        plt.title(f'BoxPlot de {self.name}')
        plt.boxplot(self.stock['Returns'])
        plt.show()

    def stock_summary(self):
        return_media = np.mean(self.stock['Returns'])
        return_sd = np.std(self.stock['Returns'])
        print(f'Esta es la información de la acción {self.name}'+'\n'+
        f'Promedio returns: {return_media}'+'\n'+
        f'Desviacin returns: {return_sd}')
