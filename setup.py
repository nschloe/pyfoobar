import os

from setuptools import find_packages, setup

# https://packaging.python.org/single_source_version/
base_dir = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(base_dir, "pyfoobar", "__about__.py"), "rb") as f:
    exec(f.read(), about)


setup(
    name="pyfoobar",
    version=about["__version__"],
    packages=find_packages(),
    url="https://github.com/nschloe/pyfoobar",
    project_urls={
        "Code": "https://github.com/nschloe/pyfoobar",
        "Issue tracker": "https://github.com/nschloe/pyfoobar/issues",
        # "Documentation": "https://packaging.python.org/tutorials/distributing-packages/",
        # "Funding": "https://donate.pypi.org",
        # "Say Thanks!": "http://saythanks.io/to/example",
        # "Source": "https://github.com/pypa/sampleproject/",
        # "Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    author=about["__author__"],
    author_email=about["__email__"],
    install_requires=[],
    description="A little bit of foobar in your life",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license=about["__license__"],
    classifiers=[
        about["__license__"],
        about["__status__"],
        # See <https://pypi.org/classifiers/> for all classifiers.
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    python_requires=">=3",
    entry_points={"console_scripts": ["pyfoobar-show = pyfoobar.cli:show"]},
)
