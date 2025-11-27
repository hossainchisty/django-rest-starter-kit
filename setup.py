from setuptools import setup, find_packages

setup(
    name="django-rest-starter-kit",
    version="1.21.2",
    packages=find_packages(),
    license="MIT",
    description="Starter kit for Django Rest Framework projects",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Hossain Chisty",
    author_email="hossain.chisty11@gmail.com",
    url="https://github.com/hossainchisty/django-rest-starter-kit",
    install_requires=[
        "django",
        "djangorestframework",
        "rest_framework_simplejwt",
        "drf_yasg",
    ],
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    include_package_data=True,  # include files from MANIFEST.in
)
