#!/usr/bin/env python
#*-* coding: utf-8 *-*

import sys
import numpy as np
import matplotlib.pyplot as plt


cpu_dict = dict()
t=0
with open(str(sys.argv[1]), 'r') as profile:
  for i, line in enumerate(profile):
    if i > 1:
      campos = line.split()
      if len(campos) != 0:
        key = campos[0]
        value = float(campos[2].strip('%'))
        if key in cpu_dict:
          l= len(cpu_dict[key])
          if l < t:
            cpu_dict[key].extend([0]*(t-l-1))
          cpu_dict[key].append(value)
        else:
          if t > 1:
            cpu_dict[key] = [0]* (t-1)
            cpu_dict[key].append(value)    
          else:
            cpu_dict[key] = [value]
      else:
        t=t+1


n=np.arange(t)
indice=cpu_dict['idle'].index(min(cpu_dict['idle']))

for key in cpu_dict:
	l=len(cpu_dict[key])
	if l!=t:
	    cpu_dict[key].extend([0]*(t-l))
	y=np.array(cpu_dict[key])
	plt.plot(n,y)
	



print '-' * 30
print 'Indices del profile:'
print ' - ' + '\n - '.join(sorted(cpu_dict.keys()))
print '-' * 30
print 'Minimo de CPU IDLE:' + str(min(cpu_dict['idle'])) + '%'
print '-' * 30

for key in cpu_dict:
	print '{0:15}\tMax {1:4}%\tMin {2:4}%\tLen {3}'.format(key, max(cpu_dict[key]), min(cpu_dict[key]), len(cpu_dict[key]))

print '-' * 60
print 'Valores de todos los indices cuando CPU IDLE es minimo:' + str(min(cpu_dict['idle'])) + '%'
print '-' * 60

for key in cpu_dict:
  print '{0:15}\tValue {1:4}%'.format(key, cpu_dict[key][indice])


plt.ylabel('CPU Load %')
plt.xlabel('Time')
plt.title('CPU Consumption Mikrotik')
plt.legend(cpu_dict.keys())
plt.show()  