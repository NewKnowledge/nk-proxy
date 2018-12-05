from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="nk_proxy",
    version="1.0.0",
    description="A proxy wrapper package for the upstream proxy service",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/NewKnowledge/nk-proxy',
    packages=["nk_proxy"],
    include_package_data=True,
    install_requires=["requests"],
    license="MIT",
)