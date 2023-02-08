# Digit Sum Prediction using CNN
A Convolutional Neural Network (CNN) model for the task of predicting the sum of digits in an image. The dataset consists of images with 4 digits and labelled data is the sum of those digits. The image is preprocessed using OpenCV's regionProps, Labels and Thresholding to identify the different regions containing the digits. The regions are then padded and resized to 28x28 to be fed into the CNN model. 

## Image Preprocessing
1. `regionProps`, `Labels`, and `Thresholding` are used to identify the regions in the image that contain the digits.
2. The regions are appended into a matrix.
3. To ensure the regions have consistent size, they are padded and resized to 28x28.
4. In cases where digits are too close and cannot be differentiated, the erosion method is used to split the close digits.
5. Small regions present inside larger regions can cause incorrect results. To address this, the smallest region in an index is removed if the length of the regions array is 5 or 6.

## CNN Architecture
The CNN model consists of the following layers:

1. Conv2D: The first layer is a 2D Convolution layer with 64 filters, each of size 3x3 and 'relu' activation function.
2. Conv2D: The second Conv2D layer also has 64 filters, each of size 3x3 and 'relu' activation function.
3. MaxPooling2D: A Max Pooling layer with a pool size of 2x2 to down-sample the input and reduce the spatial dimensions.
4. Dropout: A dropout layer is added to prevent overfitting.
5. Flatten: The data is then flattened into a one-dimensional vector.
6. Dense: A fully connected layer with 128 neurons and 'relu' activation.
7. Dropout: Another dropout layer is added to prevent overfitting.
8. Dense: The final layer is a dense layer with 10 neurons and 'softmax' activation function.
## How to use
There are two files one is `training.ipynb` and other if `inference.ipynb`. You can use the code to train the model on your own dataset or use the pre-trained weights included in the repository. If you want to test on it some other dataset use `inference.ipynb` .

Dependencies
The following libraries are required to run the code:

- OpenCV
- Tensorflow
- Numpy

## Conclusion
This CNN architecture is designed to extract features from the input image and make predictions based on these features. The model has been tested and found to produce accurate results for the task of predicting the sum of digits in an image.
