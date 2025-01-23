import os
import cv2
import argparse
from ultralytics import YOLO

# function for inference based on input source type
def run_inference(source, model, output_folder='results'):
    os.makedirs(output_folder, exist_ok=True)

    # Check if the source is a folder of images
    if os.path.isdir(source):
        for image_name in os.listdir(source):
            if image_name.lower().endswith(('.jpg', '.jpeg', '.png')):
                image_path = os.path.join(source, image_name)

                # Perform inference
                results_list = model(image_path)

                # Saving results
                for idx, result in enumerate(results_list):
                    result.save(filename=os.path.join(output_folder, f"{image_name}_result_{idx}.jpg"))

                print(f"Processed: {image_name}")

        print("Inference completed for all images in the folder.")

    # Check if the source is a single image or video
    elif source.lower().endswith(('.jpg', '.jpeg', '.png', '.mp4', '.avi', '.mov')):
        results_list = model(source)

        if source.lower().endswith(('.jpg', '.jpeg', '.png')):
            # Save the processed image
            for idx, result in enumerate(results_list):
                result.save(filename=os.path.join(output_folder, f"{os.path.basename(source)}_result_{idx}.jpg"))
            print(f"Processed image: {source}")

        else:
            # Save the processed video
            for result in results_list:
                result.save(filename=os.path.join(output_folder, f"processed_{os.path.basename(source)}"))
            print(f"Processed video: {source}")

    # Check if the source is webcam (integer input for webcam ID)
    elif source.isdigit():
        cap = cv2.VideoCapture(int(source))
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Perform inference
            results_list = model(frame)

            # Display the result
            for result in results_list:
                annotated_frame = result.plot()
                cv2.imshow('YOLOv11 Webcam Detection', annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        print("Webcam inference completed.")

    else:
        print("Invalid input source. Please provide a valid image, folder, video, or webcam ID.")

# Main function 
def main():
    parser = argparse.ArgumentParser(description="YOLOv11 Corrosion Detection Inference")
    
    # arguments for the input data and model paths
    parser.add_argument('--input', type=str, required=True, 
                        help="Path to input data (image, folder, video, or webcam ID)")
    parser.add_argument('--model', type=str, required=True, 
                        help="Path to the YOLOv11 model weights file (e.g., best.pt)")
    parser.add_argument('--output', type=str, default='results', 
                        help="Folder to save the inference results (default: 'results')")
    
    # Parse the arguments
    args = parser.parse_args()

    # Loading the YOLOv11 model
    model = YOLO(args.model)

    # Run inference based on the input type
    run_inference(args.input, model, output_folder=args.output)

if __name__ == "__main__":
    main()
