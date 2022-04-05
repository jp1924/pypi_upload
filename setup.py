from setuptools import setup, find_packages

requirements = [
    "wheel",
    "setuptools",
    "transformers==4.17.0",
    "kobert-transformers @ git+https://github.com/monologg/KoBERT-Transformers.git@4e0a00e5e4884848fe4daeccf3698a28ebcfe449",
    "pandas",
    "matplotlib",
    "torch==0.10.0+cu111 -f https://download.pytorch.org/whl/torch_stable.html"
]

dependency = [
    "git+https://github.com/huggingface/transformers.git@stable/4.16.x=transformers-4.16.1"
]

setup(
    name="setup_test",
    version="0.1",
    author="jp",
    author_email="jsb1012129@gmail.com",
    url="https://github.com/jp1924/simcse",
    install_requires=requirements,
    python_requires="3.5.0>=3.6.0",
)