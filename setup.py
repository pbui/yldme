"""yldme setup"""
import setuptools
import yldme

LONG_DESC = open('README.md').read()
# VERSION = yldme.__version__
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

VERSION = "0.0.1"
# DOWNLOAD = "https://github.com/dylanaraps/pywal/archive/%s.tar.gz" % VERSION

setuptools.setup(
    name="yldme",
    version=VERSION,
    author="Peter Bui",
    author_email="pbui@nd.edu",
    description="Pastebin and url shortener",
    long_description_content_type="text/markdown",
    long_description=LONG_DESC,
    keywords="pastebin url-shortnener",
    license="MIT",
    url="https://github.com/pbui/yldme",
    # download_url=DOWNLOAD,
    classifiers=[
        "Environment :: X11 Applications",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    packages=["yldme"],
    package_data={'': [
    'templates/*',
    'assets/css/*',
    'assets/css/pygments/*',
    'uploads/',]},
    install_requires=requirements,
    setup_requires=requirements,
    entry_points={"console_scripts": ["yldme=yldme.__main__:main"]},
    python_requires=">=3.5",
    test_suite="tests",
    include_package_data=True,
    zip_safe=False)
