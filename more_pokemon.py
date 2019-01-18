import requests
import numpy as np
import cv2
import os

if not os.path.exists('./pngs'):
    os.mkdir('./pngs')
for x in range(1, 810):
    r = requests.get('https://assets.pokemon.com/assets/cms2/img/pokedex/detail/{:03d}.png'.format(x))
    if r.status_code != 200:
        print('error', str(x))
    else:
        print('success', str(x))
    arr = np.asarray(bytearray(r.content), dtype=np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_UNCHANGED)
    cv2.imwrite('./pngs/{:03d}.png'.format(x), img)
