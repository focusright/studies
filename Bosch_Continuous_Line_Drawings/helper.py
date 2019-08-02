import random, math

GAMMA = 9 #between 4 and 9 inclusive
MAX_CITIES = 80000 #maximum cities that modern TSP solvers can handle
g_sum = 0

def quad_loop(px, M, N, K, func, drawer):
    for m in range(M):
        for n in range(N):
            ws = K * n  # width start
            we = ws + K # width end
            hs = K * m  # height start
            he = hs + K # height end
            u = 0
            for i in range(ws, we):
                for j in range(hs, he):
                    u += px[i, j]
            u //= (K*K) #mean grayscale value
            g = GAMMA - (GAMMA*u//256)
            func(g, ws, we, hs, he, drawer)

def scale_k(px, height, width, drawer): #scale k to match the capabilities of modern TSP solvers
    global g_sum
    count = 1
    K = math.gcd(width, height)
    M, N = 0, 0
    last_g_sum = 0
    while last_g_sum < MAX_CITIES:
        K = K // count**2 #we can evenly divide the k by k square by powers of 2's which are squares
        M = height // K #km rows of pixels
        N = width // K  #kn columns of pixels
        print (K, M, N)
        quad_loop(px, M, N, K, sum_g, drawer)
        count+=1
        last_g_sum = g_sum #as we divide the k square into smaller squares, g_sum will get bigger
        g_sum = 0
    return (K, M, N)

def sum_g(g, ws, we, hs, he, drawer):
    global g_sum
    g_sum += g

def render(px, K, M, N, drawer):
    quad_loop(px, M, N, K, drawpoints, drawer)
    #quad_loop(px, M, N, K, drawpath, drawer)

def drawpoints(g, ws, we, hs, he, drawer):
    points = get_points(g, ws, we, hs, he)
    pr = 10 #point radius
    for p in points:
        drawer.point((p[0], p[1]), 0)
        #drawer.ellipse([p[0], p[1], p[0]+pr, p[1]+pr], 0)
        #print(p[0], p[1])

def get_points(g, ws, we, hs, he):
    points = set()
    for count in range(g): 
        ri = random.randint(ws, we)
        rj = random.randint(hs, he)
        points.add((ri, rj))
    return points

def drawpath(g, ws, we, hs, he, drawer):
    points = get_points(g, ws, we, hs, he)
    
