from gpcharts import figure 
grafico=figure('Evaluaciones y tendencias de calificaciones')
grafico.ylabel='Calificaciones'
grafico.xlabel='Pruebas realizadas'

grafico.scatter([20,15,18,14,16,12,9,8,13,11,17,20,20,20],trendline=True)

#linea de tendencia permite analizar el comportamiento de las califiaciones y asi predecir o estimar.