# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant::Config.run do |config|
  # http://files.vagrantup.com/precise64.box
  config.vm.box = "precise64"
  
  config.vm.network :hostonly, "192.168.33.10"
  config.vm.network :bridged
  config.vm.forward_port 80, 8080
  config.vm.share_folder "repository", "/repository", "./"
  config.vm.customize ["modifyvm", :id, "--memory", 1024]
end
