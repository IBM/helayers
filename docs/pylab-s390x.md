# Overview

helayers-pylab-s390x is based on HELayers which is written in C++ and includes a Python API that is designed to enable application developers and data scientists to seamlessly apply advanced privacy preserving techniques without requiring specialized skills in cryptography - all while working in a newly integrated Python environment. HElayers is engineered to support a wide array of analytics such as linear regression, logistic regression, and neural networks so that application developers and data scientists can use the power of FHE. It is delivered as an open platform that is capable of using the latest FHE schemes and libraries for a given use case and ships with a multitude of tutorials and sample applications that highlight the basics of FHE and how to use this technology in a practical way. Sample applications include credit card fraud detection, encrypted database search, text classification, and various examples from the healthcare industry.

## System Requirements

Helayers is a Linux based Docker image.  The only requirement is a system that is capable of running a container, such as Docker, with the necessary user privileges to run docker commands. It is also assumed you have a working internet connection.

This image is built to run on all zSystems architectures including Linux on IBM Z (z16 and LinuxOne III), and zCX Container Extensions.

## License

This image is provided under a community edition license for non-commercial use; see [license](https://ibm.box.com/s/zfl6rt2p09811nyy8yow8t3mpsmkmsw6).
For commercial deployments and access to the source code, please contact [chamliam@ie.ibm.com](mailto:chamliam@ie.ibm.com) for the Premium Edition license.

## Call to Action

1. To help us create the best possible offering tailored to your needs, please provide feedback by taking the [HElayers Experience Survey](https://www.surveygizmo.com/s3/6494169/IBM-HElayers-SDK-Survey)

2. For more information on FHE, please visit our <a href="https://www.ibm.com/support/z-content-solutions/fully-homomorphic-encryption//" target=”_blank”>Content Solutions Page</a>

3. For more information on IBM HElayers, please visit our <a href="https://developer.ibm.com/blogs/secure-ai-workloads-using-fully-homomorphic-encrypted-data/" target=”_blank”>IBM Developer Blog</a>

# Getting Started

To get started with HElayers, follow our [instructional setup video](https://www.youtube.com/watch?v=_bEMWffloas&ab_channel=IBMResearch) or continue to the Installation section.

[![Fully Homomorphic Encryption](http://img.youtube.com/vi/_bEMWffloas/0.jpg)](https://www.youtube.com/watch?v=_bEMWffloas "Getting Started with HELayers")

## Installation

**Note: Do not expose the HElayers containers to unauthorized access.** Anyone with access to the container web interface will be able to execute code inside it. Only start the HElayers containers on local personal computers or on servers with controlled access.

### Step 1: Pull the Docker image

In your terminal pull this image from IBM Container Registry to your local repository.

    docker pull icr.io/helayers/helayers-pylab-s390x:latest

If you specify `:latest`, it will always pull the most recent version.  However, if you are looking for a specific version you can replace `:latest` with the version number, such as `:1.0`.

If the fetch is successful, it will download the image and you will now have an image in your local repository named `icr.io/helayers/helayers-pylab-s390x:latest`.  Check that this image exists with

    docker images


### Step 2: Run the image

Once the image download is complete, `run` the image as a container in Docker...

    docker run -p 8888:8888 -d --rm --name helayers-pylab-s390x icr.io/helayers/helayers-pylab-s390x:latest

This command runs the image and sets the container to be accessed via port 8888.  It also gives the container a name called `helayers-pylab-s390x`, which we can use to find it in the list of other running containers.

### Step 3: Access HElayers

Open a web browser on your host machine (not the docker container instance), and browse to [http://127.0.0.1:8888/lab/?token=demo-experience-with-fhe-and-python ](http://127.0.0.1:8888/lab/?token=demo-experience-with-fhe-and-python).  This will connect you to the welcome page of the Juptyer notebook.

Note: if you run the web browser in different machine than the docker container, then you need to change the IP address of the URL.

### Step 4: Get started with the tutorials and demo applications

Open the first notebook, by double clicking the one titled `00_Getting_Started.ipynb`.  This is a notebook that contains information about the different tutorials that are available, as well as instructions on how to run each one.
