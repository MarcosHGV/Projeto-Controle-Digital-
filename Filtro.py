import numpy as np
import matplotlib.pyplot as plt

def filtro(x):
    a1 = 1.99685
    a2 = 0.99686
    b = 0.00000246352
    y = np.zeros(len(x))
    y[0] = 0
    y[1] = 0
    for n in range(2, len(x)):
        y[n] = a1 * y[n-1] - a2 * y[n-2] + b * (2 * x[n-1] + x[n-2] + x[n])
    return y

def gerar_sinal(freq_sinal, freq_ruido, duracao):
    num_pontos = int(duracao * 100)  # Número de pontos desejados no vetor t
    t = np.linspace(0, duracao, num_pontos, endpoint=False)
    x = np.cos(2 * np.pi * freq_sinal * t) + 0.1 * np.cos(2 * np.pi * freq_ruido * t)
    return x

# Gerar sinal de entrada
x = gerar_sinal(0.04, 0.8, 150)

# Aplicar filtro duas vezes
filtrado = filtro(x)
novo = filtro(filtrado)

# Plotar os sinais
plt.figure(figsize=(12,8), facecolor='white')
plt.plot(x, label="Sinal de entrada", color='red')
plt.plot(filtrado, label="Sinal filtrado", color='green')
plt.gca().set_facecolor('lightgrey')  # Cor de fundo do gráfico

plt.xlabel('Amostras', fontsize=17, fontweight='bold')
plt.ylabel('Amplitude',  fontsize=17, fontweight='bold')
plt.title('Sinais: Entrada e Filtrado',  fontsize=18, fontweight='bold')
plt.legend()
plt.grid()
plt.show()
