from enum import Enum


class YLFormat(Enum):
    m4a = '140'  # audio only
    mp4_144p = '160'
    mp4_240p = '133'
    mp4_360p = '134'
    mp4_480p = '135'
    mp4_720p = '136'
    mp4_1080p = '137'
    gp3_176_144 = '17'  # 3gp: 176*144
    gp3_320_240 = '36'
    flv = '5'
    webm = '43'
    mp4_640_360 = '18'  # 640 * 360
    mp4_1280_720 = '22'
