from PIL import Image, ImageDraw
import sys
import helper

im = Image.open(sys.argv[1])
im = im.convert('L') # convert to grayscale
#im.save('greyscale.png')
width, height = im.size
px = im.load()

if len(sys.argv) == 3:
    helper.MAX_CITIES = int(sys.argv[2])
elif len(sys.argv) == 4:
    helper.MAX_CITIES = int(sys.argv[2])
    helper.GAMMA = int(sys.argv[3])

ni = Image.new('L', (width, height), 255) #ni = new image
drawer = ImageDraw.Draw(ni)

K, M, N = helper.scale_k(px, height, width, drawer)

#helper.render_points(px, K, M, N, drawer)
helper.render_paths(px, K, M, N, drawer)

ni.show()