# coding:utf-8
import matplotlib.pyplot as plt
import json
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

if __name__ == "__main__":
    f = open("./wave_data1.json", 'r')
    jsonData = json.load(f)
    waveDataList = jsonData["waveDataList"]

    plt.subplots(4, 2, figsize=(20, 14), frameon=True)
    for i, waveData in enumerate(waveDataList):
        wave_x, wave_y = [], []
        for key, value in waveData["waveHeight"].items():
            wave_x.append(float(key))
            wave_y.append(float(value))

        plt.subplot(4, 2, i+1)
        plt.xlim((-32, 32))
        plt.ylim((-2, 2))
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.plot(wave_x, wave_y, color='blue', label='时刻: ' + str(i))
        plt.legend()
        plt.xlabel("X轴坐标", size=16)
        plt.ylabel("海浪高度", size=16)

    # plt.show()
    plt.savefig("./wave_diff.png", dpi=300)
    plt.clf()