# Burned Area Detection with Deep Learning and Sentinel-2
A pipeline to process Sentinel-2 remote sensing data and train a neural network for burned area detection.


## Pipeline Description
The pipeline is divided into four processing stages (1.-4.) and one training and validation stage (5.):
1. Merge bands: Merge the Green, NIR and SWIR bands of the atmospherically corrected Sentinel-2 data and create false-color images that emphasise burned area by transferring the spectral bands to RGB-channels and normalise the values to the 0-255 color scale.
2. Extract patches: Match the BA ground truth data to the false-color images by area and date; Extract small patches of size 128x128 from the false-color images and ground truth data. The smaller patch size leads to lower memory uptake when training.
3. Sort patches: Remove empty or broken patches from the datasets
4. Split patches: Randomly split the training patches into a training dataset (70% of the total data) and a validation dataset (30% of the total data)
5. run training: Take a neural network from the pytorch library (we used a Resnet-18 with a PSPNet in U-Net architecture) and train it on the processed patches and burned area ground truth. The best-performing epoch will be validated along a baseline model (see full doc) and the performance will be measured with a IoU and Dice coefficient. The training can be tracked with Weights and Biases (wandb.com).


