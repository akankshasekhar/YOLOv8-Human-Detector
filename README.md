# My First AI Project: A Real-Time Human Detector

Hey there! This is my first big dive into computer vision, a project where I successfully built a real-time human detector using Python and the YOLOv8 model.

This was a huge learning experience for me. I managed the entire process from start to finish:

* **Gathering the Data:** I started by building my own dataset of over 250 images. I labeled every single person by hand using CVAT, which taught me a lot about what makes good training data.
* **Training the Model:** My laptop's CPU wasn't going to cut it (I tried, it was *so* slow!), so I learned how to use a **Kaggle Notebook**. I trained a YOLOv8s model for 100 epochs on their free T4 GPU, which was amazing—it finished the whole job in about 30 minutes!
* **Making it Work:** The best part! I wrote a Python script using OpenCV (`cv2`) that takes the final trained model (`best.pt`) and runs it on my live webcam feed. Seeing it draw boxes around people in real-time was an incredible "it works!" moment.

Here's a look at the final model in action on my webcam:

![My custom YOLOv8 model detecting humans on a webcam feed](image_17d0c9.jpg)
*(Note: To make this image work, you must upload your own screenshot to your repository and change the filename `image_17d0c9.jpg` to match.)*

## Features
* Detects humans in images and live webcam feeds.
* Trained on a custom dataset of 250+ images.
* Built with `ultralytics`, `OpenCV`, and `PyTorch`.

## How to Use

1.  **Clone this repo:**
    ```
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
    ```
    *(Remember to replace YOUR_USERNAME and YOUR_REPO_NAME with your details)*

2.  **Install the necessary libraries:**
    ```
    pip install -r requirements.txt
    ```

3.  **Download the Trained Model:**
    My trained `best.pt` file is available on the **[Releases page](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/releases/tag/v1.0)**. Please download it and place it in the main project folder.

4.  **Download the Dataset (Optional):**
    My dataset isn't in this repo (it's too big!). If you want to see the data or try training it yourself, you can grab it from [**LINK TO YOUR KAGGLE DATASET HERE**].

5.  **Run the webcam:**
    ```
    python webcam.py
    ```
