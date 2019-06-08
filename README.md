# foobar

[![CircleCI](https://img.shields.io/circleci/project/github/nschloe/foobar/master.svg)](https://circleci.com/gh/nschloe/foobar/tree/master)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/foobar.svg)](https://codecov.io/gh/nschloe/foobar)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![PyPi Version](https://img.shields.io/pypi/v/foobar.svg)](https://pypi.org/project/foobar)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/foobar.svg?logo=github&label=Stars&logoColor=white)](https://github.com/nschloe/foobar)

A Python project template; can be used as a [GitHub
template](https://github.blog/2019-06-06-generate-new-repositories-with-repository-templates/) for your new Python project.

### What you can do with this template

* First run
```
find . -type f -name "*.py" -o -name Makefile -o -name "*.yml" -print0 | xargs -0 sed -i 's/pyfoobar/your-project-name/g'
```
and rename the folder `foobar` to customize the name.

* Run `make black` to apply [black](https://github.com/python/black) formatting.
* Run `make lint` to run [flake8 linting](http://flake8.pycqa.org/en/latest/)
* Run `make publish` to
   - tag your project on git (`make tag`)
   - upload your package to PyPi (`make upload`)

After publishing, people can install your package with
```
pip3 install --user foobar
```

### Testing

To run the foobar unit tests, check out this repository and type
```
pytest
```

### License

foobar is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
