---
toc: true
toc_label: "Table of Contents"
header:
  image: /assets/images/docker_splash.png
  teaser: /assets/images/animated_teaser.png
---
Docker is very useful for creating a virtual machine of sorts. This can be run
on any computer and should provide the same environment making it a great tool
for e.g. developing consistently as part of a team.
{: .text-justify}

## Requirements

-   [Docker](https://www.docker.com)


## Image Definition

The Docker image is defined in the `Dockerfile` which is run in sequence and
must start with a `FROM` directive. An example sequence of commands in the
`Dockerfile` is given below.
{: .text-justify}

  ```bash
  # Select the base image.
  FROM continuumio/anaconda3

  # Set environment variables.
  ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
  LABEL version="1.0"
  ```

The `FROM` instruction provides a base image upon which to build. There are
many available options for this, accessed through the
[Docker Hub](https://hub.docker.com). As the majority of the work we do is
related to scientific programming in python, a good base image is provided by
Continuum, with the Anaconda python 3 build. This perhaps isn't the most
efficient way to generate an image, as there will be over 100 python packages
preinstalled. However, it is a relatively easy way to get a lot of
functionality quickly. Once the base image has been specified, we then set
environment variables such as language and labels.
{: .text-justify}

  ```bash
  # Create the root directory.
  RUN mkdir project_name
  COPY . /project_name/
  ENV HOME=/project_name
  ENV SHELL=/bin/bash
  VOLUME /project_name
  WORKDIR /project_name
  ```

Once the initial setup has been defined, it is necessary to establish the
directory structure, as above. Under the assumption that the Docker image is
generated for a specific project, the project directory is copied into a new
folder and set as the `$HOME` directory. This makes it easy to get up and
running as quickly as possible when loading the image.
{: .text-justify}

  ```bash
  # Set the PYTHONPATH.
  ENV PYTHONPATH=$PWD/:$PYTHONPATH

  # Install additional python packages.
  RUN pip install pytest-cov pyinstrument
  ```

For python projects, we add the required folders to the `$PYTHONPATH`. Finally,
any additional python packages can be installed with pip. This will then give
an environment in which we can develop as we normally would, but with some
added flexibility and no need to edit our local setup.
{: .text-justify}


## Running Image

To start with, it is necessary to install Docker from
[here](https://www.docker.com). Once installed and running, we can load up
containers from the image defined in the `Dockerfile`. In order to start a
Docker container, we run the following commands:
{: .text-justify}

  ```shell
  $ docker build -t project_name .
  $ docker run -it project_name bash
  ```

This will load up the environment in the `$HOME` directory set in the
`Dockerfile`. From here it is possible to run any tests or example scripts as
one otherwise would.
{: .text-justify}

To exit the container, just press `ctrl + d`.

Docker images can get quite large and take up a lot of space. It is
occasionally a good idea to check what images are available and perhaps clean
things up.
{: .text-justify}

  ```shell
  $ docker images
  $ docker system prune
  ```

  There is some good advice on maintaining reasonably sized images
  [here](https://blog.codacy.com/five-ways-to-slim-your-docker-images-5f4bd68d29f1).
  {: .text-justify}


## Summary

This is a very basic example of how one could set up a Docker image for
development of a small project. It should be noted that typically CI can
use images from Docker Hub, meaning it is possible to create the same
environment for development, testing, and deployment.
{: .text-justify}
