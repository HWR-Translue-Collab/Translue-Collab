"""
Preprocessing the ICDAR dataset for later use in image detection
"""

import numpy as np
import cv2
import os
import tqdm

print('Preprocessing ICDAR dataset for training and further use...')

# Define image and label location
data_path = 'Data/'
image_path = data_path + 'images/'
gt_path = data_path + 'ground_truth/'

# These will hold all individual image paths and respective ground truth file paths
train_image_paths = []
train_gt_paths = []

# Iterate over all files within ground_truth directory
# (this tqdm thing creates the progress bars)
for new_file in tqdm.tqdm(os.listdir(gt_path)):

    # Given a ground_truth file, build the respective image file name
    if 'gt' in new_file:
        name_split = new_file.split('.') # "gt_123.txt" becomes ["gt_123", "txt"]
        image_name = name_split[0][3:]   # Given ["gt_123", "txt"] -> image_name becomes "123"
        image_name = image_name + '.jpg' # Given "123" -> image_name becomes "123.jpg"

        path_img = os.path.join(image_path, image_name)        # Build the file path to this image "123.jpg"
        train_image_paths.append(path_img)                     # Store the path in a growing set of training images
        train_gt_paths.append(os.path.join(gt_path, new_file)) # Store the txt-file's path as well

X_final = []     # These will hold the images
Y_final = []     # These will hold their respective ground_truth labels (what we expect the network to ideally output)

grid_h = 16      # This many grid cells are projected horizontally onto the image
grid_w = grid_h  # This many grid cells are projected vertically onto the image
img_w = 512      # Image width
img_h = 512      # Image height

# Increment a counter until the count of images is reached
for j in tqdm.tqdm(range(len(train_image_paths))):

    new_file = train_image_paths[j]       # Get image we stored at index z, e.g. "123.jpg"
    x = cv2.imread(train_image_paths[j])  # Open current image
    x_sl = img_w / x.shape[1]             # Expected width in relation to original image width
    y_sl = img_h / x.shape[0]             # Expected height in relation to original image height
    img = cv2.resize(x, (img_w, img_h))   # Resizing (NOT cropping) the image to one common size

    X_final.append(img)                   # Append the resized image

    i = " "                               # Image file name separator

    # Some image files were formatted differently, we account for that
    if 'img' in new_file:
        i = ", "

    # This is a 3-dimensional 16x16(x1)x5 array to denote the image patches of interest
    Y = np.zeros((grid_h, grid_w, 1, 5))

    # For current image: Open the respective label txt file
    file = train_gt_paths[j]
    name = open(file, 'r')
    data = name.read()
    data = data.split("\n")
    data = data[:-1]

    # Iterate over the image patches that are to be found in current image
    for li in data:
        file_data = li.split(i) # file_data is something like ['41', '136', '537', '265', '"Campus"']
        strr = file_data[4]     # The word within this patch
        bb = file_data[:4]      # The box coordinates of this image patch

        # These scaled points make up the rectangle corners in the resized image
        xmin = int(bb[0]) * x_sl
        xmax = int(bb[2]) * x_sl
        ymin = int(bb[1]) * y_sl
        ymax = int(bb[3]) * y_sl

        # This is how a ground_truth rectangle could be drawn to verify the preprocessing
        # te = cv2.rectangle(img,(int(xmin),int(ymin)),(int(xmax),int(ymax)) , color = (0,255,0))

        # Scaled down image rectangle patch width and height
        w = (xmax - xmin) / img_w
        h = (ymax - ymin) / img_h

        # Compress rectangle coordinates into 16x16x5 grid layout (defines which of these grids are to be included)
        x = (((xmax + xmin) / 2) / img_w) * grid_w
        y = (((ymax + ymin) / 2) / img_h) * grid_h

        # Mark the presence of ground_truth image patch in the 16x16x5 matrix Y
        Y[int(y), int(x), 0, 0] = 1
        Y[int(y), int(x), 0, 1] = x - int(x)
        Y[int(y), int(x), 0, 2] = y - int(y)
        Y[int(y), int(x), 0, 3] = w
        Y[int(y), int(x), 0, 4] = h

    # Add this completed image patch coordinate matrix Y to the set of final labels Y_final
    Y_final.append(Y)

# Copy over X_final and Y_final into X and Y
X = np.array(X_final)
X_final = []
Y = np.array(Y_final)
Y_final = []

# Convert color space [0;255] into numeric space [-1;1] for easier computing
X = (X - 127.5) / 127.5

# Save these preprocessing results
X_path = data_path + 'X.npy'
Y_path = data_path + 'Y.npy'
np.save(X_path, X)
np.save(Y_path, Y)

print(f'Saved output to:\n{X_path}\n{Y_path}')
