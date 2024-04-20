# Handwritten Digit Classification

Classification on MNIST Dataset, utilising only traditional Machine Learning techniques. This is a course project of the course <b>Pattern Recognition And Machine Learning</b> of <b>IIT Jodhpur</b>, taught in Semester-II of Academic Year 2023-24.

### Prerequisites

<li>Downloading the MNIST Dataset is necessary for execution of the files.</li>
<li>The dataset is available in <a href="https://git-disl.github.io/GTDLBench/datasets/mnist_datasets/" target="_blank">MNIST Dataset</a></li>
<li>Download the <b>.CSV</b> files of the training and test set.</li>
<li>Create a folder <b>MNIST_CSV</b> on the main branch, and inside the folder, store the two datasets as <b>MNIST_train.csv</b> and <b>MNIST_test.csv</b></li>
<li>A folder named <b>pkl_objects</b> must be created on the main branch, if user wants to store the classifiers as pickle files.</li>

### Order of execution of files

1) [experiment_with_classifiers](experiment_with_classifiers.ipynb) - Trains different classifiers on different variation of the MNIST dataset.
2) [augmentation_code](augmentation_code.ipynb) - Generates variations of the training dataset to have more training examples for the best models. File creates and saves a .feather file.
3) [save_custom_transformed_data](save_custom_transformed_data.ipynb) - Creates and saves two .feather files, which are used for training and testing the best models.
4) [best_models](best_models.ipynb) - Trains the best models on the augmented dataset, and saves the classifiers are .pkl files for later use.
5) [prediction_real_img](prediction_real_img.ipynb) - Provides prediction of two handwritten digits clicked on camera.

The above files won't work properly if not executed in the above order. The other files will work only after file 4 has been executed.
[failure_case_best_model](failure_case_best_model.ipynb) 



