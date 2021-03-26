import glob
import os 
from random import randint
import shutil

path = input("Enter Patient path:")

text_files = glob.glob(path + "/**/*.dcm", recursive = True)

print(text_files)

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
        try:
            if category == 'A':
                shutil.copy( list_to_copy[0],  'F:\\categories\\A\\' + str(category) + str(randint(0, 1000000091)) + ".dcm")
            elif category == 'B':
                shutil.copy( list_to_copy[0],  'F:\\categories\\B\\' + str(category) + str(randint(0, 1000000091)) + ".dcm")
            elif category == 'D':
                shutil.copy( list_to_copy[0],  'F:\\categories\\D\\' + str(category) + str(randint(0, 1000000091)) + ".dcm")
            elif category == 'G':
                shutil.copy(list_to_copy[0],   'F:\\categories\\G\\' +  str(category) + str(randint(0, 1000000091)) + ".dcm")    
        except :
            print('catech entered')

    if counter > 1 :
        try:
                
            if category == 'A':
                shutil.copy( list_to_copy[1],  'F:\\categories\\A\\' + str(category) + str(randint(0, 1000000091)) + ".dcm" )
            elif category == 'B':
                shutil.copy( list_to_copy[1],  'F:\\categories\\B\\' + str(category) + str(randint(0, 1000000091)) + ".dcm")
            elif category == 'D':
                shutil.copy( list_to_copy[1],  'F:\\categories\\D\\' + str(category) + str(randint(0, 1000000091)) + ".dcm")
            elif category == 'G':
                shutil.copy(list_to_copy[1],   'F:\\categories\\G\\' + str(category) + str(randint(0, 1000000091)) + ".dcm")
        except e:
            print('catech entered')


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
read('C:\\Users\\ESLAM\\Downloads\\New folder (3)\\VisualizationTools\\ImagesTitle.txt')
