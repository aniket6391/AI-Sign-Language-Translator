# Interview Questions (Based on Project)

1.  **Computer Vision:** Explain how OpenCV reads frames from a webcam. What color format does it use by default, and why did you have to convert it for Streamlit? (Answer: BGR to RGB).
2.  **Deep Learning:** Explain the mathematical operation behind a Convolutional Layer (Conv2D). What does a filter/kernel actually do to an image?
3.  **Deep Learning:** What is the difference between ReLU and Softmax activations? Why is Softmax used in the output layer?
4.  **Machine Learning Metrics:** Your model achieved 95% accuracy. Why might accuracy be a misleading metric, and why is it important to look at the F1-Score or Confusion Matrix?
5.  **Python Concurrency:** You used `threading` for the speech engine. What is the difference between multi-threading and multi-processing in Python, considering the Global Interpreter Lock (GIL)?
6.  **System Design:** If we wanted to deploy this to 10,000 concurrent users on the web, how would the architecture need to change? (Answer: Move inference to a cloud GPU backend, stream video via WebRTC, optimize model to TFLite/ONNX).
