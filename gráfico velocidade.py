import math
import matplotlib.pyplot as plt

def calcula_vetorY(v, rad):
	return math.sin (rad) * v
	
def calcula_vetorX(v, rad):
	return math.cos (rad) * v

def calcula_tempo_no_ar (vy, g):
	return vy/g
	
g = 9.8	
#          36, 54, 72, 90, 108 (km/h)
lista_v = [10, 15, 20, 25, 30]
#             15 graus, 30 graus, 40 graus, 45 graus, 50 graus, 60 graus, 70 graus 
lista_rad = [0.261799, 0.523599, 0.698132, 0.785398, 0.872665, 1.0472, 1.22173]
lista_calcula_vetorY = []
lista_calcula_tempo_no_ar = []
lista_distanciaX = []

for i in lista_v:
	for j in lista_rad:
		a = 0		
		a = calcula_vetorY (i, j)
		b = 0		
		b = 2 * calcula_tempo_no_ar (a, g)
		c = 0		
		c = calcula_vetorX (i, j)
		distanciaX = 0
		distanciaX = b * c
		lista_distanciaX.append (distanciaX)

listanova_v = [10, 10, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15, 15, 20, 20, 20, 20, 20, 20, 20, 25, 25, 25, 25, 25, 25, 25, 30, 30, 30, 30, 30, 30, 30,]
listanova_rad = [0.261799, 0.261799, 0.261799, 0.261799, 0.261799, 0.523599, 0.523599, 0.523599, 0.523599, 0.523599,  0.698132, 0.698132, 0.698132, 0.698132, 0.698132, 0.785398, 0.785398, 0.785398, 0.785398, 0.785398, 0.872665, 0.872665, 0.872665, 0.872665, 0.872665, 1.0472, 1.0472, 1.0472, 1.0472, 1.0472, 1.22173, 1.22173, 1.22173, 1.22173, 1.22173]

def plotyy(X,Y1,Y2,eixoX,eixoY1,eixoY2):
    fig, ax1 = plt.subplots()
    ax1.plot(X, Y1, 'b')
    ax1.set_xlabel(eixoX)
    ax1.set_ylabel(eixoY1, color='b')
    for tl in ax1.get_yticklabels():
        tl.set_color('b')
            
    ax2 = ax1.twinx()
    ax2.plot(X, Y2, 'r')
    ax2.set_ylabel(eixoY2, color='r')
    for tl in ax2.get_yticklabels():
        tl.set_color('r')
    plt.show()    
    
    return None
plotyy(listanova_v, listanova_rad, lista_distanciaX, 'Velocidade (m/s)','Graus (rad)','Distância percorrida (m)')

