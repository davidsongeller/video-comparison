import cv2
import imagehash
from PIL import Image
import os

def extract_frames(video_path, output_dir, interval=1):
    video = cv2.VideoCapture(video_path)
    success, image = video.read()
    count = 0

    while success:
        if count % interval == 0:
            frame_path = os.path.join(output_dir, f"frame{count}.jpg")
            cv2.imwrite(frame_path, image)
        success, image = video.read()
        count += 1

    video.release()

def calculate_image_hash(image_path):
    image = Image.open(image_path)
    hash_value = imagehash.average_hash(image)
    return str(hash_value)

def compare_image_hashes(hash1, hash2):
    hamming_distance = imagehash.hex_to_hash(hash1) - imagehash.hex_to_hash(hash2)
    similarity_threshold = 5
    return hamming_distance <= similarity_threshold

def compare_frames(frame1_path, frame2_path):
    frame1 = cv2.imread(frame1_path)
    frame2 = cv2.imread(frame2_path)

    # Implement feature matching or scene detection techniques using OpenCV
    # Compare the frames and return a similarity score or result indicating duplicates
    # Example: using the Structural Similarity Index (SSIM)
    gray_frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray_frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    similarity_score = cv2.matchTemplate(gray_frame1, gray_frame2, cv2.TM_SQDIFF_NORMED)

    return similarity_score

def analyze_files(file1_path, file2_path):
    file1_ext = os.path.splitext(file1_path)[1].lower()
    file2_ext = os.path.splitext(file2_path)[1].lower()

    if file1_ext == '.gif' and file2_ext == '.gif':
        hash1 = calculate_image_hash(file1_path)
        hash2 = calculate_image_hash(file2_path)
        if compare_image_hashes(hash1, hash2):
            print("The GIFs are duplicates.")
        else:
            print("The GIFs are not duplicates.")
    elif file1_ext == '.gif' or file2_ext == '.gif':
        print("Cannot compare a GIF with a video file.")
    else:
        frames1_dir = 'frames1'
        frames2_dir = 'frames2'

        os.makedirs(frames1_dir, exist_ok=True)
        os.makedirs(frames2_dir, exist_ok=True)

        extract_frames(file1_path, frames1_dir)
        extract_frames(file2_path, frames2_dir)

        frames1 = os.listdir(frames1_dir)
        frames2 = os.listdir(frames2_dir)

        for frame1 in frames1:
            for frame2 in frames2:
                similarity_score = compare_frames(os.path.join(frames1_dir, frame1), os.path.join(frames2_dir, frame2))
                if similarity_score <= 0.1:  # Adjust the threshold as needed
                    print("The videos have duplicate frames.")
                    return

        print("The videos do not have duplicate frames.")

        # Perform additional verification steps if needed

# Prompt the user to input paths to the files
file1_path = input("Enter the path to the first file: ")
file2_path = input("Enter the path to the second file: ")

analyze_files(file1_path, file2_path)
