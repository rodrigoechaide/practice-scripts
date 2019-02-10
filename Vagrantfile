# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

#Matrix of ports to forward to the host machine [guest_port, host_port]
ports = [ [5000,5000], [9060, 9060], [9080, 9080], [9090, 9090] ]
vm_name = "practice-scripts"

Vagrant.configure("2") do |config|

    config.vm.box = "ubuntu/xenial64"
    config.vm.hostname = vm_name
    ports.each do |item|
        config.vm.network :forwarded_port, guest: item[0], host: item[1]
    end
    config.vm.provider "virtualbox" do |vb|
        vb.name = vm_name
        #vb.gui = true
        vb.memory = "1024"
    end
    config.vm.provision "shell", path: "deploy.sh"
end
