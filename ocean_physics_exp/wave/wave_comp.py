# coding:utf-8
import matplotlib.pyplot as plt
import json
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

if __name__ == "__main__":
    f = open("./wave_data1.json", 'r')
    jsonData = json.load(f)
    waveDataList = jsonData["waveDataList"]

    plt.subplots(1, 1, figsize=(18, 6), frameon=True)
    plt.xlim((-32, 32))
    plt.ylim((-2, 2))
    plt.grid(True, linestyle='--', alpha=0.8)
    plt.xlabel("X轴坐标", size=16)
    plt.ylabel("海浪高度", size=16)

    for i, waveData in enumerate(waveDataList):
        wave_x, wave_y = [], []
        for key, value in waveData["waveHeight"].items():
            wave_x.append(float(key))
            wave_y.append(float(value))

        plt.plot(wave_x, wave_y, alpha=0.5, label='时刻: ' + str(i), linewidth=2)

    plt.legend(loc="lower right")
    plt.savefig("./wave_comp.png", dpi=300)
    plt.clf()