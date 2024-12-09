# Interactions-AI-Studio-Project

# Project Overview 
Problem: Recognize spam calls from real calls in order to provide more efficient customer service
Purpose: Operating within the realm of cybersecurity and audio technology, this project aligns with Interactions LLC’s mission of enhancing AI-driven customer service by allocating customer service resources to real customers.
Dataset: 8,000 audio samples for training (6,400 authentic, 1,600 synthetic) and 2,000 samples for testing (1,600 authentic, 400 synthetic), drawn from multiple sources and stored into CSV files. 20% of the dataset were synthetic-generated audios.

# Goals
-Build a binary classification model labelling speech as authentic or synthetic 

-Create synthetic audio to add onto the Hugging Face authentic audio dataset

-Identify spoofed audio calls with a target F1 score of 90% or higher

# Methodology

# Results and Key Findings
Results

F1 score above 90% was achieved: 97%

False positive rate was extremely low at 1%

AUC score was extremely high at 99%


Reducing overfitting

Dropout layers and L2 regularization were added to reduce overfitting

Validation loss had less of an increase for the adjusted model indicating that overfitting was reduced 

# Potential Next Steps
Since our final model still had overfitting issues, we would like to try out more strategies to reduce overfitting so that the model will be better at generalizing to new data. 

# Individual contributions
Aayat: Prepared the 8000 authentic audios, preprocessing the data, converting audios to number arrays 

Debasree: Made 1000 synthetic audios using GoogleGTTS library, preprocessing the data, reduced overfitting and created the visualizations of the results of our model

Marilyn: Made 1000 synthetic audios using Pyttsx3 library, preprocessing the data, training neural networks and 1D CNN model and tuning the hyperparameters to increase accuracy
