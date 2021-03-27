import glob
import os 
from random import randint
import shutil

path = input("Enter Patient path:")
imageTitlesPath = input("Enter image titles path in this form \\\\code\\\\VisualizationTools\\\\ImagesTitle.txt :")
text_files = glob.glob(path + "/**/*.dcm", recursive = True)

list_to_copy= {}
path_a = "E:\\FCIH\\4\\1st term\\Graduation Project\\code\\data\\a\\"
path_b = "E:\\FCIH\\4\\1st term\\Graduation Project\\code\\data\\b\\"
path_e = "E:\\FCIH\\4\\1st term\\Graduation Project\\code\\data\\e\\"
path_g = "E:\\FCIH\\4\\1st term\\Graduation Project\\code\\data\\g\\"


def search (finalResult, image_cat):
    counter = 0
    for imageT in finalResult:
        list_to_copy[imageT] = []
        for f in text_files:
            if imageT in f:
                list_to_copy[imageT].append(f)

    print(finalResult)
    for imageTitle in finalResult:
        if len(list_to_copy[imageTitle]) > 0 :
            if finalResult[imageTitle] > 1 :
                if image_cat[imageTitle] == 'A':
                    shutil.copy( list_to_copy[imageTitle][0],  path_a + image_cat[imageTitle] + str(randint(0, 1000000091)) + ".dcm")
                    shutil.copy( list_to_copy[imageTitle][1],  path_a + image_cat[imageTitle] + str(randint(0, 1000000091)) + ".dcm" )
                elif image_cat[imageTitle] == 'B':
                    shutil.copy( list_to_copy[imageTitle][0],  path_b + image_cat[imageTitle] + str(randint(0, 1000000091)) + ".dcm")
                    shutil.copy( list_to_copy[imageTitle][1],  path_b + image_cat[imageTitle] + str(randint(0, 1000000091)) + ".dcm")
                elif image_cat[imageTitle] == 'E':
                    shutil.copy( list_to_copy[imageTitle][0],  path_e + image_cat[imageTitle] + str(randint(0, 1000000091)) + ".dcm")
                    shutil.copy( list_to_copy[imageTitle][1],  path_e + image_cat[imageTitle] + str(randint(0, 1000000091)) + ".dcm")
                elif image_cat[imageTitle] == 'G':
                    shutil.copy(list_to_copy[imageTitle][0],   path_g +  image_cat[imageTitle] + str(randint(0, 1000000091)) + ".dcm")    
                    shutil.copy(list_to_copy[imageTitle][1],   path_g + image_cat[imageTitle] + str(randint(0, 1000000091)) + ".dcm")    
            elif finalResult[imageTitle] > 0 :
                if image_cat[imageTitle] == 'A':
                    shutil.copy( list_to_copy[imageTitle][0],  path_a + image_cat[imageTitle] + str(randint(0, 1000000091)) + ".dcm")
                elif image_cat[imageTitle] == 'B':
                    shutil.copy( list_to_copy[imageTitle][0],  path_b + image_cat[imageTitle] + str(randint(0, 1000000091)) + ".dcm")
                elif image_cat[imageTitle] == 'E':
                    shutil.copy( list_to_copy[imageTitle][0],  path_e + image_cat[imageTitle] + str(randint(0, 1000000091)) + ".dcm")
                elif image_cat[imageTitle] == 'G':
                    shutil.copy(list_to_copy[imageTitle][0],   path_g +  image_cat[imageTitle] + str(randint(0, 1000000091)) + ".dcm")    
        else:
            print("There's no dcm files for file with name: " + str(imageTitle))




def read(path):
    file = open(path , 'r')
    Lines = file.readlines()
    count = 0
    titles = []
    image_cat = {}
    for line in Lines:
        count += 1
        image , cat = line.strip().split(';')
        titles.append(image)
        image_cat[image] = cat
    c = 0
    finalResult = {}
    for element in titles:
        for line in Lines:
            if element in line:
                c += 1
        finalResult[element] = c
        c = 0
    return finalResult, image_cat
        #search(image , cat)
    

#search("1-02.dcm", 'A')
#print(list_to_copy)
#E:\\FCIH\\4\\1st term\\Graduation Project\\code\\VisualizationTools\\ImagesTitle.txt
res1, res2 = read(imageTitlesPath)
print(res1)
search(res1, res2)
