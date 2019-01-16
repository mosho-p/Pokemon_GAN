import requests
import numpy as np
import cv2

for x in range(1, 810):
    r = requests.get('https://assets.pokemon.com/assets/cms2/img/pokedex/detail/{:03d}.png'.format(x))
    if r.status_code != 200:
        print('error', str(x))
    else:
        print('success', str(x))
    arr = np.asarray(bytearray(r.content), dtype=np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_UNCHANGED)
    for i in range(3):
        img[:, :, i][img[:, :, 3] == 0] = 1
    cv2.imwrite('./data/{:03d}.png'.format(x), img[:,:,:3])
