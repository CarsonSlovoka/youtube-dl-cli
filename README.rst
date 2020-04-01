.. sectnum::

.. raw:: html

    <p align="left">

        <a href="https://pypi.org/project/youtube-dl-cli">
        <img src="https://img.shields.io/static/v1?&style=plastic&logo=pypi&label=App&message=youtube-dl-cli&color=00FFFF"/></a>

        <a href="https://pypi.org/project/youtube-dl-cli">
        <img src="https://img.shields.io/pypi/v/youtube-dl-cli.svg?&style=plastic&logo=pypi&color=00FFFF"/></a>

        <a href="https://pypi.org/project/youtube-dl-cli">
        <img src="https://img.shields.io/pypi/pyversions/youtube-dl-cli.svg?&style=plastic&logo=pypi&color=00FFFF"/></a>

        <a href="https://github.com/CarsonSlovoka/youtube-dl-cli/blob/master/LICENSE">
        <img src="https://img.shields.io/pypi/l/youtube-dl-cli.svg?&style=plastic&logo=pypi&color=00FFFF"/></a>

        <br>

        <a href="https://github.com/CarsonSlovoka/youtube-dl-cli">
        <img src="https://img.shields.io/github/last-commit/CarsonSlovoka/youtube-dl-cli?&style=plastic&logo=github&color=00FF00"/></a>

        <img src="https://img.shields.io/github/commit-activity/y/CarsonSlovoka/youtube-dl-cli?&style=plastic&logo=github&color=0000FF"/></a>

        <a href="https://github.com/CarsonSlovoka/youtube-dl-cli">
        <img src="https://img.shields.io/github/contributors/CarsonSlovoka/youtube-dl-cli?&style=plastic&logo=github&color=111111"/></a>

        <a href="https://github.com/CarsonSlovoka/youtube-dl-cli">
        <img src="https://img.shields.io/github/repo-size/CarsonSlovoka/youtube-dl-cli?&style=plastic&logo=github"/></a>

        <br>

        <a href="https://pepy.tech/project/youtube-dl-cli">
        <img src="https://pepy.tech/badge/youtube-dl-cli"/></a>

        <a href="https://pepy.tech/project/youtube-dl-cli/month">
        <img src="https://pepy.tech/badge/youtube-dl-cli/month"/></a>

        <a href="https://pepy.tech/project/youtube-dl-cli/week">
        <img src="https://pepy.tech/badge/youtube-dl-cli/week"/></a>

        <!--
        -->

    </p>

=================
youtube-dl-cli
=================

**A tool that can download the video from youtube and easier to use.**

INSTALL
=================

pip install youtube-dl-cli

USAGE
=================


::

    batch_run
           [-h] [-f [YLFormat [YLFormat ...]]] [--output_dir OUTPUT_DIR]
           [--write_thumbnail] [-q]
           [URL [URL ...]]

    positional arguments:
      URL                   youtube URL

    optional arguments:
      -h, --help            show this help message and exit
      -f [YLFormat [YLFormat ...]], --format [YLFormat [YLFormat ...]]
                            The output format. m4a mp4_144p mp4_240p mp4_360p
                            mp4_480p mp4_720p mp4_1080p gp3_176_144 gp3_320_240
                            flv webm mp4_640_360 mp4_1280_720 default:
                            mp4_640_360
      --output_dir OUTPUT_DIR
                            output directory. default: USERPROFILE/Music/my_music/
      --write_thumbnail     Write the thumbnail image to a file
      -q, --quite           Do not print messages to stdout.


- full command: ``ydl_cli batch_run "url_1" "url_2" --output_dir="C:/Users/Carson/Downloads" --format m4a mp4_144p --quiet  --write_thumbnail``
- voice only  : ``ydl_cli batch_run "url_1" -f m4a``

0.1.1
-----------------

- publish to PyPI

0.1.0
-----------------

- create setup.
- .circleci/config.yml

RELEASE NOTE
=================


0.0.1
-----------------

- create CLI

0.0.0
-----------------

- creating a core class: YoutubeKeeper
