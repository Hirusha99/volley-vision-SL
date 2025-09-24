import cv2
import os

def get_video_metadata(video_path):
    if not os.path.exists(video_path):
        print("Error: Video file not found!")
        return

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Cannot open video.")
        return

    # Read metadata
    fps = cap.get(cv2.CAP_PROP_FPS)                # Frames per second
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # Total number of frames
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # Width of video
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))# Height of video
    duration = frame_count / fps if fps != 0 else 0  # Duration in seconds

    print(f"Video Path      : {video_path}")
    print(f"Resolution      : {width} x {height}")
    print(f"Frame Rate (FPS): {fps}")
    print(f"Total Frames    : {frame_count}")
    print(f"Duration        : {duration:.2f} seconds")

    cap.release()

# Example usage:
# get_video_metadata(r"videos\AlphaGo Official Trailer.mp4")
