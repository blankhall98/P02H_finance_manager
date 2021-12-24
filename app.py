from finance_manager import FinMan

#Lista de mis acciones (portafolio)
mi_portafolio = ['BTC-USD','SPY']


#Inicializacion de mis acciones
#TIP: Cambia el nombre de la acción a analizar
spy = FinMan('BTC-USD')

#Ver mi base de datos
print(spy.stock)

#Visualizar serie de tiempo
spy.plot_time_series('Returns')

#Visualizar Histograma de la aplicación
spy.plot_histogram()
spy.plot_boxplot()

#Imprimir resumen accion
spy.stock_summary()