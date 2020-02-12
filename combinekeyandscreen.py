import time
import numpy as np
from getkeys import key_check
from PIL import ImageGrab
import cv2
"""
w
s
a
d
j
k
l
wa
wd
wj
wk
wl
sa
sd
sj
sk
sl
dj
dk
dl
aj
ak
al
no key
we need 24 identifier
"""

id = np.identity(24)
w = id[0]
s = id[1]
a = id[2]
d = id[3]
j = id[4]
k = id[5]
l = id[6]
wa = id[7]
wd = id[8]
wj = id[9]
wk = id[10]
wl = id[11]
sa = id[12]
sd = id[13]
sj = id[14]
sk = id[15]
sl = id[16]
dj = id[17]
dk = id[18]
dl = id[19]
aj = id[20]
ak = id[21]
al = id[22]
nk = id[23]

def keys_to_output(keys):
    output = np.zeros(24)
    if 'W' in keys and 'A' in keys:
        output = wa
    elif 'W' in keys and 'D' in keys:
        output = wd
    elif 'W' in keys and 'J' in keys:
        output = wj
    elif 'W' in keys and 'K' in keys:
        output = wk
    elif 'W' in keys and 'L' in keys:
        output = wl
    elif 'S' in keys and 'A' in keys:
        output = sa
    elif 'S' in keys and 'D' in keys:
        output = sd
    elif 'S' in keys and 'J' in keys:
        output = sj
    elif 'S' in keys and 'K' in keys:
        output = sk
    elif 'S' in keys and 'L' in keys:
        output = sl
    elif 'D' in keys and 'J' in keys:
        output = dj
    elif 'D' in keys and 'K' in keys:
        output = dk
    elif 'D' in keys and 'L' in keys:
        output = dl
    elif 'A' in keys and 'J' in keys:
        output = aj
    elif 'A' in keys and 'K' in keys:
        output = ak
    elif 'A' in keys and 'L' in keys:
        output = al
    elif 'W' in keys:
        output = w
    elif 'S' in keys:
        output = s
    elif 'A' in keys:
        output = a
    elif 'D' in keys:
        output = d
    elif 'J' in keys:
        output = j
    elif 'K' in keys:
        output = k
    elif 'L' in keys:
        output = l
    else:
        output = nk
    return output

"""
tuş kombinasyonlarını matematik olarak ifade et
fonksiyon:
    dur denmediği takdirde
    her 10 salisede
    ekran görüntüsünü al
    kullanıcı girdisini al- kullanıcıdan tuşları al-
    tuş girdisini matematiksel olarak ifade et- one hot encoding-
    kaydet
"""

def collect_data():
    imagedata = np.array([])
    keydata = np.array([])
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)
    noquit = True
    count = 0
    while(noquit):

        #if (keys):
        last_time = time.time()
        screen = np.array(ImageGrab.grab(bbox=(100,150,660,590)))
        screenarray = np.array(cv2.resize(screen,(224,224)))
        imagedata = np.append(imagedata, screenarray)

        keys = key_check()
        print(keys)
        keyarray = keys_to_output(keys)
        keydata = np.append(keydata, keyarray)

        count = count + 1
        print("loop took {} seconds".format(time.time()-last_time))
        last_time = time.time()

        cv2.imshow('ekran', cv2.cvtColor(screenarray, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

        if count % 140 == 0 :
            file_name = "metalslug-%d"%count
            np.save(file_name+"key.npy",keydata)
            np.save(file_name+"screen.npy",imagedata)
            print("SAVEDDDKAYDETDTTETTDTDEKAYDET")
            keydata = np.array([])
            imagedata = np.array([])

        if 'Q' in keys:
            noquit = False

collect_data()