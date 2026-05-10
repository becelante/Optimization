import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd


def plot_sudoku(data: list[tuple]) -> None:
    N = range(1, 10)
    Grid = pd.DataFrame([(i, j) for i in N for j in N], columns=['i', 'j'])
    data_df = pd.DataFrame(data, columns=['i', 'j', 'k'])
    finalGrid = pd.merge(Grid, data_df, how='left').fillna(0)
    grid = finalGrid['k'].values.reshape(9, 9).astype(int)

#Create the sudoku image
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 9)
    ax.set_aspect('equal')
    ax.axis('off')
    fig.patch.set_facecolor('white')

#Iterate through the grid and draw cells and numbers
    for i in range(9):
        for j in range(9):
            val = grid[i][j]
            x, y = j, 8 - i #Invert y-axis to match Sudoku layout (matplotlib's origin is at the bottom-left)

            if val != 0: #Highlight known values with a different background color
                ax.add_patch(patches.Rectangle(
                    (x, y), 1, 1, facecolor='#F1EFE8', edgecolor='none'
                ))

            ax.add_patch(patches.Rectangle( #Draw cell borders
                (x, y), 1, 1, facecolor='none', edgecolor='#BBBBBB', linewidth=0.5
            ))

            if val != 0: #Draw the numbers in the center of the cells
                ax.text(x + 0.5, y + 0.5, str(val),
                        ha='center', va='center',
                        fontsize=16, fontweight='bold', color='#2C2C2A')
                
#Draw thicker lines to separate 3x3 subgrids
    for k in range(4):
        lw = 2.5 if k % 3 == 0 else 0.5
        ax.axhline(k * 3, color='#2C2C2A', linewidth=lw)
        ax.axvline(k * 3, color='#2C2C2A', linewidth=lw)

#Draw outer border
    ax.add_patch(patches.Rectangle(
        (0, 0), 9, 9, facecolor='none', edgecolor='#2C2C2A', linewidth=2.5
    ))

    plt.tight_layout(pad=0.3) #Add some padding around the plot
    plt.show()
