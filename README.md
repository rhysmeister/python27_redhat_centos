Role Name
=========

Install python2.7 on RedHat/CentOS 6 based systems that come with Python 2.6 by default. The default system installation is not touched.

Role Variables
--------------

python_download_url: Url for python download.
python_sha256: sha256 checksum for above python archive.
python_archive: Python archive. Dynamically set.
python_directory: Python directory. Dynamically set.
python_build_root: Directory where we build python
python_exec_path: Path to our new pthon 2.7 executable
python_expected_version: The expected output from the command set in python_exec_path what passed the --version flag.
