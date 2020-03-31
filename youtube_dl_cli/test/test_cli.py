import sys
from pathlib import Path

if 'set env':
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from youtube_dl_cli.common.testHelper import ShowTestDescription, CLITestsBase
    from youtube_dl_cli.cli import main as cli_main

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
