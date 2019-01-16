# resize pokeGAN.py
import os
import cv2

def resize(size=256, src="./data", dst="./resizedData"):
    if not os.path.exists(dst):
        os.mkdir(dst)

    for each in os.listdir(src):
        img = cv2.imread(os.path.join(src, each), cv2.IMREAD_UNCHANGED)
        for i in range(3):
            img[:, :, i][img[:, :, 3] == 0] = 1
        img = cv2.resize(img, (size, size))
        cv2.imwrite(os.path.join(dst, each), img[:, :, :3])
