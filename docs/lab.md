## Overview

helayers-lab is based on HELayers which is written in C++ and includes a C++ API that enables data scientists and application developers to easily use the power of FHE by supporting a wide array of analytics such as Linear/Logistic Regression and Neural Networks. HELayers has been designed with a layered set of capabilities and coupled with appropriate APIs so users can fully utilize the services provided by the SDK. HELayers is delivered as an open platform, capable of using the latest FHE implementations for a given use case. It is enabled with patented optimization and performance boosting innovation for computation, AI innovation and use case requirements that facilitate the practical use of a wide variety of AI workloads over FHE data.

The demos use three backends: SEAL, HELib, and HEaaN. For most demos it is easy to switch between different backends, and explore which works best in each case.

## System Requirements

HElayers is a Linux based Docker image. The only requirement is a system that is capable of running a container, such as Docker, with the necessary user privileges to run docker commands. It is also assumed you have a working internet connection.

This image is built to run on all x86 64-bit architectures including Linux, macOS, and Windows.  When the container is running, interactions are through a C++ IDE accessed via the browser.


<br />


## License
This image is provided under a community edition license for non-commercial use; see [license](https://ibm.box.com/s/zfl6rt2p09811nyy8yow8t3mpsmkmsw6).
For commercial deployments and access to the source code, please contact jbuselli@us.ibm.com and rohit.panjala@ibm.com for the premium edition license.


<br />

## Call to Action
1. To help us create the best possible offering tailored to your needs, please provide feedback by taking the [HElayers Experience Survey](https://www.surveygizmo.com/s3/6494169/IBM-HElayers-SDK-Survey)


2. For more information on FHE, please visit our <a href="https://www.ibm.com/support/z-content-solutions/fully-homomorphic-encryption//" target=”_blank”>Content Solutions Page</a>


3. For more information on IBM HElayers, please visit our <a href="https://developer.ibm.com/blogs/secure-ai-workloads-using-fully-homomorphic-encrypted-data/" target=”_blank”>IBM Developer Blog</a>


<br />

## Installation

**Note: Do not expose the HElayers containers to unauthorized access.** Anyone with access to the container web interface will be able to execute code inside it. Only start the HElayers containers on local personal computers or on servers with controlled access.

### Step 1: Pull the Docker image
In your terminal pull this image from IBM Container Registry to your local repository.

    docker pull icr.io/helayers/helayers-lab:latest
    
If you specify `:latest`, it will always pull the most recent version.  However, if you are looking for a specific version you can replace `:latest` with the version number, such as `:1.0`.

If the fetch is successful, it will download the image and you will now have an image in your local repository named `icr.io/helayers/helayers-lab:latest`.  Check that this image exists with

    docker images
    

### Step 2: Running the image

Once the image download is complete, `run` the image as a container in Docker...  

    docker run -p 8443:8443 -d --rm --name helayers-lab icr.io/helayers/helayers-lab:latest
    
This command runs the image and sets the container to be accessed via port 8443.  It also gives the container a name called `helayers-lab`, which we can use to find it in the list of other running containers.

### Step 3: Access HElayers

Open a web browser on your host machine (not the docker container instance), and browse to [http://127.0.0.1:8443/ ](http://127.0.0.1:8443/ ).  This will connect you to the welcome page of the VS Code.  

Note: if you run the web browser in different machine than the docker container, then you need to change the IP address of the URL.

### Step 4: Getting Started with the tutorials

Click on the application menu (three bars icon, top left), and
Choose Terminal > New Terminal

In the terminal change directory to examples/<demoName>

Follow the directions in the readme file of that demo.

Available demos:

#### Hebase tutorial

Basic layer 1 (hebase - abstract layer) tutorial. It 
demonstrates helayer's low level API for manipulating ciphertexts directly.

#### Neural network tutorials

Step by step tutorials how to use the C++ API for NN inference

#### Linear regression

Compute linear regression using encrypted model and data.

#### Logistic Regression Inference on a Credit Card Fraud Detection Dataset

Build a logistic regression model encrypted under HE, and run inference of encrypted samples from a dataset of credit card transactions.

#### Nearest neighbor
Encrypt a set of centroids and find nearest neighbor under HE.
Given an encrypted samples, we compute the distance between each sample and each centroid under encryption. On the client side, the results are decrypted and automatically post-processed to obtain the nearest neighbor.

#### Bitwise tutorial

Tutorial explaining the bitwise API (implemented with the BGV scheme)

#### Decicion tree inference

Decision tree inference for credit card fraud detection

#### Neural network demos

Neural network inference for MNIST, medical, and credit-card fraud datasets.
Note that the neural network tutorials above are more recommended for beginners.

#### BGV world country db lookup

Encrypted query over an encrypted database.
Uses the BGV scheme, and Fermat's little theorem to compute equality over the modular arithmetic supplied by the scheme.
