import glob
import os 
from random import randint
import shutil

path = input("Enter Patient path:")

text_files = glob.glob(path + "/**/*.dcm", recursive = True)

print(type(text_files))

list_to_copy= []

def search (name, category):
    counter = 0
    for f in text_files:
        if name in f :
            counter +=1 
            list_to_copy.append(f)
        else:
            pass
    if counter>0:
        if category == 'A':
            os.rename( list_to_copy[0],  'C:\\Users\\Omar-ElQady\\OneDrive - Faculty of Computers and Information\\Desktop\\output\\A\\' + str(category) + str(randint(0, 1000000091)) + ".dcm")
        elif category == 'B':
            os.rename( list_to_copy[0],  'C:\\Users\\Omar-ElQady\\OneDrive - Faculty of Computers and Information\\Desktop\\output\\B\\' + str(category) + str(randint(0, 1000000091)) + ".dcm")
        elif category == 'E':
            os.rename( list_to_copy[0],  'C:\\Users\\Omar-ElQady\\OneDrive - Faculty of Computers and Information\\Desktop\\output\\E\\' + str(category) + str(randint(0, 1000000091)) + ".dcm")
        elif category == 'G':
            os.rename(list_to_copy[0],  'C:\\Users\\Omar-ElQady\\OneDrive - Faculty of Computers and Information\\Desktop\\output\\G\\' +  str(category) + str(randint(0, 1000000091)) + ".dcm")    


    if counter > 1 :
        if category == 'A':
            os.rename( list_to_copy[1],  'C:\\Users\\Omar-ElQady\\OneDrive - Faculty of Computers and Information\\Desktop\\output\\A\\' + str(category) + str(randint(0, 1000000091)) + ".dcm" )
        elif category == 'B':
            os.rename( list_to_copy[1],  'C:\\Users\\Omar-ElQady\\OneDrive - Faculty of Computers and Information\\Desktop\\output\\B\\' + str(category) + str(randint(0, 1000000091)) + ".dcm")
        elif category == 'E':
            os.rename( list_to_copy[1],  'C:\\Users\\Omar-ElQady\\OneDrive - Faculty of Computers and Information\\Desktop\\output\\E\\' + str(category) + str(randint(0, 1000000091)) + ".dcm")
        elif category == 'G':
            os.rename(list_to_copy[1],  'C:\\Users\\Omar-ElQady\\OneDrive - Faculty of Computers and Information\\Desktop\\output\\G\\' + str(category) + str(randint(0, 1000000091)) + ".dcm")    



def read(path):
    file = open(path , 'r')
    Lines = file.readlines()
    count = 0

    for line in Lines:
        count += 1
        image , cat = line.strip().split(';')
        search(image , cat)
    

search("1-02.dcm", 'A')
print(list_to_copy)
read('C:\\Users\\Omar-ElQady\\OneDrive - Faculty of Computers and Information\Desktop\\VisualizationTools\\ImagesTitle.txt')