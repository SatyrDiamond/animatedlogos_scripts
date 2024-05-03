
from PIL import Image
import numpy as np
import math

fg = Image.open('logo.PNG')
fg = fg.resize((351,351), Image.Resampling.BICUBIC)
fg_array = np.array(fg)

numframes = 128

for n in range(numframes):
	fg_array = np.array(fg)

	progress = (n/numframes)

	print(n, numframes)

	colorlist = [
	[0.12, 0.12, 0.14], 
	[0.40, 0.53, 0.76],
	[0.22, 0.13, 0.22], 
	[0.91, 0.27, 0.47], 
	[0.12, 0.12, 0.14]
	]

	colorlen = len(colorlist)

	for hv, hd in enumerate(fg_array):
		for vv, vd in enumerate(hd):

			animount = (vv-hv)/(351*colorlen)+progress

			orgcolors = vd[0]/255, vd[1]/255, vd[2]/255
			bcolor = colorlist[int(((animount+0.5)*colorlen)%colorlen)]

			aflvl = (vd[3]/255)
			aplvl = 1-aflvl

			outcolor = []
			for cn in range(3):
				out = (bcolor[cn]*aplvl)+(orgcolors[cn]*aflvl)
				outcolor.append(out*255)

			vd[0:3] = outcolor
			vd[3] = 255

	out_array = fg_array

	data = Image.fromarray(out_array)
	data.save('out\\'+str(n).zfill(3)+'.png') 