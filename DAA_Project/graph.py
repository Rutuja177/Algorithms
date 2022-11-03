import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([50, 100, 500, 1000,5000,10000])
ypoints = np.array([.000603,.002309,.046131,.116293,1.984896,7.921630])
y2 = np.array([.000244,.000931,.024447,.062882,.668152,2.514627])
y3 = np.array([.000325,.001189,.025219,.074623,.904756,3.438328])
y4 = np.array([.000633,.001656,.007157,.017398,.059195,.080384])
y5 = np.array([.000372,.000865,.006320,.012559,.057591,.081131])
y6 = np.array([.000402,.000812,.004316,.011832,.040166,.061523])
y7 = np.array([.000361,.000631,.003773,.009068,.040349,.053792])


plt.plot(xpoints, ypoints)
plt.plot(xpoints,y2)
plt.plot(xpoints,y3)
plt.plot(xpoints,y4)
plt.plot(xpoints,y5)
plt.plot(xpoints,y6)
plt.plot(xpoints,y7)


plt.legend(["BubbleSort", "SelectionSort","InsertionSort","MergeSort","HipSort","QuickSort","QuickSortWith3Median"])
plt.show()