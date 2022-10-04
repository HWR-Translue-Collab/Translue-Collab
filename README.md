# Translue-Collab

This repository contains the codebase of the proof-of-concept for Translue, a real-time translation app for screen contents.

## Getting started

### Requirements
To run the provided Jupyter Notebooks, you will need to install Python (>= 3.9.12).<br>
These are the necessary requirements that will be installed:

- cv2 (4.5.5) (`pip install opencv-python==4.5.5`)
- keras (2.4.3) (`pip install keras==2.4.3`)
- matplotlib (3.5.1) (`pip install matplotlib==3.5.1`)
- numpy (1.21.5) (`pip install numpy==1.21.5`)
- scipy (1.7.3) (`pip install scipy==1.7.3`)
- sklearn (1.0.2) (`pip install scikit-learn==1.0.2`)
- tensorflow (2.4.1) (`pip install tensorflow==2.4.1`)
- jupyter (newest version) (`pip install jupyter`)

## Text Detection
The text detection module was trained on this [ICDAR dataset](https://drive.google.com/file/d/1ObrV9pbH_-LBGbIodWgB6W4dtQloTTH6/view?pli=1). Feel free to download it if you plan to re-train the model or to get a reference on how the applied dataset is structured.

### Run the model
To run the text detection system, open the command line and tpye `jupyter notebook`. Navigate to *translue-poc/text-detection* and open *Text Detection - Translue PoC.ipynb*.<br>
If you're having trouble, refer to [this tutorial](https://realpython.com/jupyter-notebook-introduction/) on using Jupyter notebooks.
