# Interactions-AI-Studio-Project

# Project Overview 
* Problem: Recognize spam calls from real calls in order to provide more efficient customer service for the AI customer service company Interactions
* Purpose: Operating within the realm of cybersecurity and audio technology, this project aligns with Interactions LLC’s mission of enhancing AI-driven customer service by allocating customer service resources to real customers and flagging fake callers.
* Dataset: 8,000 audio samples for training (6,400 authentic, 1,600 synthetic) and 2,000 samples for testing (1,600 authentic, 400 synthetic), drawn from multiple sources and stored into CSV files. 20% of the dataset were synthetic-generated audios.
* Tools: Google Colab, gTTS, Pyttsx3, Librosa, Wav2Vec, Tensorflow, Keras, Scikit-learn

# Goals
* Build a binary classification model labelling speech as authentic or synthetic 

* Create synthetic audio to add onto the Hugging Face authentic audio dataset

* Identify spoofed audio calls with a target F1 score of 90% or higher

# Methodology
1. Generate synthetic audio
   * Since our initial Common Voice dataset from HuggingFace (https://huggingface.co/datasets/mozilla-foundation/common_voice_13_0) only contained authentic audios, we needed to generate synthetic audio on our own and add onto the base dataset. We used two sources of synthetic audios in order to provide more variety to the spoofed calls so that our model would be better at generalizing many types of robocalls. We used two text-to-speech generator libraries, gTTS and pyttsx3, to generate 1000 synthetic audios each. 
2. Building Training and Testing Dataset
   * The HuggingFace dataset contained many features for metadata such as age and gender, but since most of the features columns were missing many values, we stuck with just using the audio column, which contained the actual mp3 audio file. We manually split up the training and testing datasets since we wanted the same number of each type of synthetic audio we generated. We did a 80/20 split for the train and test set, and the authentic to spoofed ratio was also 80/20. 
3. Data Preprocessing
   * The first step for preprocessing was changing the audio files to a numerical form since the models only work with numerical data. We changed the mp3 audio files into 1-dimensional number arrays by using the Librosa library. Then we generated feature vectors from the audios by using the Wav2Vec model. These feature vectors were super large, so we reduced them down to be size (300x256). We also used normalization and flattened the feature vectors into 1D arrays since the models only accept 1D arrays. We also tried another version of preprocessing in which we reduced the size of the feature vectors even further by utilizing mean pooling. This essentially took the average of each embedding dimension so that the vector was reduced to a size of 768.
4. Model Training and Selection
   * We tested 3 different models: logistic regression, neural network, and 1D CNN model.
   * Logistic regression- simpler model that can be quickly trained
     * F1 score: 62%
   * Neural network- can handle very large input sizes and can model more complex relationships
     * Without mean pooling: F1 score <30%
     * With mean pooling: F1 score of 82%
   * 1D Convolutional Neural Network (CNN)- works well with sequential data like audio as it can detect temporal (time-based) changes
     * F1 score: 97%
   * Since the 1D CNN model produced the highest F1 score, we chose it for our final model. However, we noticed that it was overfitting, so we added dropout and regularization layers to reduce overfitting.
5. Model Improvements
   * We finetuned our models by adjusting hyperparameters and testing different numbers of neurons and layers in order to achieve the highest F1 score.

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
