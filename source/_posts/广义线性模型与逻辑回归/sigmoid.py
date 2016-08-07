import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-6, 6, 100, endpoint = True)
plt.figure(figsize = (9, 5))
one = np.ones(np.shape(x))
g = 1 / (1 + np.exp(-x))
plt.plot(x, one, color = 'black', linestyle = '--')
plt.plot(x, g, color = 'red', linewidth = 2.5, label = "$ g(x) =  (1 + e ^ { -x }) ^ {-1} $");
plt.legend(loc = 'upper left');

plt.xticks(np.linspace(-6, 6, 7, endpoint = True));
plt.yticks(np.linspace(0, 1, 3, endpoint = True));
plt.ylim(0, 1.2)
plt.xlim(-6.5, 6.5);

plt.scatter([0,],[0.5], 50, color = 'blue');

plt.annotate(r'$ g(0) = 0.5 $',
         xy=(0, 0.5), xycoords='data',
         xytext=(+20, 0), textcoords='offset points', fontsize=16,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))


ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

plt.savefig('sigmoid.png', dpi = 72);
plt.show();