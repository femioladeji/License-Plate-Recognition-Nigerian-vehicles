import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def plot_cca(image, objects_cordinates):
    fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(12, 12))
    ax.imshow(image, cmap=plt.cm.gray)

    for each_cordinate in objects_cordinates:
        min_row, min_col, max_row, max_col = each_cordinate
        bound_box = mpatches.Rectangle((min_col, min_row), max_col - min_col,
            max_row - min_row, fill=False, edgecolor='red', linewidth=2)
        ax.add_patch(bound_box)

    plt.show()