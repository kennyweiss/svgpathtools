from setuptools import setup
import codecs
import os


VERSION = '1.4.2'
AUTHOR_NAME = 'Andy Port'
AUTHOR_EMAIL = 'AndyAPort@gmail.com'
GITHUB = 'https://github.com/mathandy/svgpathtools'


def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    HERE = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


setup(name='svgpathtools',
      packages=['svgpathtools'],
      version=VERSION,
      description=('A collection of tools for manipulating and analyzing SVG '
                   'Path objects and Bezier curves.'),
      long_description=read("README.md"),
      long_description_content_type='text/markdown',
      author=AUTHOR_NAME,
      author_email=AUTHOR_EMAIL,
      url=GITHUB,
      download_url='{}/raw/1.4.1/dist/svgpathtools-{}.tar.gz'.format(GITHUB, VERSION),
      license='MIT',
      install_requires=['numpy', 'svgwrite'],
      platforms="OS Independent",
      requires=['numpy', 'svgwrite'],
      keywords=['svg', 'svg path', 'svg.path', 'bezier', 'parse svg path', 'display svg'],
      classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Topic :: Multimedia :: Graphics :: Editors :: Vector-Based",
            "Topic :: Scientific/Engineering",
            "Topic :: Scientific/Engineering :: Image Recognition",
            "Topic :: Scientific/Engineering :: Information Analysis",
            "Topic :: Scientific/Engineering :: Mathematics",
            "Topic :: Scientific/Engineering :: Visualization",
            "Topic :: Software Development :: Libraries :: Python Modules",
            ],
      )
