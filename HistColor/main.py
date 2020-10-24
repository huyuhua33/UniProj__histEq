import cv2
import numpy as np
import matplotlib.pyplot as plt


def round(cdf, o, size, L):

    r = int((cdf[o])/(size) * (L-1))#
    if(r < 0):
        r = 0
    #print("cdf[o]>> "+str(cdf[o])+" cdf[min]>> "+str(cdf[min])+" r>> "+str(r))
    return r


def creatColorData(img):
    table = np.zeros([3, 256])
    print
    # print(table)
    for RGB in range(3):
        for i in img[:, :, RGB]:
            for j in i:
                # print(y)
                table[RGB][j] += 1
    return table


def findMin(table):
    min = 0
    table = np.array(table)
    for i in range(table.size):
        if( table[i] != 0 ):
            min = i
            break
    #print("min >> "+str(min))
    return min


def histColorConvert(table, img):
    cdf = np.cumsum(table)
    print("now is running.....")
    img2 = img.copy()
    height, width = img.shape
    for line in range(height):
        for pix in range(width-1):
            img2[line][pix] = round(cdf,img[line][pix],img.size,255)
    return img2


def showColorTable(table, color):

   # kwargs = dict(histtype='stepfilled',normed=1, alpha=0.75,  bins=40)
    plt.hist(table[0], histtype='stepfilled', stacked=True,
             alpha=0.75,  bins=40, color=color[0])
    plt.hist(table[1], histtype='stepfilled', stacked=True,
             alpha=0.75,  bins=40, color=color[1])
    plt.hist(table[2], histtype='stepfilled', stacked=True,
             alpha=0.75,  bins=40, color=color[2])
    #plt.hist(table,stacked= True,histtype='step',bins = 10, color = color[0])
    plt.show()


fileName = "HistColor/KT6av.png"

img = cv2.imread(fileName, -1)
table = creatColorData(img)
showColorTable(table, ['red', 'green', 'blue'])
img2 = img.copy()
img2[:,:,0] = histColorConvert(table[0],img[:,:,0]).copy()
img2[:,:,1] = histColorConvert(table[1],img[:,:,1]).copy()
img2[:,:,2] = histColorConvert(table[2],img[:,:,2]).copy()

table2 = creatColorData(img)
showColorTable(table2, ['red', 'green', 'blue'])
cv2.imshow("colorEq",img2)
cv2.imwrite("./new.jpg",img2)
#cv2.imshow("CV2.hist",cv2.equalizeHist(img))
cv2.waitKey()
