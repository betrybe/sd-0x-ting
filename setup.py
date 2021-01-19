from setuptools import setup

setup(
    name="ting",
    description="Projeto ting",
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "ting-collector=src.menu:menu",
        ],
    },
)
