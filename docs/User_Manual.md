# User Manual

Welcome to the AI Sign Language Translator Dashboard. Follow these steps to train your own signs and translate them in real-time.

## Step 1: Collect Data
1. On the dashboard, locate the **Control Panel**.
2. Click **Collect Dataset**. A configuration box will appear.
3. Type the name of the sign you want to teach the AI (e.g., "A").
4. Select the number of images (100 is recommended).
5. Click **Start Capture**.
6. Immediately position your hand in front of the webcam and perform the sign. Move your hand slightly to capture different angles.
7. Wait until the progress bar completes and the success message appears.
8. Repeat this step for at least 2 or 3 different signs.

## Step 2: Train the Model
1. Once you have collected images for multiple classes, click **Train Model** in the Control Panel.
2. The UI will display a spinner. Training will take about 1-2 minutes depending on your CPU/GPU.
3. Once finished, look at the **Training Information** panel on the right to view your Accuracy and the Loss graph.
4. The Top metric card for "Model Status" will change to **Ready**.

## Step 3: Real-Time Translation
1. Ensure the model is Ready.
2. Click **Start Camera**.
3. Position your hand in the frame. The green MediaPipe mesh will appear.
4. Perform one of the signs you trained.
5. Look at the **Prediction Panel** to see the translated text.
6. If you hold the sign steadily, the system will speak the word aloud!
7. Check the **Prediction History** table to see a log of your translations.
