from setuptools import setup, find_packages

setup(name='signet',
      version='0.0.0',
      description="Package to manipulate mutational processes.",
      url='https://github.com/OleguerCanal/signatures-net',
      packages=find_packages(),
      install_requires=[
            'torch==1.7.0',
            'scipy==1.6.1',
            'numpy==1.19.5',
            'matplotlib==3.3.4',
            'pandas==1.2.3',
            'seaborn==0.11.1',
            'scikit_optimize==0.8.1',
            'tqdm==4.59.0',
            'pyparsing==2.4.7',
            'gaussian_process==0.0.14',
            'PyYAML==6.0',
            'scikit_learn',
            'openpyxl',
      ])