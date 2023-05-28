`extract_frames()`uses OpenCV to read frames from the video at a specified interval and saves them as individual images in the output directory.

`calculate_image_hash()` uses the `imagehash` library to calculate the average hash value for an image.

`compare_image_hashes()` compares two image hashes using the Hamming distance and a similarity threshold. If the Hamming distance is below the threshold, the images are considered duplicates.

`compare_frames()` compares two frames using the Structural Similarity Index (SSIM) provided by OpenCV. You can replace this implementation with other techniques like feature matching or scene detection.

`analyze_files()` handles the main logic of the program. It checks the file extensions to determine if the input files are GIFs or videos. If they are GIFs, it uses the image hashing technique to check for duplicates. If they are videos, it extracts frames, compares them, and determines if there are duplicate frames.

##Remember to adjust the threshold values and similarity metrics:

###line 16 
`compare_image_hashes() #adjust threshold value`

Hamming Distance Threshold:
   - The Hamming distance threshold in the `compare_image_hashes()` function (line 16) determines the maximum number of bit differences allowed between two image hashes to consider them similar. A lower threshold means stricter matching, while a higher threshold allows more dissimilar images to be considered duplicates.
> If you set `similarity_threshold = 5`, images with a Hamming distance of 5 or less would be considered similar.

###Line 26
`compare_frames() #adjust similarity score threshold`

Structural Similarity Index (SSIM) Score:
   - The SSIM score in the `compare_frames()` function (line 26) represents the similarity between two frames. A higher SSIM score indicates greater similarity, while a lower score suggests more dissimilarity.
>If you set `similarity_score <= 0.1`, frames with an SSIM score of 0.1 or below would be considered similar.
