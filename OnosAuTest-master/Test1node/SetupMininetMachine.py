import subprocess
import re
import os
import time

#CONSTANTS
mkdir=""
update = "sudo apt-get update"
upgrade = "sudo apt-get upgrade -y"
installgit = "sudo apt-get install git-all -y"
installzip = "sudo apt-get install zip -y"
installunzip = "sudo apt-get install unzip -y"
installcurl = "sudo apt-get install curl -y"
installpy2 = "sudo apt-get install python -y && sudo apt-get install python-pip python-dev python-setuptools -y"
installpy3 = "sudo apt-get install python3 -y && sudo apt-get install python3-pip python3-dev python3-setuptools -y"
installpip = "pip3 install --upgrade pip"
installselenium = "pip3 install selenium"
installBazelisk = "wget https://github.com/bazelbuild/bazelisk/releases/download/v1.4.0/bazelisk-linux-amd64 && chmod +x bazelisk-linux-amd64 && sudo mv bazelisk-linux-amd64 /usr/local/bin/bazel"
installJava11 = "sudo apt-get install openjdk-11-jdk openjdk-11-jre -y"
installrequests= "pip install requessudo adduser --disabled-password sdnts"
addUsersdn= "echo -ne '\n' |sudo adduser --disabled-password sdn"
addsdntosudoGroup= "sudo usermod -aG sudo sdn "
changeshelltoSH = "sudo usermod -s /bin/bash sdn"
setsudowithoutpassword = "echo 'sdn ALL=(ALL) NOPASSWD:ALL' | sudo tee --append /etc/sudoers"
gitOnos = "git clone https://gerrit.onosproject.org/onos"
gitOnosSystemtest = "git clone https://gerrit.onosproject.org/OnosSystemTest"
gitMininet = "git clone https://github.com/jhall11/mininet.git;cd mininet;git checkout -b dynamic_topo origin/dynamic_topo;cd util;sudo ./install.sh -3fvn"
cellPath = "/home/ubuntu/onos/tools/test/cells"
installconfigObj = "sudo pip install configObj"
mininetclidriverPath = "/home/ubuntu/OnosSystemTest/TestON/drivers/common/cli/emulator"

subprocess.call(update, shell = True)
subprocess.call(upgrade, shell = True)
subprocess.call(addUsersdn, shell = True)
subprocess.call(addsdntosudoGroup, shell = True)
subprocess.call(changeshelltoSH, shell = True)
subprocess.call(setsudowithoutpassword, shell = True)

subprocess.call("cp /home/ubuntu/.ssh/id_rsa /home/ubuntu/.ssh")
subprocess.call("cp /home/ubuntu/.ssh/id_rsa.pub /home/ubuntu/.ssh")

subprocess.call("sudo chmod 600 .ssh/id_rsa")
subprocess.call("sudo chmod 644 .ssh/id_rsa.pub")
subprocess.call("sudo su - sdn -c 'mkdir .ssh'")
subprocess.call("sudo cp /home/ubuntu/.ssh/id_rsa.pub /home/sdn/.ssh/id_rsa.pub")
subprocess.call("sudo cp /home/ubuntu/.ssh/id_rsa /home/sdn/.ssh/id_rsa")
subprocess.call("sudo cp /home/ubuntu/.ssh/id_rsa.pub /home/sdn/.ssh/authorized_keys")

subprocess.call("sudo chgrp sdn /home/sdn/.ssh/id_rsa")
subprocess.call("sudo chown sdn /home/sdn/.ssh/id_rsa")
subprocess.call("sudo chown sdn /home/sdn/.ssh/id_rsa.pub")
subprocess.call("sudo chgrp sdn /home/sdn/.ssh/id_rsa.pub")
subprocess.call("sudo chgrp sdn /home/sdn/.ssh/authorized_keys")
subprocess.call("sudo chown sdn /home/sdn/.ssh/authorized_keys")

subprocess.call(gitMininet)