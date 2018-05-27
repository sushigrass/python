import numpy as np
import random
from PIL import Image


def main():
    pix = []
    for i in range(2500):
        x = []
        for q in range(2500):
            x.append((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        pix.append(x)

    array = np.array(pix,dtype=np.uint8)
    new = Image.fromarray(array)
    new.save('new.png')

if __name__ == "__main__": main()
