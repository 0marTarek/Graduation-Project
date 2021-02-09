import cv2
import numpy as np
import pydicom as dicom
import os

folder_path = "E:/uinvirsty/4_fourth year/project/dataset/JPG_test"
#images_path = os.listdir(folder_path)

def get_images_from_path (folder_path):
    images_path = os.listdir(folder_path)
    pictures = []
    for image in images_path:
        picture = cv2.imread(os.path.join(folder_path, image)) 
        pictures.append(picture)
        
    
    return pictures 

#convert to gray

def to_gray(pectures):
    images = []
    for picture in pectures:
        img = cv2.cvtColor(picture,cv2.COLOR_BGR2GRAY) 
        images.append(img)
        #cv2.imshow("gray",img)
    
    return images 
        

    
#median filter
def to_filter(pectures):
    
    images = []
    for picture in pectures:
        img = cv2.medianBlur(picture, 3)
        images.append(img)
        
    
    return images 


# Now we apply threshold
def to_threshold(pectures):
    
    images = []
    for picture in pectures:
        ret, thresh = cv2.threshold(picture, 150, 255, cv2.THRESH_TOZERO) 
        #cv2.imshow('Threshold ', thresh)
        images.append(thresh)
        
    
    return images 

 

# Morphological Operations
def Morphological_Operations(pectures):
    
    images = []
    for thresh in pectures:
        kernel = np.ones((1, 1), np.uint8) 
        closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations = 2) 
        dist_transform = cv2.distanceTransform(closing, cv2.DIST_L2, 0) 
        ret, fg = cv2.threshold(dist_transform, 0.02 * dist_transform.max(), 255, 0) 
        
        images.append(fg)
        
    
    return images 


pec = get_images_from_path(folder_path)
pec = to_gray(pec)
cv2.imshow("gray",pec[0])
    
pec = to_filter(pec)
#cv2.imshow("gray",pec[26])
    
pec = to_threshold(pec)
#cv2.imshow("gray",pec[26])
    
pec = Morphological_Operations(pec)

#cv2.imshow("gray",pec[26])

    
# Free the memory, Deallocating
if cv2.waitKey(0) & 0xff == 25:  
    cv2.destroyAllWindows()
 


