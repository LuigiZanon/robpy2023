#arquivo de teste

import RobPy as rp
import numpy as np

a = np.asarray([[1,2,3]]).T

print(a)

v3 = rp.cria_vetor3([3,2,1])

v4 = rp.cria_vetor4(v3)

print(v4)