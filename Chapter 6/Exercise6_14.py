# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 10:20:09 2021

@author: Tindi.Sommers
"""


import random
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import animation as animation

# A fuction for updating the animation

def update(frame_number, rolls_per_frame, coin, freq):
    """Function for updating the animation for each frame"""

    # roll the coin (rolls per frame ) times
    for i in range(rolls_per_frame):
        freq[random.randrange(1, 3) - 1] += 1

    # clear the frame for a new frame
    plt.cla()
    # plot a graph of frequency against the values of the coin flip
    title = f'Bar plot of {sum(freq):,} coin flips'
    axes = sns.barplot(x=coin, y=freq, palette='bright')
    axes.set_title(title)
    axes.set(xlabel='Coin', ylabel='Frequencies')
    axes.set_ylim(top=max(freq) * 1.1)

    for bar, frequency in zip(axes.patches, freq):
        text_x = bar.get_x() + bar.get_width() / 2.0
        text_y = bar.get_height()
        text = f'{frequency:,}\n{frequency / sum(freq):.2%}'
        axes.text(text_x, text_y, text, fontsize=12, ha='center', va='bottom')


sns.set_style('whitegrid')
num_of_frames = int(input('Enter the number of frames: '))
rolls_per_frame = int(input('Rolls per frame: '))
freq = [0] * 2
coin = ['Head', 'Tail']
figure = plt.figure('Flipping a coin')

coin_animation = animation.FuncAnimation(figure, update, frames=num_of_frames,
                repeat=False, interval=33, fargs=(rolls_per_frame, coin, freq))

plt.show()  # display the window
