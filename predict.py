from ultralytics import YOLO

# Load your custom-trained model from the training results folder
# Make sure 'train4' is the correct folder name for your latest training run
model = YOLO('C:\\Users\\gayat\\OneDrive\\Documents\\GETTING STARTED\\yolo_human_detector\\runs\\detect\\train4\\weights\\best.pt')

# --- IMPORTANT ---
# You MUST change this path to the actual location of a new image you want to test.
# This image should NOT be from your training or validation set.
source_image = r"C:\Users\gayat\OneDrive\Pictures\Screenshots\Screenshot 2025-09-15 215741.png"
results = model.predict(source_image, save=True)

# Run the prediction and save the result
# The result image will be saved in a new 'predict' folder inside 'runs/detect/'
results = model.predict(source_image, save=True)

print("Prediction complete!")
print("Check your 'runs/detect/' folder to see the result image.")
