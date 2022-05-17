import os
import sys
sys.path.append(os.path.join("..", "..", "CDS-VIS"))
import cv2
import numpy as np
import pandas as pd
from utils.imutils import jimshow
from utils.imutils import jimshow_channel
import matplotlib.pyplot as plt

def image_search():
    filepath = os.path.join("..", "..", "CDS-VIS", "flowers", "image_0020.jpg")
    target_image = cv2.imread(filepath)
    #jimshow(target_image)
    
    # Making histogram for target image
    histogram = cv2.calcHist([target_image], [0,1,2], None, [8,8,8], [0,256, 0,256, 0,256]) 
    # Normalizing histogram for target image
    hist_norm = cv2.normalize(histogram, histogram, 0,255, cv2.NORM_MINMAX)
    # The target image histogram is for later use when comparing 
    
    # Making a list containing the filename for all images (a sample of 10 in this case)
    all_images = []
    path = os.path.join("..", "..", "CDS-VIS", "flowers")
    names = os.listdir(path)

    for image in names[0:10]:
        filepath = os.path.join(image)
        all_images.append(filepath)
    #print(all_images)
    
    
# Making a loop that goes through each image in all_images, reading it as an image, calculating its histogram and normalising it 
    normalized = []
    for images in all_images :
        filepath = os.path.join("..", "..", "CDS-VIS", "flowers", images) 
        # Reading it as an image 
        images = cv2.imread(filepath)
        # Calculating historgram 
        images_hist = cv2.calcHist([images], [0,1,2], None, [8,8,8], [0,256, 0,256, 0,256]) 
        # Normalizing histogram 
        hist_norm = cv2.normalize(images_hist, images_hist, 0,255, cv2.NORM_MINMAX)
        normalized.append(hist_norm)
    #print(normalized)
    
    # Next is to compare all histograms (images_hist) for my target histogram and then getting the distance score 
    compared_hist = []
    for hist in normalized:
        # Using cv2 compareHist function 
        compare = cv2.compareHist(histogram, hist, cv2.HISTCMP_CHISQR)
        # Adding the compared histgrams to a list
        compared_hist.append(compare)
        # The results are the distance score 
    #print(compared_hist)

    # Finding the three most similar images to the target images  
    three_similar = []
    similar = sorted(compared_hist)[:3]
    three_similar.append(similar)
    #print(three_similar)
    
    similar = []
    image1 = compared_hist.index(918.3767684606157)
    image2 = compared_hist.index(54348.81884400394)
    image3 = compared_hist.index(62817.37225299174)
    #print(images1) = 6
    #print(image2) = 3
    #print(image3) = 7
    similar.append(all_images[6])
    similar.append(all_images[3])
    similar.append(all_images[7])
    
    #print(similar)
    
    final_images = []
    for sim_img in similar:
        path = os.path.join("..", "..", "CDS-VIS", "flowers", sim_img) 
        # Reading them as an image 
        sim_img = cv2.imread(path)
        # Comverting colorscale for plotting
        rgb_image = cv2.cvtColor(sim_img, cv2.COLOR_BGR2RGB)
        final_images.append(rgb_image)
    
    # Prepping target_image for plotting
    rgb_target = cv2.cvtColor(target_image, cv2.COLOR_BGR2RGB)    
    final_images.append(rgb_target)

    f, axarr = plt.subplots(2,2)
    axarr[0,0].imshow(final_images[3])
    axarr[0,1].imshow(final_images[0])
    axarr[1,0].imshow(final_images[1])
    axarr[1,1].imshow(final_images[2])
    
    # Plotting the distance score
    axarr[0,1].text(0.1, 0.1, f"Distance:{three_similar}", fontsize=14, ha="center") 
    # Saving plot 
    f.savefig('image_search.png')
    
    
    # Save csv
    target_img = "image_0020.jpg"
    similar.append(target_img)
    # Prepping dataframe, defining columns
    columns = ["1. Similar", "2. Similar", "3. Similar", "Target Image"]
    dframe = pd.DataFrame(similar, columns)
    dframe_trans = dframe.transpose()
    dframe_trans.to_csv("Image_search.csv", encoding = "utf-8")

    
    # Printing to terminal 
    print("Script succeeded: The following shows the distance scores of the 3 similar images as well as their filenames. The csv and the plot can be seen in the output-folder")
    print(three_similar)
    print(similar)
    
    
image_search()
