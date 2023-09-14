#arquivo de teste

import RobPy as rp
import numpy as np

a = rp.cria_vetor3([1,2,3])

b = rp.cria_vetor3([4,5,6])

print(rp.ang_vetores(a,b)*180/np.pi)