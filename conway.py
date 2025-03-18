import tensorflow as tf
from typing import List

def iterate_grid(grid: List[List[int]]) -> List[List[int]]:
    grid = tf.convert_to_tensor(grid, dtype=tf.int32)

    # Pad the grid with zeros to handle edge cases
    padded_grid = tf.pad(grid, [[1, 1], [1, 1]], mode='CONSTANT')

    neighbors = sum(tf.roll(tf.roll(padded_grid, shift=i, axis=0), shift=j, axis=1)
                    for i in (-1, 0, 1) for j in (-1, 0, 1)
                    if (i != 0 or j != 0))

    # Remove the padding after calculating neighbors
    neighbors = neighbors[1:-1, 1:-1]

    new_grid = tf.where((neighbors == 3) | ((grid == 1) & (neighbors == 2)), 1, 0)
    return new_grid.numpy().tolist()