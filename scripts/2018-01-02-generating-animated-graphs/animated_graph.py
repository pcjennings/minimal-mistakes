"""Assumes http://www.imagemagick.org/ has been installed."""
import numpy as np
import subprocess
import matplotlib.pyplot as plt
import matplotlib.cm as cm

size = 100  # number of data points

# generate some random data to plot
x = np.random.random_sample(size)
y = np.random.random_sample(size)
index = list(range(size))

# create a list to store filenames to be stitched
fname = []

# loop over data points and generate all plots
for i in index:
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111)
    ax.axis([min(x)-0.1, max(x)+0.1, min(y)-0.1, max(y)+0.1])
    ax.scatter(x[:i+1], y[:i+1], c=index[:i+1], cmap=cm.rainbow, alpha=0.5,
               s=200)

    n = 'graph_{0}.png'.format(i)
    fname.append(n)
    fig.savefig(n)

# make the gif calling ImageMagick
call = 'convert -delay 15 -loop 0 '
for i in fname:
    call += i + ' '
call += 'animated.gif'

subprocess.call(call, shell=True)
