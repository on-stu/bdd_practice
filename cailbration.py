# Import required modules
import cv2
import numpy as np
import glob
images = glob.glob('png/*.png')



mtx = np.array([[840.18, 0, 682.59],
                    [0,840.02,488.92],
                    [0, 0, 1]])

# mtx = np.array([[978.1519889,    0,         672.68264606],
#  [  0,         977.95989291, 466.20234582],
#  [  0,          0,           1        ]])

# dist = np.array([[[-0.3354, 0.0943]]])

dist = np.array([[-0.58779395,  0.45808059,  0.00308834, -0.00103879 -0.19308463]])

for image in images:
    img = cv2.imread(image)
    h,  w = img.shape[:2]
    newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx ,dist,(w,h),1,(w,h))
    dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
    # x, y, w, h = roi
    # dst = dst[y:y+h, x:x+w]
    cv2.imshow("img", dst)
    cv2.waitKey(0)
cv2.destroyAllWindows()

# img = cv2.imread(images[1])

# h, w = img.shape[:2]

# newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx ,dist,(w,h),1,(w,h))
# dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
# x, y, w, h = roi
# dst = dst[y:y+h, x:x+w]

# cv2.imshow("img", dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
	