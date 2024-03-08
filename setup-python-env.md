# Setup a Local Python Developmnet Environment

## Step-1: Anaconda Python environment

You can install Anaconda by following the [guide here](https://www.anaconda.com/download/).

## Step-2: Create a custom environment

We will create an environment for this workshop with all the required libraries installed.

```bash
# need python 3.11 for torch libraries
conda create -n atlas-1 -y python=3.11

# activate the new conda environment
conda activate atlas-1
# make sure env is swithced to atlas-1
```

install all needed packages

```bash
pip install -r requirements.txt

ipython kernel install --user --name=atlas-1 

```

**Optional: Check env**

```bash
# see installed kernels
jupyter kernelspec list

# check installed packages
conda list
```

## Step-3: Install JupyterLab

If you already have JuptyerLab in in base anaconda env.  No need to install Jupyter in this env

If you don't have jupyter install as follows

```bash
conda install jupyterlab
```

Then start jupyter lab

```bash
jupyter lab
```

When running notebooks make sure you have `atlas-1` kernel selected.
