import pandas as pd 
#create dataframe
df_marks=pd.DataFrame({'name':['Luis', 'Andrea', 'Miguel', 'Samir'],
                       'Quimica':[68,74,77,78],
                       'Algebra':[84,56,73,69],
                       'Geometria':[78,88,82,87]})
#Create excel
writer=pd.ExcelWriter('Puntajes.xlsx')

#Write dataframe to excel
df_marks.to_excel(writer)

#save
writer.save()

print("Archivo excel creado correctamente...")