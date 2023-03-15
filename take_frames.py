import cv2
import os

# Input and output folder paths
input_folder = r'C:\Users\pawan\Downloads\Computer Vision\Custom Dataset'
output_folder = r'C:\Users\pawan\Downloads\Computer Vision\Custom Dataset\data'

# Loop over all video files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.mp4') or filename.endswith('.avi'):
        # Open the video file for reading
        video_path = os.path.join(input_folder, filename)
        cap = cv2.VideoCapture(video_path)

        # Create a new folder for storing frames
        video_name = os.path.splitext(filename)[0]
        frame_folder = os.path.join(output_folder, video_name)
        os.makedirs(frame_folder, exist_ok=True)

        # Extract frames at 20 fps and save them to the frame folder
        frame_count = 0
        while True:
            # Read the next frame from the video
            ret, frame = cap.read()
            if not ret:
                break

            # Extract frames at 20 fps
            if frame_count % 3 == 0:
                # Save the frame to the output folder
                frame_filename = f'{frame_count}.jpg'
                frame_path = os.path.join(frame_folder, frame_filename)
                cv2.imwrite(frame_path, frame)

            # Increment the frame counter
            frame_count += 1

        # Release the video capture object
        cap.release()