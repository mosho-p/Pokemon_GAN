import os
import cv2

def sort_imgs():
    if not os.path.exists('./reds'):
        os.mkdir('./reds')
    if not os.path.exists('./blues'):
        os.mkdir('./blues')
    if not os.path.exists('./greens'):
        os.mkdir('./greens')
    for img in os.listdir('./pngs'):
        if img[-4:] != '.png':
            continue
        pokemon = cv2.imread('./pngs/{}'.format(img), -1) # loads in BGR
        if prim_color(pokemon) == 0:
            for i in range(3):
                pokemon[:, :, i][pokemon[:, :, 3] == 0] = 255
            cv2.imwrite('./blues/{}'.format(img), pokemon[:,:,:3])
        if prim_color(pokemon) == 1:
            for i in range(3):
                pokemon[:, :, i][pokemon[:, :, 3] == 0] = 255
            cv2.imwrite('./greens/{}'.format(img), pokemon[:,:,:3])
        if prim_color(pokemon) == 2:
            for i in range(3):
                pokemon[:, :, i][pokemon[:, :, 3] == 0] = 255
            cv2.imwrite('./reds/{}'.format(img), pokemon[:,:,:3])
    flip_images('./reds')
    flip_images('./greens')
    flip_images('./blues')

def flip_images(dir):
    for x in os.listdir(dir):
        if x[-4:] != '.png' or x.find('flip') != -1:
            continue
        img = cv2.imread('{}/{}'.format(dir, x))
        cv2.imwrite('{}/{}_flip.png'.format(dir, x.split('.')[0]), img[:, ::-1, :])


def prim_color(img):
  return max([(img[:, :, x][img[:, :, 3] != 0].mean(), x) for x in range(3)])[1]

if __name__ == '__main__':
    sort_imgs()