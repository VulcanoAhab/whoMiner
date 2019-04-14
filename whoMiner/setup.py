from distutils.core import setup

setup(
    name="whoMiner",
    version='0.1.0',
    author="VulcanoAhab",
    packages=["whoMiner"],
    url="https://github.com/VulcanoAhab/whoMiner.git",
    description="",
    install_requires=[
          "ipwhois",
          "dnspython"
      ],
)
