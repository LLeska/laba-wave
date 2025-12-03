import RPi.GPIO as GPIO
import adc_mcp
from datetime import datetime
from time import time, sleep
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import numpy as np


dynamic_range = 5.0
comp_time = 0.1
k = 3.138155
b = 0.168342
gir_pin = 15


if __name__ == "__main__":

    try:
        s = "10.5"
        adcs = []
        t = []
        files = ["10.5_см.csv"]
        for i in range(len(files)):
            with open(files[i]) as file:
                adc_ = []
                t_ = []
                lines = [line.rstrip() for line in file]
                for j in range(3, len(lines)):
                    a, c = map(float, lines[j].split(";"))
                    adc_.append(a)
                    t_.append(c)
                adcs= adc_
                t=t_
        
        h = np.float64(k) * np.array(adcs) + np.float64(b)
        plt.plot(t, h, "blue", linewidth=2, marker='o', markersize=2, label=f'{s} см')

        # Настраиваем оси и заголовок
        plt.xlabel('время, мс', fontsize=14)
        plt.ylabel('высота, см', fontsize=14)
        plt.title('Зависимость показаний высоты от времени', fontsize=12)
        ax = plt.gca()
        # Автоматические дополнительные деления (4 промежуточных деления между основными)
        ax.xaxis.set_minor_locator(AutoMinorLocator(5))
        ax.yaxis.set_minor_locator(AutoMinorLocator(5))
        # Основная сетка
        plt.grid(True, which='major', linestyle='-', alpha=0.9, linewidth=0.8)
        # Дополнительная сетка
        plt.grid(True, which='minor', linestyle=':', alpha=0.7, linewidth=0.5)
        plt.legend(loc='best', fontsize=10)
        plt.show()

    finally:
        pass