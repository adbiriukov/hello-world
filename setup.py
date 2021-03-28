from setuptools import setup


VERSION = '1.0'

install_requires = [
    'pytest>=3.5.1',
    'pytest-rerunfailures>=4.1',
    'allure-pytest>=2.5.0',
    'allure-python-commons>=2.5.0'
    'selenium>=3.141.0'
    'ddt>=1.4.2'
]


def main():
    setup(
        name='allure_tests',
        version=VERSION,
        install_requires=install_requires
    )


if __name__ == '__main__':
    main()
