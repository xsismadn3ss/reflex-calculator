# REFLEX CALCULATOR
Learn how reflex works and wich best practices you need to know to build web apps with REFLEX.

## 1. Use reflex CLI to start a new project
To use **reflex**, you need to Create a new virtual environment in python and install the **reflex** package.

### a. Create a virtual environment
In python is recommended to use virtual environments if you are working on a new project, this is allows you to have a copy of the libraries that you are using on your project.

Every package that you install in the virtual environment is only in the directory that working on and it's not installed globally on your computer.

* Execute this command to create a new virtual environment
    ```bash
    python -m venv .venv
    ```

### b. Activate virtual environment
Every time when you are going to work on your project again, is necessary to activate the virtual environment. Don't forget to use this command to activate your project.
* Linux and MacOS
    ```bash
    source .venv/bin/activate
    ```
* Windows (powershell)
    ```powershell
    .venv/scripts/activate
    ```

### c. Install Reflex on your virtual environment

```bash
pip install reflex
```

### d. Create a new Reflex app
Execute ``reflex init`` to create a new app

This command install Node Js and create the .web directory to manage the frontend with javascript of your Reflex UI.
```bash
reflex init
```
* Select option 0 (press enter) to use  a blank template.
![reflex-init](/screenshots/image-1.png)