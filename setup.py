from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ibis_loan_managment/__init__.py
from ibis_loan_managment import __version__ as version

setup(
	name="ibis_loan_managment",
	version=version,
	description="this app is for loan managment service",
	author="nextash.com",
	author_email="support@nextash.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
