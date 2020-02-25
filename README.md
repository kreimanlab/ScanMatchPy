# ScanMatchPy

This python package is built on top of [ScanMatch Matlab Toolbox](https://seis.bristol.ac.uk/~psidg/ScanMatch/) to compare saccadic eye movement sequences. Conversion is made using The Library Compiler in MATLAB® Compiler SDK™

The core matlab function uses the ScanMatch Toolbox to calculate mean scanpath score over two sets of eye saccades, each set having size of (num_stimuli, max_num_fixation, 2). Check [this](example.ipynb) example on how to use this package.

## Prerequisites
[Install and Configure the MATLAB Runtime](https://www.mathworks.com/help/compiler/install-the-matlab-runtime.html)

## Setup
Run the below command in terminal after cd'ing' to ScanMatchPy directory.
`python setup.py install`

## Original ScanMatch Matlab Toolbox paper
F. Cristino, S. Mathôt, J. Theeuwes & I. D. Gilchrist (2010). ScanMatch: A Novel Method for Comparing Fixation Sequences. Behaviour Research Methods, 42, 692-700.
