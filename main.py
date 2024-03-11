import os
import numpy as np
import cv2 as cv
from PIL import Image
from model import *
from homo import *
import matplotlib.pyplot as plt



image_folder_name = 'ER/'
result_folder_name = 'RE/'

files = os.listdir(image_folder_name)

for i in files:
    image = cv.imread(image_folder_name + i)
    # # ebrahim = cv.normalize(ebrahim, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)
    img = image / 255.
    img = np.expand_dims(img, axis=0)
    predictions = style(img) > 0.2
    unet_bool_val = np.multiply(predictions, 1)
    normalize = cv.normalize(unet_bool_val, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)
    UnetMask = np.squeeze(normalize, axis=0)
    UnetMask = np.squeeze(UnetMask, axis=2)

    kernel = np.ones((2, 2), np.uint8)
    # kernel1 = np.ones((3, 3), np.uint8)
    erode = cv.dilate(UnetMask, kernel, iterations=1)
    # erode2 = cv.dilate(UnetMask, kernel, iterations=1)
    Mask = cv.GaussianBlur(erode, (3, 3), 5)
    # Mask2 = cv.GaussianBlur(erode, (5, 5), 5)


    X = homo(image, Mask)
    # X = Image.fromarray(X)
    # X.save(result_folder_name + i)
    plt.imsave(result_folder_name + i, (cv.cvtColor(X, cv.COLOR_BGR2RGB)))

plt.gray()
plt.imsave('mask.png', Mask)