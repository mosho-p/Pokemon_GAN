import cv2
import os


for x in os.listdir('./data/'):
    if x[-4:] != '.png' or x.find('flip') != -1:
        continue
    img = cv2.imread('./data/{}'.format(x))
    cv2.imwrite('./data/{}_flip.png'.format(x.split('.')[0]), img[:,::-1,:])