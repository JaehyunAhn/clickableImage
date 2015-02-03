# -*- coding: utf-8 -*-
from imageLoadandPoint import *
"""
Filename: mainModule
Author: Sogo
Project title: Yerago image processing
Contribution date: 03/02/2015

Sogang University (c) All rights reserved
"""

# get image list
image_dir = collect_images('./testData')

# open image and point out images
load_and_point_images(image_dir,
                      file_path='./testData')