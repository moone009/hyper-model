# Copyright 2019 Growing Data Pty Ltd [https://growingdata.com.au]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages

NAME = "titanic"
VERSION = "0.0.01"
REQUIRES = [
    "click",
    "kfp",
    "xgboost",
    "pandas",
    "hypermodel",
]

setup(
    name=NAME,
    version=VERSION,
    description="Tragic Titanic Machine Learning Demo",
    author="Growing Data",
    install_requires=REQUIRES,
    packages=find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.5.3",
    include_package_data=True,
    entry_points={"console_scripts": ["titanic = titanic.__main__:main"]},
)
