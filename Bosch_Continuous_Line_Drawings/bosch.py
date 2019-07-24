from PIL import Image, ImageDraw
import math, random

im = Image.open( 'wall.jpg' )
im = im.convert('L') # convert to grayscale
#im.save('greyscale.png')
width, height = im.size
px = im.load()
#print(px[40,40])
#print(width, height)
K = math.gcd(width, height)
M = height // K #km rows of pixels
N = width // K  #kn columns of pixels
#print(K)

ni = Image.new('L', (width, height), 255) #ni = new image
draw = ImageDraw.Draw(ni)

for m in range(M):
    for n in range(N):
        ws = K * n  # width start
        we = ws + K # width end
        hs = K * m  # height start
        he = hs + K # height end
        r = random.randint(0, 255)
        for i in range(ws, we):
            for j in range(hs, he):
                draw.point((i, j), r)

ni.show()