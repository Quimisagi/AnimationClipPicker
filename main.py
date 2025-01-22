
from video_processor import load_video_paths, process_video
import argparse
import sys

videos_path_file = "videos_path.txt"

def main():
    parser = argparse.ArgumentParser(description="Process videos in a directory")
    parser.add_argument("--parent_dir", type=str, required=True, help="Parent directory containing videos")
    args = parser.parse_args()

    parent_dir = args.parent_dir

    if not parent_dir:
        print("Error: No parent directory provided. Please pass --parent_dir argument.")
        sys.exit(1)  # Exit the program

    try:
        # Check if videos_path_file exists and has content
        with open(videos_path_file, "r") as file:
            content = file.read().strip()
            video_paths = content.splitlines() if content else load_video_paths(parent_dir)
    except FileNotFoundError:
        # Load video paths if the file doesn't exist
        video_paths = load_video_paths(parent_dir)
        with open(videos_path_file, "w") as file:
            file.write("\n".join(video_paths))

    print("\nVideo paths loaded.")

    for i, video_path in enumerate(video_paths):
        process_video(video_path, i, len(video_paths))

if __name__ == "__main__":
    main()
