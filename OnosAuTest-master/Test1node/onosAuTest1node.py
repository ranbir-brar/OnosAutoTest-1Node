import subprocess
import re
import time
import os

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

#asking user for ip adresses
manageMachineIP = raw_input("Please enter the ip address for manage machine:")
mininetMachineIP = raw_input("Please enter the ip address for mininet machine:")
targetMachineIP1 = raw_input("Please enter the ip address for target 1 machine:")
privatekeyLocation = raw_input("Please enter the absolute file path of your private key:")
publickeyLocation = raw_input("Please enter the absolute file path of your public key:")
testcase = raw_input("Please enter the name of the test you would like to run")

projectPath = os.getcwd()

subprocess.call("cp {} {}/id_rsa".format(privatekeyLocation,projectPath), shell = True)
subprocess.call("cp {} {}/id_rsa.pub".format(publickeyLocation,projectPath), shell = True)

privatekeyLocation = projectPath+"/id_rsa"
publickeyLocation = projectPath+"/id_rsa.pub"

subprocess.call("sudo chmod 600 .ssh/id_rsa", shell = True)
#connect to Manage Machine (ubuntu user)

subprocess.call('ssh -i {} ubuntu@{}'.format(privatekeyLocation,manageMachineIP),shell = True)

#installing softwares on manage machine
subprocess.call(update, shell = True)
subprocess.call(upgrade, shell = True)
subprocess.call(installgit, shell = True)
subprocess.call(installzip, shell = True)
subprocess.call(installunzip, shell = True)
subprocess.call(installcurl, shell = True)
subprocess.call(installpy2, shell = True)
subprocess.call(installpy3, shell = True)
subprocess.call(installpip, shell = True)
subprocess.call(installselenium, shell = True)
subprocess.call(installBazelisk, shell = True)
subprocess.call(installJava11, shell = True)
subprocess.call(installrequests, shell = True)
subprocess.call(installselenium, shell = True)
subprocess.call(addUsersdn, shell = True)
subprocess.call(addsdntosudoGroup, shell = True)
subprocess.call(changeshelltoSH, shell = True)
subprocess.call(setsudowithoutpassword, shell = True)

subprocess.call('cp {} /home/ubuntu/.ssh'.format(privatekeyLocation),shell = True)
subprocess.call('cp {} /home/ubuntu/.ssh'.format(publickeyLocation),shell = True)

subprocess.call("sudo chmod 600 .ssh/id_rsa", shell = True)
subprocess.call("sudo chmod 644 .ssh/id_rsa.pub", shell = True)
subprocess.call("sudo su - sdn -c 'mkdir .ssh'", shell = True)
subprocess.call("sudo cp /home/ubuntu/.ssh/id_rsa.pub /home/sdn/.ssh/id_rsa.pub", shell = True)
subprocess.call("sudo cp /home/ubuntu/.ssh/id_rsa /home/sdn/.ssh/id_rsa", shell = True)
subprocess.call("sudo cp /home/ubuntu/.ssh/id_rsa.pub /home/sdn/.ssh/authorized_keys", shell = True)
subprocess.call(gitOnos, shell = True)

subprocess.call("echo 'export ONOS_ROOT=~/onos' | sudo tee --append /home/ubuntu/.bashrc", shell = True)
subprocess.call("echo 'source $ONOS_ROOT/tools/dev/bash_profile' | sudo tee --append /home/ubuntu/.bashrc", shell = True)
subprocess.call("source .bashrc", shell = True)

subprocess.call(installconfigObj, shell = True)
subprocess.call(gitOnosSystemtest, shell = True)
subprocess.call("cd OnosSystemTest/TestON/ ; ./install.sh", shell = True)

#subprocess.call("cp ", projectPath , "/oneNodeDemo.txt ", projectPath, "/oneNodeDemo.txt")

#filling oneNodeDemo text file with proper parameters
filename="oneNodeDemo.txt"
with open(filename, 'r+') as f:
    text = f.read()
    text = re.sub("IPadd1", targetMachineIP1)
    text = re.sub("IPadd2", mininetMachineIP)
    f.write(text)
    f.truncate()

#Upload oneNodeDemo under cell
subprocess.call ("cp {}/oneNodeDemo.txt {}".format(projectPath,cellPath), shell=True)

#Upload SetupMininetMachine.py and SetupTargetMachine.py to the manage machine
subprocess.call("cp {}/SetupMininetMachine.py /home/ubuntu/OnosSystemTest".format(projectPath),shell=True)
subprocess.call("cp {}/SetupTargetMachine.py /home/ubuntu/OnosSystemTest".format(projectPath),shell=True)

#Set up mininet Machine
subprocess.call("cd OnosSystemTest; python SetupMininetMachine.py ubuntu {}".format(mininetMachineIP),shell=True)

#Set up target machine
subprocess.call("cd OnosSystemTest; python SetupTargetMachine.py ubuntu {}".format(targetMachineIP1),shell=True)

subprocess.call("exit",shell=True)

subprocess.call('ssh -i {} sdn@{}'.format(privatekeyLocation,manageMachineIP),shell = True)
subprocess.call("sudo chmod 700 /home/sdn/.ssh",shell=True)
subprocess.call("sudo chmod 644 /home/sdn/.ssh/authorized_keys",shell=True)
subprocess.call(gitOnos,shell=True)
subprocess.call("echo 'export ONOS_ROOT=~/onos' | sudo tee --append /home/sdn/.bashrc",shell=True)
subprocess.call("echo 'source $ONOS_ROOT/tools/dev/bash_profile' | sudo tee --append /home/sdn/.bashrc",shell=True)
subprocess.call("source .bashrc",shell=True)

subprocess.call("cd onos; bazel build onos",shell=True)
subprocess.call("sudo chgrp sdn /home/sdn/.ssh/id_rsa",shell=True)
subprocess.call("sudo chown sdn /home/sdn/.ssh/id_rsa",shell=True)
subprocess.call("sudo chown sdn /home/sdn/.ssh/id_rsa.pub",shell=True)
subprocess.call("sudo chgrp sdn /home/sdn/.ssh/id_rsa.pub",shell=True)
subprocess.call("sudo chgrp sdn /home/sdn/.ssh/authorized_keys",shell=True)
subprocess.call("sudo chown sdn /home/sdn/.ssh/authorized_keys",shell=True)
subprocess.call("exit",shell=True)

subprocess.call('ssh -i {} ubuntu@{}'.format(privatekeyLocation,manageMachineIP),shell = True)
subprocess.call("cell oneNodeDemo; cd ~/OnosSystemTest/TestON/bin/; ./cli.py run {}".format(testcase),shell=True)