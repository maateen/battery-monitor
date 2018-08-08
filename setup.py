import setuptools

setuptools.setup(
    name="battery-monitor",
    install_requires=[
        "pygobject",
    ],
    entry_points={
        "console_scripts": [
            "battery-monitor=battery_monitor.run:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={
        '': ['icons/*.png'],
    },
    classifiers=(
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: POSIX :: Linux",
    ),
)
