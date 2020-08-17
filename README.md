# OnosAutoTest-1Node
Script to run 1 node Onos System Tests automatically

This README file shows how to run ONOS Sytem testcases that require 1 node.

For more information about ONOS System Testing please read: [ONOS Sytem Testing Guide] (https://wiki.onosproject.org/display/ONOS/System+Testing+Guide)

*You don't need to install any softwares or create users on any VMs because the script will do all that automatically. You only need to create the VMs manually. 

##Setup test script to run 1 node tests
### On the Compute Canada Cloud

1. First check if you have ssh key in ~/.ssh, if you don't have one, please generate it by using the following command:
`ssh-keygen -t rsa -m PEM`

**Note that don't setup the password here**
After generating a key please upload this public key to the ***Key Pairs*** in Compute Canada. 

2. Create 3 VMs manually (1 manage machine, 1 mininet machine, 1 target machine).

### Open Test1node folder
This folder contains 4 files:
* oneNodeDemo.txt - text file which contains the parameters for the cell setup. 
* onosAuTest1node.py - main file which sets up environment for test cases
* SetupMininetMachine.py - sets up environment on manage machine (mininet)
* SetupTargetMachine.py  - sets up environemnt on target machine

The main file we need to run is **onosAuTest1node.py*
We can run it by inputting the following command:
`python onosAuTest1Node.py`

Then you input 3 ip addresses (the public network up for the manage machine and the intranet ip for the other machines) and the location of the public key and private key. This file can be used to run any of the 1 node onos system tests. 
