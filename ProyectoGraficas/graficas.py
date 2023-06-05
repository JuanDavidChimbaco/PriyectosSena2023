import matplotlib.pyplot as plt

xpoint = [0,6,12,24,0]
ypoint = [0,250,0,500,0]

x= [80, 85, 90, 95, 100, 105, 110, 115, 120, 125]
y= [0,200,100,200,0,0,0,0,0,0]

font1 = {'family':'comics','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.title("Sports Watch Data", loc = 'left', fontdict=font1)

plt.subplot(2,1,1)
plt.plot(xpoint,ypoint,marker='.',ms=20, color='red')

plt.subplot(2,1,2)
plt.plot(x,y,'*',linestyle = '-.',linewidth=1)

plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

plt.scatter(x, y)
plt.bar(x,y)
plt.show()