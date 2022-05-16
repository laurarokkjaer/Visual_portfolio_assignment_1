# Visual Analytics - Spring 2022
# Portfolio Assignment 1

This repository contains the code and descriptions from the first assigned project of the Spring 2022 module Visual Analytics as part of the bachelor's tilvalg in Cultural Data Science at Aarhus University - whereas the overall Visual analytics portfolio (zip-file) consist of 4 projects, 3 class assignments + 1 self-assigned.

## Repo structure
### This repository has the following directory structure:

| **Folder** | **Description** |
| ----------- | ----------- |
| ```in``` | Contains the input data (will be empty) |
| ```out``` | Contains the results (outputs like plots or reports)  |
| ```src``` | Contains code for assignment 1 |
| ```utils``` | Contains utility functions written by [Ross](https://pure.au.dk/portal/en/persons/ross-deans-kristensenmclachlan(29ad140e-0785-4e07-bdc1-8af12f15856c).html), and which have been used in the assignments |

Also containing a ```MITLICENSE``` for guidelines of how to reproduce and use the data in this repository, as well as a ```.txt``` reqirements-file, where the required installments will be listed.

## Assignment description
The official description of the assignment from github/brightspace [assignment description](https://github.com/CDS-AU-DK/cds-visual/blob/main/assignments/assignment1.md):

For this assignment, you will write a small Python program to compare image histograms quantitively using Open-CV and the other image processing tools you've already encountered. Your script should do the following:

- Take a user-defined image from the folder
- Calculate the "distance" between the colour histogram of that image and all of the others.
- Find which 3 image are most "similar" to the target image.
- Save an image which shows the target image, the three most similar, and the calculated distance score.
- Save a CSV which has one column for the filename and three columns showing the filenames of the closest images in descending order

#### The goal of the assignment 
The goal of this assignment was to demonstrate a good understanding of how to use simple image processing techniques to extract valuable information from image data. The results is to have a simple tool for performing image search on a dataset of images, finding which images are most similar to one another along with a plot visualising those images.

#### Data source
The data used in this assignment was the in class flowers-folder from UCloud (shared-drive/CDS-VIS/flowers). 
Link to flowers dataset: [flowers dataset](https://www.robots.ox.ac.uk/~vgg/data/flowers/102/).


## Methods
To solve this assignment i have worked with ```opencv``` in order to both calculate the histograms as well as for the general image processing (using the ```calcHist```, ```imread```, ```normalize``` and ```compareHist```). Futhermore i used the ```jimshow``` and ```jimshow_channel``` from the ```utils```-folder, along with the ```matplotlib``` for plotting and visualisation.

## Usage (reproducing results)
For this .py script the following should be written in the command line:
- change directory to the folder /src 
- write command: python image_search.py
- when processing results there will be a messagge saying that the script has succeeded and the outputs can be seen in the output folder 

The target image, as well as the most similar images can be seen in the output folder both as csv (with file informations) and as a visualisation where the images are plottet next to each other


## Discussion of results
something about 
- a user defined input (what that could do for the assignment and the reproducability 
- the transision from a notebook to a .py script 

