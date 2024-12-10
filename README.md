# Interactions-AI-Studio-Project

# Project Overview 
* Problem: Recognize spam calls from real calls in order to provide more efficient customer service for the AI customer service company Interactions
* Purpose: Operating within the realm of cybersecurity and audio technology, this project aligns with Interactions LLC’s mission of enhancing AI-driven customer service by allocating customer service resources to real customers.
* Dataset: 8,000 audio samples for training (6,400 authentic, 1,600 synthetic) and 2,000 samples for testing (1,600 authentic, 400 synthetic), drawn from multiple sources and stored into CSV files. 20% of the dataset were synthetic-generated audios.
* Tools: Google Colab, gTTS, Pyttsx3, Librosa, Wav2Vec, Tensorflow, Keras, Scikit-learn

# Goals
* Build a binary classification model labelling speech as authentic or synthetic 

* Create synthetic audio to add onto the Hugging Face authentic audio dataset

* Identify spoofed audio calls with a target F1 score of 90% or higher

# Methodology
1. Generate synthetic audio
   Since our initial Common Voice dataset from HuggingFace (https://huggingface.co/datasets/mozilla-foundation/common_voice_13_0) only contained authentic audios, we needed to generate synthetic audio on our own and add onto the base dataset. We used two sources of synthetic audios in order to provide more variety to the spoofed calls so that our model would be better at generalizing many types of robocalls. We used two text-to-speech generator libraries, gTTS and pyttsx3, to generate 1000 synthetic audios each. 
3. Building Training and Testing Dataset
   The HuggingFace dataset contained many features of metadata such as age and gender, but since most of the features contained a majority of empty cells, we stuck with just using the audio column, which contained the actual mp3 audio file. We did a 80/20 split for the train and test set. 
5. Data Preprocessing
   The first step for preprocessing was changing the audio files to a numerical form since the models only work with numerical data. We changed the mp3 audio files into 1-dimensional number arrays by using the Librosa library. Then we generated feature vectors from the audios by using the Wav2Vec model.
7. Model Training and Selection
   We tested 3 different models: logistic regression, neural network, and 1D CNN model.
   Logistic regression- simpler model that can be quickly trained
   Neural network- can handle very large input sizes and can model more complex relationships
   1D Convolutional Neural Network (CNN)- works well with sequential data like audio as it can detect temporal (time-based) changes
8. Model Improvements
   We finetuned our models by adjusting hyperparameters and testing different numbers of neurons and layers in order to achieve the highest F1 score. 
# Results and Key Findings
Results

* F1 score above 90% was achieved: 97%

* False positive rate was extremely low at 1%

* AUC score was extremely high at 99%


Reducing overfitting

* Dropout layers and L2 regularization were added to reduce overfitting

* Validation loss had less of an increase for the adjusted model indicating that overfitting was reduced 

# Potential Next Steps
Since our final model still had overfitting issues, we would like to try out more strategies to reduce overfitting so that the model will be better at generalizing to new data. 

# Individual contributions
* Aayat: Prepared the 8000 authentic audios, preprocessing the data, converting audios to number arrays 
* Debasree: Made 1000 synthetic audios using GoogleGTTS library, preprocessing the data, made feature vectors for training dataset, reduced overfitting and created the visualizations of the results of our model
* Marilyn: Made 1000 synthetic audios using Pyttsx3 library, preprocessing the data,  made feature vectors for testing dataset, training neural networks and 1D CNN model and tuning the hyperparameters to increase accuracy
