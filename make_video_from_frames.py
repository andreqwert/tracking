import os
import sys
import numpy as np
import cv2
from tqdm import tqdm

w, h = 2048, 1024


def make_video_from_frames(path_to_imgs_folder, path_to_write_video, out_name='video', fps=1.0):

    data_names = sorted(os.listdir(path_to_imgs_folder))
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    video = cv2.VideoWriter(path_to_write_video+out_name+'.avi', fourcc, fps, (w, h)) #isColor=False

    for c, i in enumerate(data_names):
        if i.startswith('.'):
            continue

        print(c, i)
        img = cv2.imread(path_to_imgs_folder+i)
        print(path_to_imgs_folder+i)
        img = cv2.resize(img, (w, h))
        video.write(img) 
    cv2.destroyAllWindows()
    video.release()



path_to_imgs_folder = '/Users/user/Desktop/417/input/'
path_to_write_video = '/Users/user/Desktop/417/output/'


make_video_from_frames(path_to_imgs_folder, path_to_write_video)