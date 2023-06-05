import matplotlib.pyplot as plt

meses = ['Enero','Febrero','Marzo']
ventas = [15000,50000,25400]

colores = ['red','#FF88cc','#df544f','c']

separacion = [0.1,0,0]

# plt.bar(meses,ventas,color=colores)
plt.pie(ventas,labels=meses,startangle = 85, explode=separacion, shadow = True , colors=colores , labeldistance=100)
plt.title('Venta Primer Trimestre')
# plt.xlabel('Meses')
# plt.ylabel('Ventas')
plt.legend(title = "Meses:")
plt.show()