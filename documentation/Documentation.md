# Documentation

This documentation contains the detailed setup instructions, the meetings notes in order, as well as the respective resources that were researched, gathered and presented per meeting for and with Translue.

## Collaboration Goal

The goal was to research and build a knowledge base with proof-of-concept on whether or not artifical intelligence can be applied on edge devices with the purpose of running real-time image text translation on the phone screen. With a pruned and quantized, mobile-optimized image text detector, the proof-concept shows that indeed capable artifical intelligence systems can be deployed within restricted environments like phones, without a significant trade-off in accuracy/performance.


## Getting Started - Text Detection Module

This project requires a Python version >= 3.9 to be installed on your system. From here, these Python packages are required (with respective install command):

- cv2 (4.5.5) (`pip install opencv-python==4.5.5.64`)
- keras (2.4.3) (`pip install keras==2.4.3`)
- matplotlib (3.5.1) (`pip install matplotlib==3.5.1`)
- numpy (1.21.5) (`pip install numpy==1.21.5`)
- pillow (9.2.0) (`pip install pillow==9.2.0`)
- scipy (1.7.3) (`pip install scipy==1.7.3`)
- sklearn (1.0.2) (`pip install scikit-learn==1.0.2`)
- tensorflow (2.4.1) (`pip install tensorflow==2.4.1`)
- tensorflow model optimization (0.7.3) (`pip install tensorflow-model-optimization==0.7.3`)
- jupyter (newest version) (`pip install jupyter`)

To run this project, type into a command line `jupyter notebook`. This will launch a local Juypter server from which you can navigate to the project's notebook file `Text Detection - Translue PoC.ipynb`. From here, you can click at the notebook cells to highlight them. To run a notebook cell, press `CTRL + ENTER`.

The notebook is equipped with more code-specific, documenting texts and comments. See there for further details on what we implemented and how we did this in detail.

## Meeting-related documentation

1. 29.08.2022
   - [Meeting Notes (pdf)](meeting-notes/pdf/29_08_2022.pdf)
   - [Meeting Notes (md)](meeting_notes/md/29_08_2022.md)
   - [Key Questions](research/pdf/key_questions_29_08_2022.pdf)
2. 05.09.2022
   - [Meeting Notes (pdf)](meeting-notes/pdf/05_09_2022.pdf)
   - [Meeting Notes (md)](meeting_notes/md/05_09_2022.md)
   - [Key Questions](research/pdf/additional_key_questions_raised_by_a_developer.pdf)
3. 12.09.2022
   - [Meeting Notes (pdf)](meeting-notes/pdf/12_09_2022.pdf)
   - [Meeting Notes (md)](meeting_notes/md/12_09_2022.md)
   - [Key Questions](research/pdf/key_questions-12_09_2022.pdf)
   - [Translue Elaboration Presentation](artifacts/Translue%20-%20Elaboration%20-%2012.09.2022.pdf)
4. 19.09.2022
   - [Meeting Notes (pdf)](meeting-notes/pdf/19_09_2022.pdf)
   - [Meeting Notes (md)](meeting_notes/md/19_09_2022.md)
   - [Competitor Materials](research/pdf/competitors-open_source.pdf)
   - [Existing Recognition Solutions](research/md/existing_text_recognition_solutions.pdf)
   - [Translue Case Study Google Lens](artifacts/Translue%20-%20Google%20Lens%20-%2019.09.2022.pdf)
   - [Translue x HWR - Building a Text Recognition AI](artifacts/Translue%20x%20HWR%20-%20Building%20A%20Text%20Recognition%20AI.pdf)
5. 18.11.2022
   - [Key Questions](research/pdf/key_questions-18_11_2022.pdf)
   - [Translue - Optimal Brain Damage - Researching Pruning & Quantization](artifacts/Translue%20-%20Optimal%20Brain%20Damage%20-%20Pruning%20Neural%20Networks.pdf)


We also added an additional [Recap Presentation](artifacts/Recap_Presentation.pdf), additionally summarizing our findings.