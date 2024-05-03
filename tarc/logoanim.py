
from PIL import Image
import numpy as np
import math

fg = Image.open('tarclogo.bmp')
fg = fg.resize((512,512), Image.Resampling.BICUBIC)
fg_array = np.array(fg)

wg = Image.open('tarclogo.bmp')
wg = fg.resize((1536,1536), Image.Resampling.BICUBIC)
wg_array = np.array(fg)
wg.crop((0, 256, 1024, 1024-256))

numframes = 200

for n in range(numframes):
	print(n, numframes)

	wg_array = np.array(wg)
	wg_array = wg_array.astype(np.float64)/256

	fg_array = np.array(fg)
	fg_array = fg_array.astype(np.float64)/256

	progress = (n/numframes)
	bglvl = ((abs(0.5-progress))*8)-2.5
	bglvl = max(0, min(bglvl, 1))
	fg_array *= bglvl


	for x in range(512):
		for y in range(512):
			ym = (y+int(progress*2688))-768
			fg_array[x][y] += wg_array[x+500][ym] if 1536>ym>0 else 0


	out_array = (fg_array*256).astype(np.uint8)
	data = Image.fromarray(out_array)
	data.save('out\\'+str(n).zfill(3)+'.png') 