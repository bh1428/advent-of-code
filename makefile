#
# makefile for Advent of Code
#

VENV_DIR := .venv
UV := uv
ifeq ($(OS),Windows_NT)
	SHELL := powershell.exe
	.SHELLFLAGS := -NoProfile -Command
	VENV := .\$(VENV_DIR)\Scripts
	VENV_ACTIVATE := $(VENV)\activate.bat
else
	SHELL := bash
	VENV := ./$(VENV_DIR)/bin
	VENV_ACTIVATE := $(VENV)/activate
endif

all: sync

.NOTPARALLEL:

.PHONY: init
init: $(VENV_ACTIVATE)

$(VENV_ACTIVATE):
	$(UV) venv
    ifeq (,$(wildcard requirements.txt))
		$(UV) pip compile pyproject.toml -o requirements.txt
    endif
    ifeq (,$(wildcard dev-requirements.txt))
		$(UV) pip compile pyproject.toml --extra dev -o dev-requirements.txt
    endif
	$(UV) pip sync dev-requirements.txt --allow-empty-requirements
	$(UV) pip install -e .

requirements.txt: $(VENV_ACTIVATE) pyproject.toml
	$(UV) pip compile pyproject.toml -o requirements.txt

dev-requirements.txt: $(VENV_ACTIVATE) pyproject.toml
	$(UV) pip compile pyproject.toml --extra dev -o dev-requirements.txt

.PHONY: upgrade_all
upgrade_all: upgrade_uv upgrade_requirements sync

.PHONY: upgrade_requirements
upgrade_requirements: $(VENV_ACTIVATE)
	$(UV) pip compile pyproject.toml --upgrade -o requirements.txt
	$(UV) pip compile pyproject.toml --upgrade --extra dev -o dev-requirements.txt

.PHONY: upgrade_uv
upgrade_uv:
	$(UV) self update

.PHONY: sync
sync: $(VENV_ACTIVATE) requirements.txt dev-requirements.txt
	$(UV) pip sync --allow-empty-requirements dev-requirements.txt
	$(UV) pip install -e .

.PHONY: list
list: $(VENV_ACTIVATE)
	$(UV) pip list
