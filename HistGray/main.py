import cv2
import numpy as np
import matplotlib.pyplot as plt

def round(cdf,o,size,L):
    
    r = int((cdf[o])/(size) * (L-1))#
    if(r < 0) :
        r = 0
    #print("cdf[o]>> "+str(cdf[o])+" cdf[min]>> "+str(cdf[min])+" r>> "+str(r))
    return r

def creatGrayData(img):
    table = [0]*255
    # print(table)
    for i in img:
        for j in i:
            # print(y)
            table[j] += 1
    return table

def findMin(table):
    min = 0
    table = np.array(table)
    for i in range(table.size):
        if(table[i] != 0):
            min = i
            break
    #print("min >> "+str(min))
    return min

def histGrayConvert(table, img):
    cdf = np.cumsum(table)
    print("now is running.....")
    img2 = img.copy()
    height, width = img.shape
    for line in range(height):
        for pix in range(width-1):
            img2[line][pix] = round(cdf,img[line][pix],img.size,255)
    print(img2)
    print("running finish")
    cv2.imwrite("new.jpg", img2)
    cv2.waitKey()
    return img2


def showGrayTable(table,color):
    
    plt.hist(table,bins = 10, color = color)
    plt.show()


fileName = "Unequalized_Hawkes_Bay_NZ.jpg"

img = cv2.imread(fileName, 0)
print(img)
'''
cv2.imshow("org", img)
cv2.waitKey()
'''
table = creatGrayData(img)
showGrayTable(table,'gray')
tab2 = findMin(np.array(table))

#findMin(np.array(table))
img2 = histGrayConvert(table, img)
table2 = creatGrayData(img2)
plt.hist([table,table2],bins = 10, color = ['black','gray'])
plt.show()
for i in range (255):
    print(str(i) +" Org: "+ str(table[i]) + " Hist: "+ str(table2[i]))

cv2.imshow("histEq", img2)
cv2.waitKey()
