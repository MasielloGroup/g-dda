import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('Spectrum')
data_sort = data[data[:,1].argsort(),]
aeff = data_sort[:,0]
wave = 1.240/data_sort[:,1]
C_ext = data_sort[:,2]*np.pi*aeff**2
C_abs = data_sort[:,3]*np.pi*aeff**2
C_sca = data_sort[:,4]*np.pi*aeff**2

plt.plot(wave, C_ext, label='Ext.')
plt.plot(wave, C_abs, label='Abs.')
plt.plot(wave, C_sca, label='Sca.')

plt.xlabel('Energy [eV]')
plt.ylabel('Cross Section [$\mu$m$^2$]')
plt.legend(frameon=False)
plt.xlim([1, 2.5])
plt.show()

