import numpy as np
import cv2

def template_matcher(image_path:str, template_path:str):
    img = cv2.resize(cv2.imread(image_path, 0), (0, 0), fx=0.8, fy=0.8)
    template = cv2.resize(cv2.imread(template_path, 0), (0, 0), fx=0.8, fy=0.8)
    h, w = template.shape

    methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
    for method in methods:
        img2 = img.copy()

        result = cv2.matchTemplate(img2, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            location = min_loc
        else:
            location = max_loc
        
        bottom_right = (location[0] + w, location[1] + h)
        mid_point = (int((location[0]+bottom_right[0])/2),int((location[1]+bottom_right[1])/2))
        print('Mid Point:', mid_point)
        print(location,bottom_right, '\n\n')
        cv2.rectangle(img2, location, bottom_right, 255, 5)
        cv2.circle(img2, mid_point, 5, (0, 0, 0), 10)
        cv2.imshow('Match', img2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

template_matcher('assets/soccer_practice.jpg', 'assets/ball.PNG')
