# Viva Questions & Answers

**Q1: What is the main objective of this project?**
A: To translate sign language gestures into text and speech in real-time using a laptop webcam, bridging the communication gap for hearing-impaired individuals.

**Q2: Why did you use MediaPipe instead of just feeding raw images to the CNN?**
A: Raw images contain background noise (walls, clothes, lighting changes). MediaPipe extracts exactly 21 hand landmarks, allowing us to crop the image strictly around the hand. This drastically improves the CNN's accuracy and makes it invariant to backgrounds.

**Q3: What is the architecture of your CNN?**
A: It consists of two Conv2D layers with ReLU activation for feature extraction, followed by MaxPooling layers. Then a Flatten layer, a Dense layer with 128 neurons, a Dropout layer to prevent overfitting, and a final Dense Softmax layer for classification.

**Q4: What is the purpose of the Dropout layer?**
A: Dropout randomly ignores a set percentage of neurons during training. This prevents the network from over-relying on specific features and memorizing the training data, thus reducing overfitting and improving generalization.

**Q5: What Optimizer and Loss function did you use?**
A: I used the Adam optimizer because it adapts the learning rate during training, and Categorical Crossentropy as the loss function because this is a multi-class classification problem.

**Q6: How does the Text-to-Speech (TTS) work without freezing the camera?**
A: The TTS engine (`pyttsx3`) is executed inside a separate background Thread. If it ran on the main thread, the OpenCV `while` loop would pause while the computer was speaking, causing the video feed to freeze.

**Q7: How did you prevent the app from speaking a word 30 times a second?**
A: I implemented a stabilization buffer. The model must predict the exact same sign for 5 consecutive frames with >80% confidence before it registers. Then, I added a 3.0-second time cooldown for the last spoken word.

**Q8: Why use Streamlit instead of Flask or Django?**
A: Streamlit is designed specifically for Machine Learning and Data Science applications. It allowed me to rapidly build a reactive, single-page dashboard with built-in data visualization (loss charts, metrics) without writing extensive HTML/JS/CSS.
