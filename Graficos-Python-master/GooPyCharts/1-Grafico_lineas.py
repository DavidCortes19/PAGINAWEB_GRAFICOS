from gpcharts import figure
"""
grafico1 = figure('Grafica de lineas')
grafico1.plot([3,4,5,4,3])

grafico2= figure(title='Grafica de  2 lineas')
grafico2.plot([[3,4],[4,2],[5,1],[4,2],[3,4]])
"""
#Grafica
grafico3=figure(title='Ventas tortas (cantidades)',
                ylabel='Cantidad',
                width=800 , height=600)

valoresX=['Dias','Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
valoresY=[['Semana1','Semana2'],[3,4],[4,2],[5,1],[4,2],[3,4],[5,1],[4,2]]
grafico3.plot(valoresX, valoresY);