# Cinemetrica is a collection of tools written in Python for the statistical analysis of movies.

# PySceneDetect imports:
import scenedetect
from scenedetect.video_manager import VideoManager
from scenedetect.scene_manager import SceneManager
from scenedetect.stats_manager import StatsManager
from scenedetect.detectors.content_detector import ContentDetector

# OpenCV, colorgram.py and PIL imports:
import colorgram
from PIL import Image, ImageDraw
import cv2

# Other imports:
import os
from tqdm import tqdm


# Returns a list containing all the shots detected as tuples of (start, end) FrameTimecodes.
def shot_detector(video_path):
    video_manager = VideoManager([video_path])
    stats_manager = StatsManager()
    scene_manager = SceneManager(stats_manager)
    scene_manager.add_detector(ContentDetector())
    shot_list = []
    video_manager.set_downscale_factor()
    video_manager.start()
    scene_manager.detect_scenes(frame_source=video_manager)
    shot_list = scene_manager.get_scene_list()
    video_manager.release()
    return shot_list


def get_shot_frames(video_path, image_format, quality, scale):
    if not os.path.isdir('FRAMES'):
        os.mkdir('FRAMES')
    video_manager = VideoManager([video_path])
    stats_manager = StatsManager()
    scene_manager = SceneManager(stats_manager)
    scene_manager.add_detector(ContentDetector())
    shot_list = []
    video_manager.set_downscale_factor()
    video_manager.start()
    scene_manager.detect_scenes(frame_source=video_manager)
    shot_list = scene_manager.get_scene_list()
    video_manager.release()
    scenedetect.scene_manager.save_images(shot_list, video_manager, 1, 1, image_format, quality,
                                          image_name_template='$VIDEO_NAME-$SCENE_NUMBER',
                                          output_dir='FRAMES', downscale_factor=scale, show_progress=True)


# Converts shot_list to a list of tuples (scene_number, duration(s)) if has_id = true,
# converts shot_list to a list of shot durations if has_id = false.
def list_convert(shot_list, has_id):
    new_list = []
    if has_id:
        for i in range(1, len(shot_list)):
            shot = [i, abs(shot_list[i][0].get_seconds() - shot_list[i - 1][0].get_seconds())]
            new_list.append(shot)
    else:
        for i in range(1, len(shot_list)):
            new_list.append(abs(shot_list[i][0].get_seconds() - shot_list[i - 1][0].get_seconds()))
    return new_list


# Returns the tuple (mean shot length, standard deviation), must have a shot_list list as the argument.
def mean_shot_length(shot_list):
    duration_list = list_convert(shot_list, False)
    total = 0
    sum_squares = 0
    for i in range(1, len(duration_list)):
        total += duration_list[i]
    mean = total / len(duration_list)
    for i in range(1, len(duration_list)):
        sum_squares += pow(i - mean, 2)
    std = pow(sum_squares / len(duration_list), 1 / 2)
    return [mean, std]


# Returns the last n longest shots in ascending order as tuples (sceneNumber, duration),
# must have a shot_list list as the argument.
def longest_n_shots(shot_list, n):
    new_list = list_convert(shot_list, True)
    new_list.sort(key=lambda x: x[1])
    print(new_list)
    final_list = []
    for i in range(len(new_list) - n, len(new_list)):
        final_list.append(new_list[i])
    return final_list


# Returns the first n shortest shots in ascending order as tuples (sceneNumber, duration),
# must have a shot_list list as the argument.
def shortest_n_shots(shot_list, n):
    new_list = list_convert(shot_list, True)
    new_list.sort(key=lambda x: x[1])
    print(new_list)
    final_list = []
    for i in range(0, n):
        final_list.append(new_list[i])
    return final_list


# Generates a n-color palette from an image.
def palette(path, n, width, height, id):
    colors = colorgram.extract(path, n)
    colors.sort(key=lambda c: c.hsl.h)
    palette_width = int(width / n)
    base_image = Image.new("RGBA", (width, height), None)
    image = ImageDraw.Draw(base_image)
    index = 0
    range_increment = 0
    while index < len(colors):
        color = colors[index]
        rgb = (getattr(color.rgb, 'r'), getattr(color.rgb, 'g'), getattr(color.rgb, 'b'))
        image.rectangle([range_increment, 0, range_increment + palette_width, height], fill=rgb, outline=None)
        index += 1
        range_increment += palette_width
    if not os.path.isdir('PALETTE'):
        os.mkdir('PALETTE')
    base_image.save(os.getcwd() + "\\PALETTE\\" + str(id) + ".png")


# Generates the palette for all images in folder 'FRAMES'.
def all_palette(frames_path, n, width, height):
    i = 0
    for file in tqdm(os.listdir(frames_path)):
        i += 1
        palette(frames_path + '/' + file + '', n, width, height, i)


def paletteTimeline():
    img1 = cv2.imread('PALETTE/' + str(1) + ".png")
    for i in tqdm(range(2, 138)):
        img2 = cv2.imread('PALETTE/' + str(i) + ".png")
        img1 = cv2.vconcat([img1, img2])
    cv2.imwrite('averagePalette2.jpg', img1)

