import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import numpy as np
from scipy.interpolate import CubicSpline

colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
    '#ff0000', '#000000'
]

adc = []
t = []
with open("files_calib.txt", "r") as file:
    files = [line.rstrip() for line in file]
for i in range(len(files)):
    with open(files[i]) as file:
        adc_ = []
        t_ = []
        lines = [line.rstrip() for line in file]
        for i in range(3, len(lines)):
            a, b = map(int, lines[i].split(";"))
            adc_.append(a)
            t_.append(b)
        adc.append(adc_)
        t.append(t_)



h = []
adcs = []
for i in range(len(files)):
    adcs.append(sum(adc)/len(adc))
    h.append(files[i][:-13])
    plt.plot(adc[i], t[i], colors[i], linewidth=2, marker='o', markersize=2, label=f'{h[i]} см')

adcs = np.array(adcs)
h = np.array(h)
k, b = np.polyfit(adcs, h, deg=1)
# Настраиваем оси и заголовок
plt.xlabel('время, мс', fontsize=14)
plt.ylabel('показания ацп', fontsize=14)
plt.title('Зависимость показаний ацп от времени', fontsize=12)
ax = plt.gca()
# Автоматические дополнительные деления (4 промежуточных деления между основными)
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
# Основная сетка
plt.grid(True, which='major', linestyle='-', alpha=0.9, linewidth=0.8)
# Дополнительная сетка
plt.grid(True, which='minor', linestyle=':', alpha=0.7, linewidth=0.5)
plt.legend(loc='best', fontsize=10)


plt.figure(figsize=(6, 6))
plt.scatter(adcs, h, color='blue')
# Настраиваем оси и заголовок
plt.xlabel('высота уровня воды', fontsize=14)
plt.ylabel('показания ацп', fontsize=14)
plt.title('Зависимость показаний ацп от высоты уровня воды\nk = {k}, b = {b}', fontsize=12)
ax = plt.gca()
# Автоматические дополнительные деления (4 промежуточных деления между основными)
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
# Основная сетка
plt.grid(True, which='major', linestyle='-', alpha=0.9, linewidth=0.8)
# Дополнительная сетка
plt.grid(True, which='minor', linestyle=':', alpha=0.7, linewidth=0.5)
plt.legend(loc='best', fontsize=10)



plt.tight_layout()
plt.show()