from setuptools import find_packages, setup

setup(
    name="model_name",
    packages=find_packages(exclude=["tutorial_notebook_assets"]),
    install_requires=[
        "dagster",
        "pandas",
        "matplotlib",
        "seaborn",
        "scikit-learn",
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
