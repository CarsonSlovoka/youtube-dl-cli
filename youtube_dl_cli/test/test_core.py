import sys
from pathlib import Path

if 'set env':
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from youtube_dl_cli.download_youtube_video import YLFormat
    from youtube_dl_cli.common.testHelper import ShowTestDescription
    from youtube_dl_cli.download_youtube_video import YoutubeKeeper

    sys.path.remove(sys.path[0])


class DownloadTests(ShowTestDescription):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.options = dict()  # writethumbnail, quiet
        self.yk = YoutubeKeeper()

    def test_download_voice_only(self):
        self.yk.start([('https://www.youtube.com/watch?v=vbttZVTSJRU', [YLFormat.m4a, ])]),

    def test_download_mp4(self):
        self.yk.start([('https://www.youtube.com/watch?v=vbttZVTSJRU', [YLFormat.m4a, YLFormat.mp4_640_360])])

    def test_multiple_format(self):
        self.yk.start([('https://www.youtube.com/watch?v=vbttZVTSJRU', [YLFormat.m4a, YLFormat.mp4_640_360, YLFormat.mp4_1280_720])]),

    def test_download_from_list(self):
        self.yk.start([
            ('https://www.youtube.com/watch?v=LRLdhFVzqt4', [YLFormat.m4a, ]),
            ('https://www.youtube.com/watch?v=vbttZVTSJRU', [YLFormat.m4a, ]),
        ], **self.options),

    def test_write_thumbnail(self):
        self.options['writethumbnail'] = True
        self.yk.start([('https://www.youtube.com/watch?v=LRLdhFVzqt4', [YLFormat.m4a, YLFormat.mp4_640_360])])
