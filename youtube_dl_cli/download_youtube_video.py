__all__ = ('YoutubeKeeper', 'YLFormat')

import youtube_dl

import os
from pathlib import Path

from .structured import YLFormat

from typing import List, Tuple, Sequence, Iterable

from tkinter.messagebox import askokcancel
from tkinter import Tk
if 'withdraw tk':
    Tk().withdraw()


class YoutubeKeeper:
    __slots__ = ()

    @staticmethod
    def download(url: str, options: dict):
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([url])

    @staticmethod
    def start(download_list: Iterable[Tuple[str, Sequence[YLFormat]]],
              output_dir: Path = None,
              **options):
        if output_dir and not output_dir.exists():
            print(f'output_dir not exists: {output_dir}')
            return
        else:
            output_dir = Path(os.environ["USERPROFILE"]) / Path('Music/my_music')
            output_dir.mkdir(exist_ok=True)

        for cur_data in download_list:
            if not isinstance(cur_data, (tuple, list)) and len(cur_data) < 2:
                continue
            cur_url, tuple_format = cur_data
            for format_info in tuple_format:
                if not isinstance(format_info, YLFormat):
                    print(f'the format is not correct. format: {format_info}')
                    continue
                fmt_name, fmt = format_info.name, format_info.value
                try:
                    YoutubeKeeper.download(cur_url, dict(format=fmt,
                                                         # outtmpl=f"{Path(output_dir) / Path(f'%(title)s-{fmt_name}.%(ext)s')}",
                                                         outtmpl=f"{Path(output_dir) / Path(f'%(title)s.%(ext)s')}",
                                                         writethumbnail=options.get('writethumbnail'),
                                                         # ignoreerrors=True,
                                                         quiet=options.get('quiet')
                                                         ))
                except youtube_dl.utils.DownloadError:
                    print(f'download error: {cur_url} | {fmt_name}')

        if askokcancel('All done!', 'Open the music folder?'):
            os.startfile(output_dir)
        return
