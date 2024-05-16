from moviepy.editor import VideoFileClip, clips_array


def concat_videos_side_by_side(video_path1, video_path2, output_path):
    # Load the videos
    video1 = VideoFileClip(video_path1)
    video2 = VideoFileClip(video_path2)

    # Ensure the videos have the same duration
    min_duration = min(video1.duration, video2.duration)
    video1 = video1.subclip(0, min_duration)
    video2 = video2.subclip(0, min_duration)

    # Concatenate videos side by side
    final_clip = clips_array([[video1, video2]])

    # Write the result to a file
    final_clip.write_videofile(output_path, codec="libx264")


# Example usage for the Egypt videos:
concat_videos_side_by_side(
    "./static/videos/renders/Egypt/2024-05-06-19-20-33-nobg.mp4",
    "./static/videos/renders/Egypt/2024-05-06-19-20-33.mp4",
    "./static/videos/renders/Egypt/output-egypt-comparison.mp4",
)

# Example usage for the library videos:
concat_videos_side_by_side(
    "./static/videos/renders/library/2024-05-02-12-45-03-nobg.mp4",
    "./static/videos/renders/library/2024-05-02-12-45-03.mp4",
    "./static/videos/renders/library/output-library-comparison.mp4",
)

# Example usage for the floating-tree videos:
concat_videos_side_by_side(
    "./static/videos/renders/floating-tree/2024-05-02-18-01-45-nobg.mp4",
    "./static/videos/renders/floating-tree/2024-05-02-18-01-45.mp4",
    "./static/videos/renders/floating-tree/output-floating-tree-comparison.mp4",
)

# Example usage for the train videos:
concat_videos_side_by_side(
    "./static/videos/renders/train/2024-05-02-12-29-01-nobg.mp4",
    "./static/videos/renders/train/2024-05-02-12-29-01.mp4",
    "./static/videos/renders/train/output-train-comparison.mp4",
)
