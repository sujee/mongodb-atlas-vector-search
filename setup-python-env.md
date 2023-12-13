# Setup

## Pre-reqs

Have a python (preferrably Anaconda environment) environment

## Step-1: Setup Python Env

```bash
# need python 3.10 for torch libraries
conda create -n atlas-1 -y python=3.10
conda activate atlas-1
# make sure env is swithced to atlas-1
```

install all needed packages

```bash
pip install -r requirements.txt
ipython kernel install --user --name=atlas-1 
```

To manage kernels

```bash
jupyter kernelspec list

# remove unwanted kernel
jupyter kernelspec uninstall  KERNEL_NAME

```

check packages installed by 

```bash
conda list
```

## Step-2: Setup and Verify OpenAI API Key

```bash
cp   env.sample   .env
```

Edit .env file and add your OPENAI KEY in this format

```text
OPENAI_API_KEY=xyz-12345
```

Test openAI access

```bash
python   test-openai-key.py
```

you should see response.

That's it!  Now you are all setup!

## Step-3: To run jupyter:

If you already have Juptyer in in base anaconda env.  No need to install Jupyter in this env

If you don't have jupyter install as follows

```bash
conda install jupyterlab
```

Then start jupyter lab

```bash
jupyter lab
```

* navigate to the folder and open notebooks
* Choose kernel `atlas-1`
* Run the notebook
