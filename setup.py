import setuptools
from setuptools import setup, find_packages, find_namespace_packages
from setuptools.command.test import test as test_class
# from distutils.core import setup
from pathlib import Path
import sys
import unittest

if 'eny path':
    import youtube_dl_cli
    from youtube_dl_cli import __version__, __exe_name__, __author__, __description__


VERSION_NUMBER = __version__
DOWNLOAD_VERSION = __version__
PACKAGES_DIR = youtube_dl_cli.__name__
SETUP_NAME = PACKAGES_DIR.replace('_', '-')
ALIAS_NAME = __exe_name__
GITHUB_URL = f'https://github.com/CarsonSlovoka/{SETUP_NAME}/tree/master'

# find_package_modules = setuptools.command.build_py.build_py.find_package_modules


with open(Path(__file__).parent / Path('README.rst'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

with open(Path(__file__).parent / Path('requirements.txt')) as req_txt:
    LIST_REQUIRES = [line.strip() for line in req_txt if not line.startswith('#') and line.strip() != '']


def test_setup():
    from youtube_dl_cli.test.test_cli import CLITests
    suite_list = [unittest.TestLoader().loadTestsFromTestCase(class_module) for class_module in (CLITests, )]
    suite_class_set = unittest.TestSuite(suite_list)

    # suite_function_set = unittest.TestSuite()
    # suite_function_set.addTest(module.class('fun_name'))

    suite = suite_class_set  # pick one of two: suite_class_set, suite_function_set
    # unittest.TextTestRunner(verbosity=1).run(suite)  # self.verbosity = 0  # 0, 1, 2.  unittest.TextTestResult
    return suite


setup(
    name=SETUP_NAME,
    version=f'{VERSION_NUMBER}',  # x.x.x.{dev, a, b, rc}

    packages=find_packages(exclude=['youtube_dl_cli.test.*']),  # ignore modules

    include_package_data=True,  # include any data files it finds inside your package directories that are specified by your MANIFEST.in
    package_data={},  # {f'{PACKAGES_DIR}.config': ['gui.ui', f'static/{SETUP_NAME}/*.ico'],},
    license="Apache-2.0",
    author=' |'.join(__author__),
    author_email='jackparadise520a@gmail.com',

    install_requires=LIST_REQUIRES,

    url=GITHUB_URL,
    description=__description__,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/x-rst',
    keywords=['youtube', 'download'],

    download_url=f'{GITHUB_URL}/tarball/v{DOWNLOAD_VERSION}',
    python_requires='>=3.6.2,',

    zip_safe=False,
    classifiers=[  # https://pypi.org/classifiers/
        'Topic :: Multimedia :: Video',
        'Topic :: Multimedia :: Video :: Capture',
        'Topic :: Multimedia :: Sound/Audio :: Players',
        'Topic :: Multimedia :: Sound/Audio :: Players :: MP3',
        'Natural Language :: Chinese (Traditional)',
        'Natural Language :: English',
        'Operating System :: Microsoft',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    entry_points={
        'console_scripts': [
            f'{ALIAS_NAME}=youtube_dl_cli.cli:main',
        ],
    },
    test_suite='setup.test_setup',  # `python setup.py test` will call this function. # return value must is `suite`
)
