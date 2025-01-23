from video_processor import load_video_paths, process_video
import argparse
import sys

videos_path_file = "videos_path.txt"

def main():
    parser = argparse.ArgumentParser(description="Process videos in a directory")
    parser.add_argument("--parent_dir", type=str, required=True, help="Parent directory containing videos")
    parser.add_argument("--output_file", type=str, default='./accepted_videos.txt', help="Path of the output file to save the paths of accepted videos")
    parser.add_argument("--restart", dest='restart', action='store_true', help="Restart the process from the beginning")
    parser.add_argument("--fps", type=int, default=64, help="Frames per second")
    parser.add_argument("--minimun_frames", type=int, default=3, help="Minimum frames trheshold. Videos with less frames will be skipped")
    args = parser.parse_args()

    parent_dir = args.parent_dir
    output_file = args.output_file

    if not parent_dir:
        print("Error: No parent directory provided. Please pass --parent_dir argument.")
        sys.exit(1)  # Exit the program


    if args.restart:
        print("Restarting the process from the beginning.")
        with open(videos_path_file, "w") as file:
            file.write("")
        with open(output_file, "w") as file:
            file.write("")

    try:
        # Attempt to read existing video paths from the file
        with open(videos_path_file, "r") as file:
            content = file.read().strip()

        if content:
            video_paths = content.splitlines()
            print("Video paths loaded from file.")
        else:
            raise ValueError("File is empty. Reloading video paths.")

    except (FileNotFoundError, ValueError):
        # Load video paths from the directory if the file doesn't exist or is empty
        video_paths = load_video_paths(parent_dir)
        with open(videos_path_file, "w") as file:
            file.write("\n".join(video_paths))
        print(f"Videos loaded from directory and saved to file {videos_path_file}")

    start_index = 0


    if not args.restart:
        try:
            with open(output_file, "r") as file:
                lines = file.readlines()
                last_line = lines[-1] if lines else None
                if last_line:

                    parts = last_line.split(" - ")
                    if len(parts) > 0:
                        start_index = int(parts[0].strip())
                        print(f"Extracted last clip: {start_index}")
                    else:
                        print("No valid number found in the last line.")
                else:
                    print("The file is empty or has no lines.")
        except FileNotFoundError:
            print("The file does not exist.")

    file = open(output_file, "a")



    for i in range(start_index, len(video_paths)):
        print(f"Processing video {i + 1}/{len(video_paths)}")
        video_path = video_paths[i]
        process_video(video_path, i, len(video_paths), file, args.fps, args.minimun_frames)

if __name__ == "__main__":
    main()
