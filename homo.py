import cv2 as cv
import numpy as np


def distance(point1, point2):
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def gaussian(D0, imgShape):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows / 2, cols / 2)
    for x in range(cols):
        for y in range(rows):
            base[y, x] = np.exp(((-distance((y, x), center) ** 2) / (2 * (D0 ** 2))))
    return base


# Separate Ref and Ill components for B channel
def homo(img, Mask):
    b, g, r = cv.split(img)
    imgLb = np.log(b + 0.01)
    Maskb = gaussian(30, b.shape)
    imgFb = np.fft.fftshift(np.fft.fft2(imgLb))
    LUMb = imgFb * Maskb
    REFb = imgFb * (1 - Maskb)
    lumb = np.exp(np.fft.ifft2(np.fft.ifftshift(LUMb)))
    reflectb = np.exp(np.fft.ifft2(np.fft.ifftshift(REFb)))
    Refb = np.abs(reflectb)
    Lumb = np.abs(lumb)
    RefB = Refb.astype(np.float32)
    LumB = Lumb.astype(np.float32)

    # Separate Ref and Ill components for G channel
    imgLg = np.log(g + 0.01)
    Maskg = gaussian(30, g.shape)
    imgFg = np.fft.fftshift(np.fft.fft2(imgLg))
    LUMg = imgFg * Maskg
    REFg = imgFg * (1 - Maskg)
    lumg = np.exp(np.fft.ifft2(np.fft.ifftshift(LUMg)))
    reflectg = np.exp(np.fft.ifft2(np.fft.ifftshift(REFg)))
    Refg = np.abs(reflectg)
    Lumg = np.abs(lumg)
    RefG = Refg.astype(np.float32)
    LumG = Lumg.astype(np.float32)

    # Separate Ref and Ill components for R channel
    imgLr = np.log(r + 0.01)
    Maskr = gaussian(30, r.shape)
    imgFr = np.fft.fftshift(np.fft.fft2(imgLr))
    LUMr = imgFr * Maskr
    REFr = imgFr * (1 - Maskr)
    lumr = np.exp(np.fft.ifft2(np.fft.ifftshift(LUMr)))
    reflectr = np.exp(np.fft.ifft2(np.fft.ifftshift(REFr)))
    Refr = np.abs(reflectr)
    Lumr = np.abs(lumr)
    RefR = Refr.astype(np.float32)
    LumR = Lumr.astype(np.float32)

    # Inpainting for each component separately
    # B channel
    Iib = cv.inpaint(LumB, Mask, 1, cv.INPAINT_NS)
    Rib = cv.inpaint(RefB, Mask, 1, cv.INPAINT_NS)

    # G channel
    Iig = cv.inpaint(LumG, Mask, 1, cv.INPAINT_NS)
    Rig = cv.inpaint(RefG, Mask, 1, cv.INPAINT_NS)

    # R channel
    Iir = cv.inpaint(LumR, Mask, 1, cv.INPAINT_NS)
    Rir = cv.inpaint(RefR, Mask, 1, cv.INPAINT_NS)

    # Compounding any component of each channel
    B = Rib * Iib
    G = Rig * Iig
    R = Rir * Iir

    # B = RefB * Iib
    # G = RefG * Iig
    # R = RefR * Iir
    bgr = (np.dstack((B, G, R))).astype(np.uint8)


    # # ## Trsnsform to YUV color model
    # yuv = cv.cvtColor(bgr, cv.COLOR_BGR2YUV)
    # y, u, v = cv.split(yuv)
    # imgLy = np.log(y + 0.01)
    # Masky = gaussian(30, y.shape)
    # imgFy = np.fft.fftshift(np.fft.fft2(imgLy))
    # LUMy = imgFy * Masky
    # REFy = imgFy * (1 - Masky)
    # lumy = np.exp(np.fft.ifft2(np.fft.ifftshift(LUMy)))
    # reflecty = np.exp(np.fft.ifft2(np.fft.ifftshift(REFy)))
    # Refy = np.abs(reflecty)
    # Lumy = np.abs(lumy)
    # RefY = Refy.astype(np.float32)
    # LumY = Lumy.astype(np.float32)
    #
    # # Separate Ref and Ill components for G channel
    # imgLu = np.log(u + 0.01)
    # Masku = gaussian(30, u.shape)
    # imgFu = np.fft.fftshift(np.fft.fft2(imgLu))
    # LUMu = imgFu * Masku
    # REFu = imgFu * (1 - Masku)
    # lumu = np.exp(np.fft.ifft2(np.fft.ifftshift(LUMu)))
    # reflectu = np.exp(np.fft.ifft2(np.fft.ifftshift(REFu)))
    # Refu = np.abs(reflectu)
    # Lumu = np.abs(lumu)
    # RefU = Refu.astype(np.float32)
    # LumU = Lumu.astype(np.float32)
    #
    # # Separate Ref and Ill components for R channel
    # imgLv = np.log(v + 0.01)
    # Maskv = gaussian(30, v.shape)
    # imgFv = np.fft.fftshift(np.fft.fft2(imgLv))
    # LUMv = imgFv * Maskv
    # REFv = imgFv * (1 - Maskv)
    # lumv = np.exp(np.fft.ifft2(np.fft.ifftshift(LUMv)))
    # reflectv = np.exp(np.fft.ifft2(np.fft.ifftshift(REFv)))
    # Refv = np.abs(reflectv)
    # Lumv = np.abs(lumv)
    # RefV = Refv.astype(np.float32)
    # LumV = Lumv.astype(np.float32)
    #
    # thresh_RV = cv.normalize(RefV, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)
    # threshRV = cv.adaptiveThreshold(thresh_RV, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 3, 21)
    # MASK2 = cv.GaussianBlur(threshRV, (3, 3), 5)
    #
    # Iy = cv.inpaint(LumY, Mask2, 1, cv.INPAINT_NS) #MASK2
    # Ry = cv.inpaint(RefY, Mask2, 1, cv.INPAINT_NS)
    #
    # Iu = cv.inpaint(LumU, Mask2, 1, cv.INPAINT_NS)
    # Ru = cv.inpaint(RefU, Mask2, 1, cv.INPAINT_NS)
    #
    # Iv = cv.inpaint(LumV, Mask2, 1, cv.INPAINT_NS)
    # Rv = cv.inpaint(RefV, Mask2, 1, cv.INPAINT_NS)
    #
    # Y = Ry * Iy
    # U = Ru * Iu
    # V = Rv * Iv
    # YUV = (np.dstack((Y, U, V))).astype(np.uint8)
    # BGR = cv.cvtColor(YUV, cv.COLOR_YUV2BGR)
    return bgr

