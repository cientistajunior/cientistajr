import matplotlib.pyplot as plt

alturas = [150, 160,165,170,175,180,185]

pesos = [50,60,65,70,75,80,85]

plt.scatter(alturas,pesos)
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.title('Relação entre Altura e Peso')
plt.show()
