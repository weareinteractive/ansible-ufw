lint:
	ansible-lint .

ubuntu18.04:
	vagrant up bionic
	vagrant destroy -f bionic

ubuntu16.04:
	vagrant up xenial
	vagrant destroy -f xenial
