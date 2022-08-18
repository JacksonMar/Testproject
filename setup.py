
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# with io.open("requirements.txt") as f:
#     required = f.read().splitlines()
#
# with io.open("Readme.md", encoding="utf-8") as f:
#     long_description = f.read()

def main():
    setup(
        name='testproject',
        version='1.0',
        description='My testproject',
        long_description="long_description",
        long_description_content_type="text/markdown",
        url='https://github.com/JacksonMar/Testproject',
        author='Ievgen Marinoshenko',
        author_email='contact@demo.com',
        packages=['src',
                  'src.pages',
                  'tests',
                  'tests.ui'],


        # package_dir={'mypackage.utils': 'mypackage/utils',
        #              'mypackage.manager': 'mypackage/manager',
        #              'mypackage.creator': 'mypackage/creator'},
        install_requires=[
            'allure-pytest<=2.9.45',
            'allure-python-commons<=2.9.45',
            "atomicwrites<=1.4.1",
            "attrs<=22.1.0",
            "certifi<=2022.6.15",
            "charset-normalizer<=2.1.0",
            "colorama",
            "configparser",
            "crayons",
            "idna",
            "iniconfig",
            "more-itertools",
            "packaging",
            "pluggy",
            "py",
            "pyparsing",
            "pytest",
            "pytest-html",
            "pytest-metadata",
            "pytest-testconfig",
            "requests",
            "selenium",
            "six",
            "tomli",
            "urllib3",
            "webdriver-manager"],

        include_package_data=True,
        keywords="mypackage for product test",

    )


if __name__ == '__main__':
    main()
