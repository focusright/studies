import random, math, tsp

GAMMA = 6 #between 4 and 9 inclusive
MAX_CITIES = 80000 #maximum cities that modern TSP solvers can handle
g_sum = 0
all_points = list()

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
    K = math.gcd(width, height)     #there is an implicit problem here that needs to be solved
    M, N = 0, 0                     #when the dimensions are weird and there are no good gcd 
    last_g_sum = 0                  #other than 1, how to find the closest dimension that makes
    while last_g_sum < MAX_CITIES:  #sensible k by k squares
        K = K // count**2 #we can evenly divide the k by k square by powers of 2's which are squares
        M = height // K #km rows of pixels
        N = width // K  #kn columns of pixels
        quad_loop(px, M, N, K, sum_g, drawer)
        print (K, M, N, g_sum)
        count+=1
        last_g_sum = g_sum #as we divide the k square into smaller squares, g_sum will get bigger
        g_sum = 0
        if K <= 3: #when k is less than 3 it doesn't make sense anymore
            break
    return (K, M, N)

def sum_g(g, ws, we, hs, he, drawer):
    global g_sum
    g_sum += g





def render_points(px, K, M, N, drawer):
    quad_loop(px, M, N, K, drawpoints, drawer)

def drawpoints(g, ws, we, hs, he, drawer):
    points = get_points(g, ws, we, hs, he)
    pr = 10 #point radius
    for p in points:
        drawer.point((p[0], p[1]), 0)
        #drawer.ellipse([p[0], p[1], p[0]+pr, p[1]+pr], 0)
        #print(p[0], p[1])

def get_points(g, ws, we, hs, he): #get points for one k by k square
    points = set()
    for count in range(g): 
        ri = random.randint(ws, we)
        rj = random.randint(hs, he)
        points.add((ri, rj))
    return points





def render_paths(px, K, M, N, drawer):
    quad_loop(px, M, N, K, accumulate_points, drawer)
    #tsp.create_data_model(all_points)
    path = tsp.run(all_points)
    #print(path)
    for i in range(len(path)-1):
        current = all_points[path[i]]
        next = all_points[path[i+1]]
        drawer.line([current, next], 0, 2)
    start = all_points[path[0]]
    end = all_points[path[len(path)-1]]
    drawer.line([end, start], 0, 1) #connect the first and last node to complete the drawing

def accumulate_points(g, ws, we, hs, he, drawer):
    global all_points
    points = get_points(g, ws, we, hs, he)
    for p in points:
        all_points.append(p)
    