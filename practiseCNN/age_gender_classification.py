import zipfile
zip = zipfile.Zipfile("/content/utkface-new.zip",'r')
zip.extractall("/content")
zip.close()

immport os 
import numpy as np
import pandas as pd
import pandas as pd
from keras.preprocessing.image import ImageDataGenerator

folder_path = '/content/utkface_aligned_cropped/UTKFace'
age = []
gendre = []
img_path = []
for file in os.listdir(folder_path):
    age.append(int(file.split('_')[0]))
    gender.append(int(file.split('_')[1]))
    img_path.append(file)
len(age)
df = pd.DataFrame({'age':age,'gender':gender,'img':img_path})
df.shape
df.head()
train_df = df.sample(frac=1,random_state=0).iloc[:20000]
test_df = df.sample(frac=1,random_state=0).iloc[2000:]
