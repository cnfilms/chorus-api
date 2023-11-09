import setuptools

setuptools.setup(
    name="chorus-api",
    version="1.0.5",
    author="Joel ONIPOH",
    author_email="technique@cinego.net",
    description="Chorus API Package https://piste.gouv.fr",
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    url="https://github.com/cnfilms/chorus-api",
    keywords=["python", "chorus", "api", "piste", "chorus piste"],
    packages=setuptools.find_packages(),
    install_requires=[r.strip() for r in open('requirements.txt').read().splitlines()],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7'
)
