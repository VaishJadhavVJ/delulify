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
from setuptools import setup, find_packages

setup(
    name="delulify",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "delulify=delulify.__main__:main",  # Creates the `delulify` CLI command
        ],
    },
    description="A Python CLI wrapper with emotionally supportive or roasting error messages for crashed scripts.",
    author="Vaishnavi Jadhav",
    author_email="vaishnavijadhav@example.com",  # Replace with your email
    url="https://github.com/your-repo/delulify",  # Replace with your repo URL
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    long_description="""
    Delulify is a Python CLI tool that wraps around your Python scripts. When your script crashes, 
    Delulify intercepts the traceback and provides you with emotionally supportive—or brutally 
    roast-worthy—error messages instead. Choose your vibe!
    """,
    long_description_content_type="text/markdown",
)