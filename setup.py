from setuptools import setup, find_packages


setup(
    name="keras_custom_ImageDataGenerator",
    version="1.0",
    packages=find_packages(),
    install_requires=["rasterio>=0.1"],
)