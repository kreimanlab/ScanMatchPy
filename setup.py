## >>>>>> Original MATLAB exported code for setup.py >>>>>>>>>>>>>>>>>>>>>>>>>>>
#
# Copyright 2015-2018 The MathWorks, Inc.

# from distutils.core import setup
# from distutils.command.clean import clean
# from distutils.command.install import install
#
# class InstallRuntime(install):
#     # Calls the default run command, then deletes the build area
#     # (equivalent to "setup clean --all").
#     def run(self):
#         install.run(self)
#         c = clean(self.distribution)
#         c.all = True
#         c.finalize_options()
#         c.run()
#
# if __name__ == '__main__':
#
#     setup(
#         name="matlabruntimeforpython",
#         version="R2019b",
#         description='A module to call MATLAB from Python',
#         author='MathWorks',
#         url='https://www.mathworks.com/',
#         platforms=['Linux', 'Windows', 'MacOS'],
#         packages=[
#             'ScanMatchPy'
#         ],
#         package_data={'ScanMatchPy': ['*.ctf']},
#         # Executes the custom code above in order to delete the build area.
#         cmdclass={'install': InstallRuntime}
#     )
#
## >>>>> Original MATLAB exported code for setup.py >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Conversion to use setuptools instead of disutils to make it compatible with pip

from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess

class InstallMatlabRuntime(install):
    def run(self):
        subprocess.call(['./install_matlab_runtime.sh'])
        install.run(self)

setup(
    name="ScanMatchPy",
    version="1",
    description='A python converted module of ScanMatch Toolbox for Matlab',
    packages=[
        'ScanMatchPy'
    ],
    package_data={'ScanMatchPy': ['*.ctf']},
    cmdclass={'install': InstallMatlabRuntime},
)
