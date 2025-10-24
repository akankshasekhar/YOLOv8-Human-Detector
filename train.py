from ultralytics import YOLO

model = YOLO('yolov8s.pt')

def main():
    results = model.train(
        data='data.yaml',
        epochs=100,
        imgsz=640
    )
    print("Training complete!")

if __name__ == '__main__':
    main() 