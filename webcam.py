from ultralytics import YOLO
import cv2

# --- LOAD YOUR CUSTOM MODEL ---
# IMPORTANT: Update this path to where you saved your new best.pt file
model = YOLO('best.pt') # Or 'best_models/best.pt' if you made a subfolder

# --- INITIALIZE WEBCAM ---
cap = cv2.VideoCapture(0) # '0' is usually the built-in webcam

# --- REAL-TIME DETECTION LOOP ---
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        frame = cv2.resize(frame, (480, 360))
        # Run YOLOv8 inference on the frame
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("YOLOv8 Webcam Feed", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()