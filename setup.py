from setuptools import setup, find_packages

setup(
    name='my_project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Add your project dependencies here.
        "requests",
        "unittest",
    ],
    entry_points={
        'console_scripts': [
            'my_project=my_project.main:main'
            #'mycommand=mypackage.mymodule:main_function',
        ]
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple example package",
    license="MIT",
    keywords="example tutorial",
    url="http://example.com/your_package_name",   # project home page
)
