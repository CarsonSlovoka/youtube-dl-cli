__all__ = ('CLITests',)

import sys
from os import mkdir, scandir
from pathlib import Path
import shutil


if 'set env':
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from youtube_dl_cli.common.testHelper import ShowTestDescription, CLITestsBase
    from youtube_dl_cli.cli import main as cli_main
    from youtube_dl_cli.common.utils import after_end
    sys.path.remove(sys.path[0])


class CLITests(ShowTestDescription):
    def test_show_version(self):
        with self.assertRaises(SystemExit) as context_manager:
            cli_main(['--version'])
        self.assertEqual(context_manager.exception.code, 0)

    def test_show_help(self):
        with self.assertRaises(SystemExit) as context_manager:
            cli_main(['--help'])
        self.assertEqual(context_manager.exception.code, 0)


class BatchRunTests(CLITestsBase):
    def __init__(self, *args, **kwargs):
        super().__init__('batch_run', cli_main, *args, **kwargs)

    def test_show_help(self):
        with self.assertRaises(SystemExit) as context_manager:
            self.start_run(['--help'])
        self.assertEqual(context_manager.exception.code, 0)

    def test_run(self):
        self.start_run(['https://www.youtube.com/watch?v=LRLdhFVzqt4', 'https://www.youtube.com/watch?v=vbttZVTSJRU',
                        '--format', 'm4a', 'mp4_144p',
                        '--write_thumbnail'
                        ])

    def test_output_dir_is_working(self):
        temp_dir = Path(__file__).parent/Path('temp')
        shutil.rmtree(temp_dir, ignore_errors=True)

        mkdir(temp_dir)

        self.start_run(['https://www.youtube.com/watch?v=Wfkri2q6fKs',
                        '-f', 'm4a',
                        '--output_dir', temp_dir.absolute()
        ])

        list_video = [entry.path for entry in scandir(temp_dir) if entry.is_file()]
        with after_end(
            cb_fun=lambda: shutil.rmtree(temp_dir)  # make sure the temp_dir will remove after finished.
        ) as _:
            self.assertGreater(len(list_video), 0)



