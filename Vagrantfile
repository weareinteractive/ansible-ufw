# -*- mode: ruby -*-
# vi: set ft=ruby :

$script = <<-SCRIPT
if [ -x "$(command -v apt-get)" ]; then
  sudo apt-get update
  sudo apt-get install -y python
elif [ -x "$(command -v pacman)" ]; then
  sudo pacman -S python --noconfirm
else
  printenv
fi
echo "done"
SCRIPT

Vagrant.configure("2") do |config|

  config.vm.define 'bionic' do |instance|
    instance.vm.box = 'ubuntu/bionic64'
  end

  config.vm.define 'xenial' do |instance|
    instance.vm.box = 'ubuntu/xenial64'
  end

  config.vm.define 'trusty' do |instance|
    instance.vm.box = 'ubuntu/trusty64'
  end

  config.vm.define 'stretch' do |instance|
    instance.vm.box = 'debian/stretch64'
  end

  config.vm.define 'jessie' do |instance|
    instance.vm.box = 'debian/jessie64'
  end

  config.vm.define 'archlinux' do |instance|
    instance.vm.box = 'archlinux/archlinux'
  end

  # install dependencies
  config.vm.provision "shell", inline: $script

  # View the documentation for the provider you're using for more
  # information on available options.
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "tests/main.yml"
    ansible.verbose = 'vv'
    ansible.become = true
  end
end
