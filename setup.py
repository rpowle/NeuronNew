
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

Project_name="NeuronNew_pypi"
USERNAME="rpowle"

setuptools.setup(
    name=f"{project_name}-{USERNAME}",
    version="0.0.1",
    author="USERNAME",
    author_email="rajpowle12@gmail.com",
    description="its an implemntion of perceptron",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{USERNAME}/{project_name}",
    project_urls={
        "Bug Tracker": f"https://github.com/{USERNAME}/{project_name}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)