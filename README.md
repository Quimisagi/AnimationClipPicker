# Clip Selection Tool

This Python program allows you to manually select clips from a dataset, enabling you to discard those clips that don’t meet the expectations for your model.

## How to Run

To execute the program, run the following command:

```bash
python main.py --parent_dir {path}
```

### Program Behavior

Upon running, the tool will load the paths of all the clips in the specified directory. The paths are stored in a `videos_path.txt` file, allowing you to easily resume your work.

### Interaction

- To **accept** a video, simply press the **Enter** key.
- To **decline** a video, press **'r'** or **Esc** key.
- To undo last action, press ***'u'***.

The paths of the accepted videos will be stored in a `.txt` file (default: `accepted_videos.txt`).

### Arguments

- **`parent_dir` (required)**:  
  The path to the dataset directory containing your clips.

- **`output_file`** *(default: `./accepted_videos.txt`)**:  
  This file stores the paths of the videos that have been accepted.

- **`fps`** *(default: 100)*:  
  Frames per second for processing the clips.

- **`minimum_frames`** *(default: 3)*:  
  The minimum frame threshold. Videos with fewer frames than this will be skipped.

  - **`restart`** *(optional)*:  
  If set to `True`, the process will restart from scratch, reloading both the video paths and state.

- **`random_selection`** *(optional)*:  
  Specify the number of clips to select randomly.
