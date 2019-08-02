from PIL import Image, ImageDraw
import sys, math, random
import helper1

im = Image.open( 'wall.jpg' )
im = im.convert('L') # convert to grayscale
#im.save('greyscale.png')
width, height = im.size
px = im.load()
#print(px[40,40])
#print(width, height)
K = math.gcd(width, height)//49
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
        sum = 0
        for i in range(ws, we):
            for j in range(hs, he):
                sum += px[i, j]
        sum //= (K*K)
        #print(sum)
        points = set()
        for mgv in range(sum): #mean grayscale value
            ri = random.randint(ws, we)
            rj = random.randint(hs, he)
            points.add((ri, rj))
        pr = 10 #point radius
        for p in points:
            draw.point((p[0], p[1]), 0)
            #draw.ellipse([p[0], p[1], p[0]+pr, p[1]+pr], 0)
            #print(p[0], p[1])


ni.show()