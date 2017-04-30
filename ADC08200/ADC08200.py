import matplotlib.pyplot as plt
import numpy as np


def CreateSeries(File,FreqRef):

	with open(File) as f:
	    content = f.readlines()
	# you may also want to remove whitespace characters like `\n` at the end of each line
	Vd = [x.strip().split("\t")[2] for x in content] 
	Vd = np.array(Vd).astype(np.float)
	Vd = 64.0* Vd / 5.0 / 8.0
	V = [x.strip().split("\t")[1] for x in content] 
	V = np.array(V).astype(np.float)
	V = 64.0* V / 5.0 
	OverFlow = [ int(x/32) for x in V]
	t = [x.strip().split("\t")[0] for x in content]
	t = np.array(t).astype(np.float)/FreqRef
	Res = []
	N = t[-1]
	for i in range(len(OverFlow)):
		Res.append((V[i]-32*OverFlow[i]+32*Vd[i]+128*OverFlow[i])*3.3/256)

	return Res,t,N

