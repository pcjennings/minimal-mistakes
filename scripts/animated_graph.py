"""Animated graph, assumes http://www.imagemagick.org/ has been installed."""
import numpy as np
import subprocess
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm

matplotlib.rc('font', serif='Helvetica Neue Light')
matplotlib.rcParams.update({'font.size': 22})

p1 = np.random.random_sample(size=100)
p2 = np.random.random_sample(size=100)
index = list(range(len(p1)))

step_p1, step_p2, step_index = [], [], []
fname = []
for i in index:
    step_p1.append(p1[i])
    step_p2.append(p2[i])
    step_index.append(i)

    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111)
    ax.axis([min(p1)-0.1, max(p1)+0.1, min(p2)-0.1, max(p2)+0.1])
    ax.scatter(step_p1, step_p2, c=step_index, cmap=cm.rainbow, alpha=0.5,
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
