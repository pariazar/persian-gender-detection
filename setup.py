import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PGD",                     
    version="0.0.2",                        
    author="Hamed Pariazar",                     
    description="it can detect gender by firstName",
    long_description=long_description,      
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      
    python_requires='>=3.6',                
    py_modules=["persianutils","re","pandas","pgd"],             
    package_dir={'':'.'},     
    install_requires=[]                     
)