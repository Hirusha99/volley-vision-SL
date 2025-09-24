
import cv2
import os

def video_to_frames(video_path, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video
    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:  # No more frames
            break

        # Save each frame as an image
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:05d}.jpg")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1

    cap.release()
    print(f"Extracted {frame_count} frames to '{output_folder}'")

# Example usage:
# video_to_frames("input_video.mp4", "frames_output")



# ------------------------------------------------------

# import cv2
# import os

# def video_to_frames(video_path, output_folder, frame_interval):
#     # Create the output folder if it doesn't exist
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     cap = cv2.VideoCapture(video_path)
#     frame_count = 0
#     saved_count = 0

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         # Save only every "frame_interval" frames
#         if frame_count % frame_interval == 0:
#             frame_filename = os.path.join(output_folder, f"frame_{saved_count:05d}.jpg")
#             cv2.imwrite(frame_filename, frame)
#             saved_count += 1

#         frame_count += 1

#     cap.release()
#     print(f"Extracted {saved_count} frames (every {frame_interval}th frame) to '{output_folder}'")

# Example usage:
# video_to_frames("input_video.mp4", "frames_output", frame_interval=30)

