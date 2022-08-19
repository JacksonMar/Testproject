
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
            "colorama<=0.4.5",
            "configparser<=5.2.0",
            "crayons<=0.4.0",
            "idna<=3.3",
            "iniconfig<=1.1.1",
            "more-itertools<=8.14.0",
            "packaging<=21.3",
            "pluggy<=1.0.0",
            "py<=1.11.0",
            "pyparsing<=3.0.9",
            "pytest<=7.1.2",
            "pytest-html<=1.19.0",
            "pytest-metadata<=2.0.2",
            "pytest-testconfig<=0.1.0",
            "requests<=2.28.1",
            "selenium<=4.4.2",
            "six<=1.16.0",
            "tomli<=2.0.1",
            "urllib3<=1.26.11",
            "webdriver-manager<=3.8.3"],

        include_package_data=True,
        keywords="mypackage for product test",

    )


if __name__ == '__main__':
    main()
