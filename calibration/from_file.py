import cv2 as cv
import numpy as np
import glob

ret, mtx, dist, rvecs, tvecs = np.load('calib.npz').values()
images = glob.glob('png/*.png')

for image in images:
    img = cv.imread(image)
    h,  w = img.shape[:2]
    newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))

    # undistort
    dst = cv.undistort(img, mtx, dist, None, newcameramtx)
    # crop the image
    x, y, w, h = roi
    # dst = dst[y:y+h, x:x+w]
    cv.imshow('image',dst)
    cv.waitKey(0)

    # undistort
    mapx, mapy = cv.initUndistortRectifyMap(mtx, dist, None, newcameramtx, (w,h), 5)
    dst = cv.remap(img, mapx, mapy, cv.INTER_LINEAR)
    # crop the image
    x, y, w, h = roi
    # dst = dst[y:y+h, x:x+w]
    cv.imshow('image',dst)
    cv.waitKey(0)
cv.destroyAllWindows()