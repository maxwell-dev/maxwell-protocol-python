import setuptools
import subprocess

#subprocess.check_call("bin/maxwell_protocol_gen.sh".split())

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().split("\n")

setuptools.setup(
    name="maxwell_protocol",
    version="0.1.0",
    author="Xu Chaoqian",
    author_email="chaoranxu@gmail.com",
    description="The maxwell protocol implementation for python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maxwell-dev/maxwell-protocol-python",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    )
)
