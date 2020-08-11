def isPointInCircle(x,y,r,center=(0,0)):
    if ((x-center[0])**2 + (y-center[1])**2 < (r**2)) or ((x-center[0])**2 + (y-center[1])**2 == (r**2)) :
        return True
    elif (x-center[0])**2 + (y-center[1])**2 > (r**2) :
        return False
    
    
import random

def generateRandomSquarePoints(n,length,center=(0,0)):
    minx = center[0]-length/2
    miny = center[1]-length/2
    maxx = center[0]+length/2
    maxy = center[1]+length/2
  
    points = [[random.uniform(minx,maxx),random.uniform(miny,maxy)] for i in range (n)]

    return points


def MCCircleArea(r,n=100,center=(0,0)):
    jumlah_pointincircle =0
    points = generateRandomSquarePoints (n,2*r,center)

    for i in range (n) :
        if (isPointInCircle (points[i][0],points[i][1],r,center)) == True :
            jumlah_pointincircle +=1
  
    luas_lingkaran = (jumlah_pointincircle/n)*((2*r)**2)
  
    return luas_lingkaran


def LLNPiMC(nsim,nsample):
    total_area = 0
  
    for i in range (nsim) :
        luas_lingkaran = MCCircleArea(1,nsample)
        total_area = total_area + luas_lingkaran
  
    pi_average = total_area/nsim
  
    return pi_average


def relativeError(act,est):
    error_relative = ((est-act)/act)*100
  
    return abs(error_relative)
