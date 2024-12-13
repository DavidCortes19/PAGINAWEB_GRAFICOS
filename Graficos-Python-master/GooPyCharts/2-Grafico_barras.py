from gpcharts import figure

grafico=figure('Competiciones UEFA (CLUBES)')
grafico.ylabel='Equipos de futbol'
valoresx=['Cantidad de titulos','Real Madrid','AC Milan','Liverpool','Barcelona','Bayern Munich']
valoresy=[['Champions League','Europa League'],
          [15,2],[7,0],[6,3],[5,0],[6,1]]
grafico.bar(valoresx, valoresy)