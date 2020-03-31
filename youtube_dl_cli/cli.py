import sys
from pathlib import Path

if 'set env':
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from youtube_dl_cli import __version__, __exe_name__
    from youtube_dl_cli.download_youtube_video import YLFormat, YoutubeKeeper
    from youtube_dl_cli.common.consoleHelper import text_color, Fore

    sys.path.remove(sys.path[0])

from typing import NewType
import argparse

Name = NewType('Name', str)


class CLI:
    """Command Line Interface"""

    __slots__ = ()

    BATCH_RUN: Name = 'batch_run'

    @classmethod
    def build_parser(cls):
        def init_common_parameter(sub_parser):
            ...

        def init_batch_fix(sub_parser: argparse.ArgumentParser):
            init_common_parameter(sub_parser)  # the bach_fix is
            sub_parser.add_argument('url_list', help='youtube URL',
                                    metavar='LIST',
                                    nargs='*')  # convert to list automatically

            sub_parser.add_argument('-f', '--format', help=f'The output format. {text_color(f"  ".join([msg for msg in YLFormat.__members__]))}'
                                                           f'  default: {text_color("mp4_640_360", Fore.BLUE)}',
                                    metavar='YLFormat',
                                    default=YLFormat.mp4_640_360,
                                    nargs='*',  # multiple choice.
                                    choices=[key for key in YLFormat.__members__]
                                    )

            sub_parser.add_argument('--output_dir', help='output directory. default: USERPROFILE/Music/my_music/',
                                    type=Path, default=None,
                                    )

            sub_parser.add_argument('--write_thumbnail', help='Write the thumbnail image to a file',
                                    action='store_true',
                                    dest='write_thumbnail')

            sub_parser.add_argument('-q', '--quite', help='Do not print messages to stdout.',
                                    action='store_true',
                                    dest='quiet')

        description = 'A tool that can download the video from youtube and easier to use.'
        usage = '\n'.join([desc for desc in
                           ['@',
                            'full command: ' + text_color(f'{__exe_name__} batch_run "url1" "url2" --output_dir="C:/Users/Carson/Downloads" --format m4a mp4_144p --quiet  --write_thumbnail'),
                            'voice only  : ' + text_color(f'{__exe_name__} batch_run "url1" -f m4a'),
                            '@'
                            ]])
        main_parser = argparse.ArgumentParser(prog=f'{__exe_name__}.exe',
                                              description=description,
                                              usage=usage,
                                              formatter_class=argparse.RawTextHelpFormatter)
        main_parser.add_argument('--version', action='version', version='%(prog)s \n\tversion:' + f'{__version__}')

        sub_cmd: argparse._SubParsersAction = main_parser.add_subparsers(
            title='Available commands', dest='sub_cmd',
            metavar=''  # metavar='SUBCOMMAND', help='DESCRIPTION'
        )
        sub_cmd.required = True

        batch_fix = sub_cmd.add_parser(cls.BATCH_RUN, help='Automated Batch Processing')
        init_batch_fix(batch_fix)

        return main_parser


def main(cmd_list: list = None):
    cli = CLI()
    parser = cli.build_parser()
    args = parser.parse_args(cmd_list) if cmd_list else parser.parse_args()

    fmt_list = [eval(f'{YLFormat.__name__}.{fmt}') for fmt in args.format]
    download_list = [(url, fmt_list) for url in args.url_list]
    options = dict(writethumbnail=args.write_thumbnail,
                   quiet=args.quiet)

    dict_run_app = {cli.BATCH_RUN: lambda: YoutubeKeeper.start(download_list, output_dir=args.output_dir, **options)}

    app_name = args.sub_cmd
    dict_run_app[app_name]()
    return 'FINISHED'


if __name__ == '__main__':
    """
    main()
    """
    # main(['--version'])
    # main(['--help'])
    main(['batch_run', '--help'])
