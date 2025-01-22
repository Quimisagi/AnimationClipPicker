import cv2
import os
import time
from spinner import Spinner

def load_video_paths(parent_dir):
    print(f"Loading video paths from {parent_dir}")
    video_paths = []
    spinner = Spinner("Scanning directories...")
    spinner.start()  # Start the spinner
    for root, dirs, files in os.walk(parent_dir):
        for file in files:
            if file.endswith(".mp4"):
                video_paths.append(os.path.join(root, file))
    spinner.stop()  # Stop the spinner
    return video_paths

def process_video(video_path, video_index, total_videos, output_file):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Could not open video at {video_path}. Skipping...")
        return

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    current_frame = 0

    while True:
        ret, frame = cap.read()
        time.sleep(0.01)

        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            current_frame = 0
            time.sleep(0.5)
            continue

        relative_path = video_path.split('download/')[1] if 'download/' in video_path else video_path
        info_text = f"Frames: {current_frame + 1}/{total_frames} - Video: {video_index + 1}/{total_videos} - Path: {relative_path}"
        info_lines = info_text.split(" - ")

        # Overlay text
        draw_overlay(frame, info_lines)

        # Display the frame with information
        cv2.imshow('Video Playback', frame)

        key = cv2.waitKey(25) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('r'):
            print(f"Video {video_index + 1} rejected")
            break
        elif key == 13:
            print(f"Video {video_index + 1} accepted")
            output_file.write(f"{video_index} - {video_path}\n")
            output_file.flush()
            break

        current_frame += 1

    cap.release()

def draw_overlay(frame, info_lines, x=10, y=50, font_scale=0.6, font_color=(255, 255, 255), background_color=(0, 0, 0, 100), font_thickness=1, line_spacing=20):
    for idx, line in enumerate(info_lines):
        y_offset = y + idx * line_spacing
        text_size = cv2.getTextSize(line, cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_thickness)[0]
        bg_x1, bg_y1 = x - 5, y_offset - 15
        bg_x2, bg_y2 = x + text_size[0] + 5, y_offset + 5

        cv2.rectangle(frame, (bg_x1, bg_y1), (bg_x2, bg_y2), background_color, cv2.FILLED)
        cv2.putText(frame, line, (x, y_offset), cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_color, font_thickness, cv2.LINE_AA)

