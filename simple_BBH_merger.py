import numpy as np
import scipy
import scipy.signal
import matplotlib.pyplot as plt

# Frequency ranges of BBH mergers
def fmerger(M):
    '''Calculates the merger freuqency of a BBH system given the total mass M of the system

    '''
    c = 3*10**8
    G = 6.674*10**(-11)
    R = 1.7
    freq = (2*c**3)/(R**(3/2)*G*M*1.989*10**30)/(2*np.pi)

    return freq

# Calculate the frequency ranges of 
ranges = []; masses = []
# 1. Supermassive 10**11 Msolar
Mmin = 2*10**11; Mmax = 2*10**12
ranges.append([fmerger(Mmin), fmerger(Mmax)])
masses.append([Mmin, Mmax])
# 2. Billion Msolar
Mmin = 2*10**9; Mmax = 2*10**10
ranges.append([fmerger(Mmin), fmerger(Mmax)])
masses.append([Mmin, Mmax])
# 3. Million Msolar
Mmin = 2*10**6; Mmax = 2*10**7
ranges.append([fmerger(Mmin), fmerger(Mmax)])
masses.append([Mmin, Mmax])
# 4. Few to tens Msolar
Mmin = 2; Mmax = 20
ranges.append([fmerger(Mmin), fmerger(Mmax)])
masses.append([Mmin, Mmax])

for i in range(len(ranges)):
    plt.plot(masses[i], ranges[i])
plt.legend(['Supermassive', 'Billion','Million', 'Few to tens'])
plt.title('BBH Total Mass vs. Merger Frequency')
plt.yscale("log")
plt.xscale("log")
plt.xlabel(r'Total Mass M ($M_{\odot}$)')
plt.ylabel(r'Merger Frequency $F_m$ (Hz)')
plt.show()

print(ranges)

# Question 3: 