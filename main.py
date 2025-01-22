
from video_processor import load_video_paths, process_video
import argparse
import sys

videos_path_file = "videos_path.txt"

def main():
    parser = argparse.ArgumentParser(description="Process videos in a directory")
    parser.add_argument("--parent_dir", type=str, required=True, help="Parent directory containing videos")
    parser.add_argument("--output_file", type=str, default='./accepted_videos.txt', help="Path of the output file to save the paths of accepted videos")
    args = parser.parse_args()

    parent_dir = args.parent_dir
    output_file = args.output_file

    if not parent_dir:
        print("Error: No parent directory provided. Please pass --parent_dir argument.")
        sys.exit(1)  # Exit the program

    # Check if the videos_path_file exists
    try:
        with open(videos_path_file, "r") as file:
            content = file.read().strip()
            if content:
                video_paths = content.splitlines()
                print("Video paths loaded from file.")
            else:
                video_paths = load_video_paths(parent_dir)
                with open(videos_path_file, "w") as file:
                    file.write("\n".join(video_paths))
                file.close()
                print(f"Videos loaded from directory and saved to file {videos_path_file}")
            
    except FileNotFoundError:
        video_paths = load_video_paths(parent_dir)
        with open(videos_path_file, "w") as file:
            file.write("\n".join(video_paths))
        file.close()
        print(f"Videos loaded from directory and saved to file {videos_path_file}")

    last_clip_number = 0

    try:
        with open(output_file, "r") as file:
            lines = file.readlines()
            last_line = lines[-1] if lines else None
            if last_line:
                
                parts = last_line.split(" - ")
                if len(parts) > 0:
                    last_clip_number = int(parts[0].strip())
                    print(f"Extracted last clip: {last_clip_number}")
                else:
                    print("No valid number found in the last line.")
            else:
                print("The file is empty or has no lines.")
    except FileNotFoundError:
        print("The file does not exist.")

    file = open(output_file, "a")



    for i in range(last_clip_number, len(video_paths)):
        print(f"Processing video {i + 1}/{len(video_paths)}")
        video_path = video_paths[i]
        process_video(video_path, i, len(video_paths), file)

if __name__ == "__main__":
    main()
