There are a number of ways to generate animated graphs. In this post, I will use a combination of matplotlib and [ImageMagick](http://www.imagemagick.org/script/index.php) to produce a relatively easy and robust way to generate an animated gif of a graph. It is possible to do this directly with matplotlib, however, I found this to be a little fiddly.

## General Method

The easiest way to generate a gif without needing to change pre-existing code too much is to create a large number of individual graphs and then stitch them together. The graphs are created with matplotlib and saved as png files, though any plotting library could be used. ImageMagick is then called to stitch all the individual images together.

## Automating

The automated script is relatively simple.

  ```python
  """Assumes http://www.imagemagick.org/ has been installed."""
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
  ```

The graph comes out as follows:

![animated graph](../scripts/animated.gif)
