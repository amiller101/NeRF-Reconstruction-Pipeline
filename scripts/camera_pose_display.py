import argparse

import json

import numpy as np

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

def plot_trajectory(poses, directions, save_path=None):

    fig = plt.figure(figsize=(12, 6))

    # 3D Perspective View
    ax1 = fig.add_subplot(121, projection='3d')

    #ax1.plot(poses[:, 0], poses[:, 1], poses[:, 2], label='Camera Path', color='blue', linestyle='--')

    ax1.scatter(poses[:, 0], poses[:, 1], poses[:, 2], c=np.arange(len(poses)), cmap='viridis', s=30)
    # Plot directions as red arrows

    for pos, dir in zip(poses, directions):
        ax1.quiver(pos[0], pos[1], pos[2], dir[0], dir[1], dir[2], length=0.35, color='red')

    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')
    ax1.set_title('3D Perspective View')
    #ax1.legend()

    # Top View (X-Y plane)
    ax2 = fig.add_subplot(122)
    #ax2.plot(poses[:, 0], poses[:, 1], label='Camera Path', color='blue', linestyle='--')
    ax2.scatter(poses[:, 0], poses[:, 1], c=np.arange(len(poses)), cmap='viridis', s=30)

    # Plot directions in 2D (projected)

    for pos, dir in zip(poses, directions):
         ax2.arrow(pos[0], pos[1], dir[0]*0.1, dir[1]*0.1, head_width=0.05, head_length=0.05, fc='red', ec='red')

    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_title('Top View (X-Y)')
    ax2.axis('equal')
    #ax2.legend()

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)

    else:
        plt.show()

  
def main():

    parser = argparse.ArgumentParser(description='Visualize camera poses from transforms.json')

    parser.add_argument('--input_dir', required=True, help='Directory containing transforms.json')
    args = parser.parse_args()

    input_dir = args.input_dir
    json_path = f"{input_dir}/transforms.json"

    with open(json_path, 'r') as f:
        data = json.load(f)

    frames = data['frames']

    positions = []
    directions = []

    for frame in frames:

        matrix = np.array(frame['transform_matrix'])

        # Translation vector
        pos = matrix[:3, 3]
        # Rotation matrix
        rot = matrix[:3, :3]

        # Assuming camera's forward direction is -Z in camera coordinates

        forward_world = rot @ np.array([0, 0, -1])

        positions.append(pos)

        directions.append(forward_world)

    positions = np.array(positions)
    directions = np.array(directions)
    plot_trajectory(positions, directions)


if __name__ == "__main__":
    main()