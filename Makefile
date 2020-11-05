.DEFAULT_GOAL:=help
DISTROS=centos8 centos7 ubuntu2004 ubuntu1804 ubuntu1604 debian9
MAKEFLAGS+=-s

# --- Macros ------------------------------------------------------------------

# print error: ${.err}
.err=$(error ${2})

# list of all args: $(call .args,NUM)
.args=$(patsubst +%,,$(filter-out $@, $(MAKECMDGOALS)))
# single arg at position: $(call .args.req,NUM)
.args.arg=$(word ${1}, ${.args})
# required arg: $(call .args.req,NUM,ERROR)
.args.req=$(if ${.args.arg},${.args.arg},${.err})

# --- Targets -----------------------------------------------------------------

%: # This allows us to accept extra arguments
	@:

## Run linters
## Usage: make lint
lint:
	yamllint .
	ansible-lint .

## Generate README.md
## Usage: make readme
readme:
	@ansible-readme

## Print distros
## Usage: make distros
distros:
	echo "${DISTROS}"

## Start running your role
## Usage: make converge DISTRO
converge: distro=$(call .args.req,1,Missing DISTRO)
converge:
	@MOLECULE_DISTRO=${distro} molecule converge

## Shutdown your role
## Usage: make destroy
destroy:
	@molecule destroy

## Run your test
## Usage: make test DISTRO
test: distro=$(call .args.req,1,Missing DISTRO)
test:
	@MOLECULE_DISTRO=${distro} molecule test

## Show help text
help:
	@awk '{ \
		if ($$0 ~ /^.PHONY: [a-zA-Z\-\_0-9]+$$/) { \
			helpCommand = substr($$0, index($$0, ":") + 2); \
			if (helpMessage) { \
				printf "\033[36m%-23s\033[0m %s\n", \
					helpCommand, helpMessage; \
				helpMessage = ""; \
			} \
		} else if ($$0 ~ /^[a-zA-Z\-\_0-9.]+:/) { \
			helpCommand = substr($$0, 0, index($$0, ":")); \
			if (helpMessage) { \
				printf "\033[36m%-23s\033[0m %s\n", \
					helpCommand, helpMessage"\n"; \
				helpMessage = ""; \
			} \
		} else if ($$0 ~ /^##/) { \
			if (helpMessage) { \
				helpMessage = helpMessage"\n                        "substr($$0, 3); \
			} else { \
				helpMessage = substr($$0, 3); \
			} \
		} else { \
			if (helpMessage) { \
				print "\n                        "helpMessage"\n" \
			} \
			helpMessage = ""; \
		} \
	}' \
	$(MAKEFILE_LIST)
