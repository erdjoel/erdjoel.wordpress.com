##virtualenv##

[virtualenv](http://pypi.python.org/pypi/virtualenv) is a tool to create isolated Python environments. 

virtualenv creates a folder which contains all the necessary executables to use the packages that a Python project would need.

It solves the “Project X depends on version 1.x but, Project Y needs 4.x” dilemma, and keeps your global 
site-packages directory clean and manageable. For example, you can work on a project which requires 
Django 1.3 while also maintaining a project which requires Django 1.0.

virtualenv installed by default by python 3

Create a virtual environment for a project:

`c:\>python -m venv myenv c:\path\to\myenv`

To begin using the virtual environment, it needs to be activated:

> execute activate.bat inside <venv folder>\Scripts\activate.bat

> or Activate.ps1 if using powershell window

The name of the current virtual environment will now appear on the left of the prompt 
(e.g.(venv)Your-Computer:your_project UserName$) to let you know that it’s active. 

From now on, any package that you install using pip will be placed in the venv folder, isolated from 
the global Python installation.

Install packages as usual, for example:
`(v_env_name)$ pip install requests`

If you are done working in the virtual environment for the moment, you can deactivate it:
`(v_env_name)$ deactivate`

This puts you back to the system’s default Python interpreter with all its installed libraries.

To delete a virtual environment, just delete its folder. 

In order to keep your environment consistent, it’s a good idea to “freeze” the current state of the environment 
packages. To do this, run
`$ pip freeze > requirements.txt`

This will create a requirements.txt file, which contains a simple list of all the packages in the current environment,  and their respective versions. You can see the list of installed packages without the requirements format using
`$ pip list`

to re-create the environment from requirement  (install the same packages using the same versions):
`$ pip install -r requirements.txt`

This can help ensure consistency across installations, across deployments, and across developers.

> Notes: Do remember to exclude the virtual environment folder from source control by adding it to the ignore list.

##virtualenvwrapper##

[virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/index.html) provides a set of commands which makes working with virtual environments much more pleasant. It also places all your virtual environments in one place.

For Windows, you can use the virtualenvwrapper-win.
To install (make sure virtualenv is already installed):
`$ pip install virtualenvwrapper-win`

In Windows, the default path for WORKON_HOME is %USERPROFILE%Envs
Basic Usage
`$ mkvirtualenv v_env_name #Create a virtual environment inside ~/Envs`
`$ workon v_env_name       #Work on a virtual environment`

Alternatively, you can make a project, which creates the virtual environment, and also a project directory 
inside $PROJECT_HOME, which is cd -ed into when you workon myproject.
`$ mkproject myproject`
`$ workon myproject`

virtualenvwrapper provides tab-completion on environment names. It really helps when you have a lot of 
environments and have trouble remembering their names.

workon also deactivates whatever environment you are currently in, so you can quickly switch between environments.

Deactivating is still the same:
`$ deactivate`

To delete:
`$ rmvirtualenv v_env_name`


Other useful commands

- `$ lsvirtualenv` List all of the environments
- `$ cdvirtualenv` Navigate into the directory of the currently activated virtual environment, so you can browse its site-packages, for example.
- `$ cdsitepackages` Like the above, but directly into site-packages directory.
- `$ lssitepackages` Shows contents of site-packages directory.
