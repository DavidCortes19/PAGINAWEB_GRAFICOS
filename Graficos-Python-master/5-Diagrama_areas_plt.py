import matplotlib.pyplot as plt

sales_a=[2,3.5,4.5,5.2,3,7,5.5]
sales_b=[1,2.3,3.1,4.5,2,4.2,4.3]
years=[2016,2017,2018,2019,2020,2021,2022]

plt.fill_between(years,sales_a,label="EMPRESA A",color="green")
plt.fill_between(years,sales_b,label="EMPRESA B",color="blue")

plt.title("DIAGRAMA DE AREAS")
plt.legend(loc="upper left")
plt.show()