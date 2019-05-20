prj-dir := $(shell pwd)
src-dir := $(prj-dir)/maxwell
venv-dir := $(prj-dir)/venv
python-native := python3
python-venv := $(venv-dir)/bin/python
nose := $(venv-dir)/bin/nose2
pip := $(venv-dir)/bin/pip

define get_site_dir
$(shell $(python-venv) -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")
endef

init: create-env install-deps set-path gen

create-env:
	$(python-native) -m venv $(venv-dir)

install-deps:
	$(pip) install -r requirements.txt

set-path:
	echo $(src-dir) > $(call get_site_dir)/my.pth

gen:
	$(prj-dir)/bin/maxwell_protocol_gen.sh

test: init
	$(nose)

clean:
	$(prj-dir)/bin/maxwell_protocol_clean.sh
	rm -rf $(venv-dir) $(prj-dir)/build $(prj-dir)/dist ${prj-dir}/maxwell_protocol.egg-info
