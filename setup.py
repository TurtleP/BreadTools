from setuptools import setup, find_packages

setup(
    name='BreadTools',
    version='0.1.0',
    url='',
    author='TurtleP',
    license='MIT',
    description="Pbanj's Windows Registry Tools",
    install_requires=['pyqt5', 'winreg'],
    packages=find_packages(),
    entry_points={'gui_scripts': ['BreadTools=BreadTools.__main__:main']}
)
