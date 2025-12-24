import sys

import matplotlib.pyplot as plt
import socolors

try:
    plt.style.use(sys.argv[1])
    filename = f"{sys.argv[1]}.png"
except IndexError:
    filename = "default.png"

for x in range(5):
    plt.plot(range(10), [10 ** (i + x) for i in range(10)], label=f"$i={x}$")

plt.xlabel("$x$-value")
plt.ylabel("$10^{x+i}$")
plt.legend()
plt.semilogy()

plt.savefig(filename)
