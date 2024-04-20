# Handwritten Digit Classification

Classification on MNIST Dataset, utilising only traditional Machine Learning techniques. This is a course project of the course <b>Pattern Recognition And Machine Learning</b> of <b>IIT Jodhpur</b>, taught in Semester-II of Academic Year 2023-24.

## Prerequisites

<li>Downloading the MNIST Dataset is necessary for execution of the files.</li>
<li>The dataset is available in <a href="https://git-disl.github.io/GTDLBench/datasets/mnist_datasets/" target="_blank">MNIST Dataset</a></li>
<li>Download the <b>.CSV</b> files of the training and test set.</li>
<li>Create a folder <b>MNIST_CSV</b> on the main branch, and inside the folder, store the two datasets as <b>MNIST_train.csv</b> and <b>MNIST_test.csv</b></li>

## Instruction regarding saving files and images

Keep **pickle.dump()** and **plt.savefig()** statements uncommented if you wish to save the trained classifiers or images.

## Order of execution of files

1) [experiment_with_classifiers](experiment_with_classifiers.ipynb) - Trains different classifiers on different variation of the MNIST dataset.
2) [augmentation_code](augmentation_code.ipynb) - Generates variations of the training dataset to have more training examples for the best models. File creates and saves a .feather file.
3) [save_custom_transformed_data](save_custom_transformed_data.ipynb) - Creates and saves two .feather files, which are used for training and testing the best models.
4) [best_models](best_models.ipynb) - Trains the best models on the augmented dataset, and saves the classifiers are .pkl files for later use.
5) [prediction_real_img](prediction_real_img.ipynb) - Provides prediction of two handwritten digits, [3.jpg](3.jpg) and [7.jpg](7.jpg), clicked on camera. Certain preprocessing steps are involved before prediction.
\
\
The above files won't work properly if not executed in the above order.
\
[gen_augmentation_images](gen_augmentation_images.ipynb) is used to view the different variations of a single image, after data augmentation. Can be used after execution of [file 2](augmentation_code.ipynb).
\
[failure_case_best_model](failure_case_best_model.ipynb) is used to perform failure case analysis of the best model obtained after training. File is available for execution after executing [file 4](best_models.ipynb).

## Types of Datasets used for training

* Original dataset (with normalisation)
* Principal Component Analysis (dimensionality reduction)
* Linear Discriminant Analysis (dimensionality reduction)
* Edge Detector with Prewitt Kernel (feature extractor)
* Custom feature extractor
* Augmented Dataset for larger training set
  
## Classifiers used

* K-Nearest Neighbors
* Decision Trees
* Linear Regression
* Naive Bayes (Gaussian and Multinomial)
* Random Forest
* AdaBoost
* Histogram Gradient Boosting Classifier
* Support Vector Machines with Radial Basis Function Kernel

## Maximum Accuracy Achieved

98.08%

## Report

View the [report](report.pdf) to get an in-depth understanding of the project.

## Slides

A concise [presentation](slides.pdf) about the project. 

## Interface

* [App](app) folder contains the code to the app hosted on Hugging Face.
* [Link](https://huggingface.co/spaces/rishz09/prml-project)

## Authors

* Ankit Kumar (B22CS076)
* Rishabh Acharya (B22CS090)
* Pujit Jha (B22CS091)
* Raj Nandan Singh (B22EE052)
* Ayush Pekamwar (B22EE084)

\
**Group No: 32**

