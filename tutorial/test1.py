import matplotlib.pyplot as plt
import matplotlib.image as mpimg

if __name__ == "__main__":
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
    plt.show()