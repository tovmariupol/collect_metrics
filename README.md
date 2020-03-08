# Collection of Linux server metrics 

This project was written on Python as a  task for collecting standard metrics on a Ubuntu server using a docker container.

## Getting Started

This instruction will help you deploy the project on your Linux server.

### Prerequisites

You need to install Docker on Linux Server. All examples in this guide will be given for Ubuntu Server 18.04  

The following command will help you determine if a Docker package is installed on your system:
$ sudo apt list --installed | grep docker

If Docker is not installed on your server, then the following commands will help you to install one:

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
sudo apt-cache policy docker-ce
sudo apt-get install docker-ce docker-ce-cli containerd.io

By default, the docker command can only be run the root user or by a user in the docker group.
I recommend adding your user to the docker group, if you want to avoid typing sudo whenever you run
docker command.

sudo usermod -aG docker ${USER}

To apply the new group membership, log out of the server and back in, or type the following:

su - ${USER}

Confirm that your user is now added to the docker group by typing:

id -nG

If you added your user to the docker group, that you don't need to type the sudo before running docker command.

### Installing

To install create a folder for this project and copy the project files to it.
Create docker image:

docker build -t collect_metrics .

If there were no errors when building the image, then the scrip is ready to run.

## Running the tests

docker run --rm  collect_metrics  mem

Metric= mem
virtual total:   2089340928.00
virtual used:     338694144.00
virtual free:     175312896.00
virtual shared:     2834432.00
swap total:      2147479552.00
swap used:           274432.00
swap free:       2147205120.00

## Deployment

This project supports the collection of the following metrics for Linux server:
cpu, mem, disks, network, process 

CPU:
docker run  --rm  collect_metrics cpu

MEM:
docker run  --rm  collect_metrics mem

Disks:
docker run  --rm  collect_metrics disks

Network:
docker run --network=host --rm  collect_metrics  network

Process:
docker run -v /etc/passwd:/etc/passwd  --pid=host --rm  collect_metrics  process 

## Versioning

v1.0.1


## Authors

Oleh Tyshchenko

