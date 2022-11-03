import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='SpaceMAP',
    version='0.0.1',
    author='',
    author_email='',
    description='',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='',
    project_urls = {
        "Bug Tracker": ""
    },
    license='MIT',
    packages=['umap.utils'],
    install_requires=['requests'],
)
