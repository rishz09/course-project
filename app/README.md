# [Interface](https://huggingface.co/spaces/rishz09/prml-project) Hosted on Hugging Face

This folder contains files to deploy the app on Hugging Face.
* [requirements.txt](requirements.txt) contains the modules and their corresponding versions which shall be installed on building the app for the first time.
* [app.py](app.py) contains the code to load the trained model, perform necessary operations and give prediction.
* [Makefile](Makefile) runs the streamlit app on Hugging Face.
* [gbc_custom](gbc_custom.pkl) is the pickled Histogram Gradient Boosting Classifier, trained on custom transformed dataset (non-augmented).

## Instructions for choosing classifier

* On Hugging Face, 2 best classifiers have been uploaded. The Random Forest Classifier, being large in size, hasn't been uploaded here, and can be found [here](https://huggingface.co/spaces/rishz09/prml-project/tree/main).
* By default, the interface is made to load the Gradient Boosting Classifier due to it's low usage of computational resources. However, better generalisation performance can be achieved with the computationally more expensive Random Forest Classifier.
* To use the Random Forest Classifier, instructions are provided inside [app.py](app.py).
