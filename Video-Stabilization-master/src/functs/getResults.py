import numpy as np
from os import listdir
from os.path import isfile, join
from stabFuncts import getITF

resPath = "/media/achyuth/D6E2B920E2B905B1/MSIT/Stabilization/Video-Stabilization-master/Videos/"
onlyfiles = [f for f in listdir(resPath) if isfile(join(resPath, f))]
onlyfiles.sort()
maxlength = max(len(s) for s in onlyfiles)
onlyfilesext = [f.ljust(maxlength, ' ') for f in onlyfiles]

names = np.array(onlyfilesext)
#print onlyfiles
#print names

# compute ITF
itf = []
for vid in onlyfiles:
    itf.append(str(getITF(resPath+vid)))
itf = np.array(itf)

res =  np.column_stack((names, itf))
np.savetxt("res.txt", res, delimiter=" ", fmt="%s")
