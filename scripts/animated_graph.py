"""Animated graph, assumes http://www.imagemagick.org/ has been installed."""
import numpy as np
import subprocess
import matplotlib.pyplot as plt
import matplotlib.cm as cm

size = 100
p1 = np.random.random_sample(size)
p2 = np.random.random_sample(size)
index = list(range(size))

fname = []

for i in index:
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111)
    ax.axis([min(p1)-0.1, max(p1)+0.1, min(p2)-0.1, max(p2)+0.1])
    ax.scatter(p1[:i+1], p2[:i+1], c=index[:i+1], cmap=cm.rainbow, alpha=0.5,
               s=200)
    plt.xlabel('variable 1')
    plt.ylabel('variable 2')

    n = 'graph_{0}.png'.format(i)
    fname.append(n)
    fig.savefig(n)

call = 'convert -delay 15 -loop 0 '
for i in fname:
    call += i + ' '
call += 'animated.gif'

subprocess.call(call, shell=True)
