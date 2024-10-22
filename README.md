# Burned Area Detection with Deep Learning and Sentinel-2
A pipeline to process Sentinel-2 remote sensing data and train a neural network for burned area detection.


details of the work containing the steps and results are in p2m_report.pdf and presentation_p2m.pptx


The pipeline is divided into four processing stages (1.-4.) and one training and validation stage (5.):
1. Merge bands: Merge the Green, NIR and SWIR bands of the atmospherically corrected Sentinel-2 data and create false-color images that emphasise burned area by transferring the spectral bands to RGB-channels and normalise the values to the 0-255 color scale.
2. Extract patches: Match the BA ground truth data to the false-color images by area and date; Extract small patches of size 128x128 from the false-color images and ground truth data. The smaller patch size leads to lower memory uptake when training.
3. Sort patches: Remove empty or broken patches from the datasets
4. Split patches: Randomly split the training patches into a training dataset (70% of the total data) and a validation dataset (30% of the total data)
5. run training: Training using YOLOv8 (code in p2m.ipynb). you can directly run p2m.ipnyb to import the data from roboflow and then train the model and visualize the results.

the model is deployed using streamlit where you can directly use the weights of the trained model.
