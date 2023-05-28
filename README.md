# video-comparison
analyzes two video or gif files to attempt to identify duplicates 

# Video and GIF Duplicate Analyzer

This Python program allows you to analyze GIFs and videos to identify duplicates with varying content. It combines multiple techniques and libraries to achieve accurate results.

## Features

- Supports analysis of both GIFs and videos.
- Uses OpenCV and FFmpeg for video processing and frame extraction.
- Applies feature extraction algorithms (e.g., SIFT or SURF) to capture distinctive visual features from frames.
- Provides different duplicate detection methods, including feature matching, scene detection, and deep learning-based approaches.
- Assigns similarity scores and thresholds to determine duplicates.
- Performs additional verification steps for accuracy.

## Requirements

- Python 3.x
- OpenCV
- FFmpeg
- PIL (Python Imaging Library)
- imagehash
- (Add any additional libraries or dependencies here)

## Usage

1. Clone the repository or download the source code.

2. Install the required dependencies using the following command:

`pip install opencv-python ffmpeg-python pillow imagehash`

4. Follow the prompts to provide the paths to the input files for analysis.

`python main.py`

## Customization

- Adjust the threshold values and similarity metrics in the code to suit your specific needs and desired level of sensitivity.
- Modify or extend the duplicate detection methods and verification steps based on your requirements.

## Limitations

- The program currently supports GIFs, videos, and frame-based duplicate analysis. Other file formats or specialized analysis techniques are not included in this version.

## Contributing

Contributions are welcome! If you encounter any issues, have suggestions, or would like to add new features, please feel free to submit a pull request or open an issue.

## License

GPL-3.0 License

