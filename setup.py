from setuptools import setup, find_packages

setup(
    name="delulify",
    version="1.0.2",  # Remember to bump this if you edit code again!
    author="Vaishnavi Jadhav",
    author_email="119286282+VaishJadhavVJ@users.noreply.github.com",  # <--- UPDATED HERE
    description="Turns your runtime errors into emotionally supportive debugging hints.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/VaishJadhavVJ/delulify",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        "console_scripts": [
            "delulify=delulify.__main__:main",
        ],
    },
)