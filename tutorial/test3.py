import matplotlib.pyplot as plt
import matplotlib.image as mpimg

if __name__ == "__main__":
    plt.subplots()
    plt.plot([1,2,3,4,5],[2,3,1,4,5], color='blue', label='min')
    plt.plot([1,2,3,4,5],[12,13,11,14,15],color='red', label='max')
    # plt.legend(loc='lower left')
    plt.legend(loc='best')
    plt.xlabel("index")
    plt.ylabel("height")
    plt.title("test3")
    plt.show()