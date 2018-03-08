# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vbguest.no_remote = true
  config.vbguest.auto_update = false

  config.vm.define 'xenial' do |instance|
    instance.vm.box = 'ubuntu/xenial64'
  end
  #config.vm.provision "shell", inline: "sudo apt-get update"
  #config.vm.provision "shell", inline: "sudo apt-get install -y python"

  config.vm.define 'archlinux' do |instance|
    instance.vm.box = 'archlinux/archlinux'
  end
  config.vm.provision "deps", type: "shell", inline: "sudo pacman -S python --noconfirm"

  # View the documentation for the provider you're using for more
  # information on available options.
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "tests/main.yml"
    ansible.verbose = 'vv'
    ansible.become = true
  end
end
