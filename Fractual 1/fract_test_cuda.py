from PIL import Image, ImageDraw

import numba 
from numba import cuda 
from numba import jit


from datetime import datetime
import numpy


MAX_ITER = 20

def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1
    return n

@numba.jit
def fract_test(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER: #compute magnitude of z and check if less than max iteration
        z = z*z + c
        n += 1
    return n

# def draw_fractal(scale):
# 	# Image size (pixels)
# 	WIDTH = 1000
# 	HEIGHT = 800

# 	# Plot window
# 	RE_START = -2
# 	RE_END = 1
# 	IM_START = -1
# 	IM_END = 1

# 	palette = []

# 	im = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
# 	draw = ImageDraw.Draw(im)

	

# 	for x in range(0, WIDTH):

# 		if ((x % 100) == 0):
# 			print("Percent Complete " + str((x/WIDTH)*100) + "%" )

# 		for y in range(0, HEIGHT):
# 			# Convert pixel coordinate to complex number
# 			c = complex(RE_START+(x/WIDTH/scale)*(RE_END-RE_START),IM_START+(y/HEIGHT/scale)*(IM_END-IM_START))
# 			# Compute the number of iterations
# 			# m = mandelbrot(c)
# 			m = fract_test(c)
# 			cuda.profile_stop()
# 			# The color depends on the number of iterations

# 			#color = 255 - int(m * 255 / MAX_ITER)

# 			red = 255 - int(m * 255 / MAX_ITER)
# 			green = int((255 - int(m * 255 / MAX_ITER))*(x/WIDTH))
# 			blue = int((255 - int(m * 255 / MAX_ITER))*(y/HEIGHT))


# 			# Plot the point
# 			draw.point([x, y], (red, green, blue))

# 	now = datetime.now()

# 	current_time = now.strftime("%H_%M_%S")

# 	im.save("output\\" + current_time + '.png', 'PNG')	


def draw_fractal(scale):
	# Image size (pixels)
	WIDTH = 1000
	HEIGHT = 800

	# Plot window
	RE_START = -2
	RE_END = 1
	IM_START = -1
	IM_END = 1

	palette = []

	im = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
	draw = ImageDraw.Draw(im)


	for x in range(0, WIDTH):
		for y in range(0, HEIGHT):

			


c = complex(RE_START+(x/WIDTH/scale)*(RE_END-RE_START),IM_START+(y/HEIGHT/scale)*(IM_END-IM_START))
if __name__=="__main__":
	draw_fractal(2)

#data = numpy.zeros((WIDTH, HEIGHT))

#print(data)