
from PIL import Image
import numpy as np
import math

bg = Image.open('bg.png')
bg = bg.resize((210,210), Image.Resampling.NEAREST)
bg_array = np.array(bg)

fg = Image.open('fg.png')
fg =fg.resize((210,210), Image.Resampling.NEAREST)
fg_array = np.array(fg)

def hsv_to_rgb(h, s, v) -> tuple:
    h -= math.ceil(h)-1
    if s:
        if h == 1.0: h = 0.0
        i = int(h*6.0); f = h*6.0 - i
        w = v * (1.0 - s)
        q = v * (1.0 - s * f)
        t = v * (1.0 - s * (1.0 - f))
        if i==0: return (v, t, w)
        if i==1: return (q, v, w)
        if i==2: return (w, v, t)
        if i==3: return (w, q, v)
        if i==4: return (t, w, v)
        if i==5: return (v, w, q)
    else: return (v*255, v*255, v*255)

numframes = 64

for n in range(numframes):
	fg_array = np.array(fg)
	for v in fg_array:
		for p in v:
			lvl = p[0]/255
			p[0], p[1], p[2] = hsv_to_rgb(n/numframes, 1, ((lvl**0.7)*2)*255)

	out_array = bg_array+fg_array

	data = Image.fromarray(out_array)
	data.save('out\\'+str(n).zfill(3)+'.png') 