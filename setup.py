from setuptools import setup, find_packages


# with open("requirements.txt") as f:
#     requirements = f.read().splitlines()


setup(
    name="my_package",
    version="0.0.1",
    description="My python package",
    packages=find_packages(),
    include_package_data=True,
    # install_requires=requirements,
)
