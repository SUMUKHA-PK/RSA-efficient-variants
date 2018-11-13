from matplotlib import pyplot as plt

bits = [2048,2304,2560,2816,3072]

Time = [684.47,335.12,298.73,661.07,593.27]


plt.plot(bits,Time, label='EA1RSA')

plt.xlabel('Number of bits')
plt.ylabel('Time taken')

plt.legend()

plt.show()