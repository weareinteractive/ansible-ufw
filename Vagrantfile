# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vbguest.no_remote = true

  config.vm.define 'xenial' do |instance|
    instance.vm.box = 'ubuntu/xenial64'
  end

  config.vm.provision "shell", inline: "sudo apt-get update"
  config.vm.provision "shell", inline: "sudo apt-get install -y python"

  # View the documentation for the provider you're using for more
  # information on available options.
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "tests/main.yml"
    ansible.verbose = 'vv'
    ansible.become = true
  end
end
