import adc_mcp
from datetime import datetime
from time import time
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator


dynamic_range = 5.0
comp_time = 0.1



if __name__ == "__main__":
    adc = adc_mcp.MCP3021(dynamic_range, comp_time)
    try:
        s = input("Введите уровень воды в см")
        dt = datetime.now()
        print("- Wave Lab")
        print("- Date: ", dt)
        t = []
        adc_arr = []
        with open("files_calib.txt", "w") as files:
            with open(s+"_см_calib.csv", "w") as file:
                files.write(s+"_см.csv\n")
                file.write("- Jet Lab\n")
                file.write("- Date: "+ str(dt)+"\n")
                file.write(s+"см\n")
                t0 = time()
                for i in range(10/comp_time):
                    mes = adc.read
                    tc = time()
                    t1 = time()
                    adc.append(mes)
                    t.append(t1)
                    ans = str(mes)+";"+str(t1 - t0) +"\n"
                    print(ans)
                    file.write(ans) 
                    print(time() - tc)    
        plt.plot(adc, t, "blue", linewidth=2, marker='o', markersize=2, label=f'{s} см')

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

    finally:
        adc.deinit()