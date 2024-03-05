from setuptools import setup

setup(
    name='PalmTree',
    url='https://github.com/eric86y/PalmTree',
    author='Eric Werner',
    author_email='eric.werner.mail@gmail.com',
    packages=['PalmTree'],
    install_requires=[
        "PySide6==6.6.1",
    ],
    version='0.1',
    license='MIT',
    description='A slim GUI for a convenient OCR Workflow.',
    long_description=open('README.md').read(),
)