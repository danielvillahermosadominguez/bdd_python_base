# Quick guide to start with this example

We have used to configure this environment:
* Visual studio code
* virtualenv as virtual environment
*  Python 3.10.5 or +

From the terminal you can use the following commands to start:
1. Install the virtual environment 
``` bash
    pip install virtualenv
    python -m venv .\venv   
```
2. Activate the environment -- (windows) 
```
    .\venv\Scripts\activate.bat
```
3. Install dependencies 
``` bash
    pip install -r requirements.txt
```
4. Execute the unit tests
``` bash
    pytest  
```
5. Execute coverage 
``` bash
    coverage run -m pytest     <- generate the coverage    
    coverage report <- you can see in the terminal
    coverage html <- an html report is generated
```
6. Execute Behave (BDD) 
``` bash
    behave
```
If everything has going well you can open your IDE. 

## Using Visual Studio Code
* From the terminal go to the "bdd_python_base" folder
* type "code ." and the visual studio code will be open
* Install a plugin for Guerkin syntax. For example: Feature Syntax Highlight and snippets(Cucumber/Guerkin)
  * Ctrl+Shift+P -> Python:Configure Test->pytest. You can execute the test with Test Explorer
  * Or with "Run and debug" -> Select "Unit test execution"

NOTE:If you have some problem with the test explorer, you could reconfigurate it if you remove the .vscode/settings.json and configure it again.

## Using PyCharm
* Open PyCharm an close the projects (if you have an open project)
* Open the folder "bdd_python_base" 
* Open <No interpreter> (In the right-down corner) -> Interpreter settings -> Add interpreter-> add local interpeter -> Virtualenv environment
* Select Evironment: Existing
* Select the folder <your folder>\venv\Scripts\python.exe and click ok
* Open Run-> Edit configurations-> + ->Python Test -> Pytest
  * Check your Python interpeter is the interpreter you have created in your folder
  * Select the target the folder "bdd_python_base" 
* Open Run-> Edit configurations-> + ->Behave
 * Check your Python interpeter is the interpreter you have created in your folder

# Detailed information about the environment preparation
If you want to prepare all the environment from Zero, you have here all the steps and considerations. If you don't want to do it, you don't need to read the following information.

If you have problems with the setup, maybe this information could be useful to find the solution.

## 1. Installing and activating the virtual environment 
Create a folder, for example: c:\workspace\bdd_python_base 

You need to have python installed in your machine and pip.

``` bash 
pip install virtualenv
python -m venv .\venv
```

You must activate the virtual environment. Al the dependencies will be installed in this environment
```
-- In windows
.\venv\Scripts\activate.bat
-- In Linux
venv/Scripts/activate
```

You will see the text "(venv)"" in the console. This is an indicator you are in the virtual environment.

Now,  you will need to install the dependencies:

## 2. Installing the dependencies

``` bash
pip install -r requirements.txt
``` 

## 3. Configuring the Visual Studio Code

* Open your Visual Studio Code and click on "File->Open folder". Select the folder where you have created the environment. In this case "c:\workspace\bdd_python_base"
* Now click in Run->Add configuration->Python. You will see a new folder called :".vscode/launch.json"
  
You will need this launch.json
```
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: current file",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        },
        {
            "name": "BDD execution",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/venv/Scripts/Behave.exe",
            "console": "integratedTerminal",
            "args": [
                "--tags=~@Skip"
            ],
            "cwd": "${workspaceFolder}"
        },
        {
            "name": "Unit Test execution",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/venv/Scripts/pytest.exe",
            "console": "integratedTerminal"
        },
    ]
}
```

## 4. first 'Hello world in python'

 Create a file, for example helloworld.py and write the following code:
``` python
   print("Hello World"); 
``` 

You can execute in the terminal:

``` PS
(venv) PS C:\workspace\python\bdd_python_base> python helloworld.py
Hello World

```

Or, if you have configurated Visual Studio code, select the file "helloworld.py" and you have two options:
* Run-> Run without Debuging
* Run-> Run with Debuging => you could use breakpoints

## 5. installing pytest and your first unit test

In the dependencies "requirements.txt" pytests has been included. So, you shouldn't need to install it.

By default, pytest is going to look for test in every file that starts in with the sufix "test_" but we could
create a pytest.ini file to setup the test folders. For example

You can create your first dummy unit test:
``` bash 
    dummy <-- your production code
        __init__.py
        dummy.py
    tests  <-- your test code
        __init__.py
        dummy
            __init__.py
            test_dummy.py
```

For this, you will need the following python.ini file:
``` ini
# pytest.ini
[pytest]
testpaths =
    tests
    integration (<- you could create more than one folder. We won't need it)
```

## 6. pytest with visual studio code

You need to go to the icon of "Testing" -> Configure Python tests->pytest (pytest framework) and select the folder  "c:\workspace\bdd_python_base". 
* Ctrl+Shift+P -> Python:Configure Test->pytest

NOTE:If you have some problem with the test explorer, you could reconfigurate it if you remove the .vscode/settings.json and configure it again.

Or with "Run and debug" -> Select "Unit test execution"


## 7. coverage

Something interesting is to have coverage. The coverage library has been include in the requirements.txt, so you shouldn't have to include it.
https://coverage.readthedocs.io/en/7.1.0/

You will need a configuration file: ".coveragerc" with the following configuraiton
``` ini
    [html]
    directory = html-coverage
    [run]
    omit = 
        dummy/__init__.py
        tests/*   
```
       
Some interesting commands to generate the coverage
``` bash
    
    -- generate the file .coverage
    coverage run -m pytest (todo)
    coverage run -m pytest arg1 , arg2 (ficheros)    

    -- generate the report of coverage in the console or html
    coverage report 
    coverage html
```  

## 8. Behave configuration
he coverage library has been include in the requirements.txt, so you shouldn't have to include it. Some interesting links:
* https://github.com/behave/behave
* https://behave.readthedocs.io/en/stable/install.html
* https://www.tutorialspoint.com/behave/behave_quick_guide.htm


We need to create a folder for the features in c:\workspace\bdd_python_base\src\features\dummy.feature with the following:
``` Guerkin
Feature: Dummy Feature

Scenario: Dummy Scenario
Given a dummy given
When a dummy thing happens
Then a dummy result happens too
```

NOTE: For the Visual Studio code, you should install the plugin behave for the syntax of guerkin. Maybe, you could install "Feature Syntax Highlight and snippets(Cucumber/Guerkin)" which is better.


Now, we will need to create the steps in the folder "c:\workspace\bdd_python_base\src\features\steps\dummy_steps.py"

An now you will need to execute the following command:
```
behave
```

And you will see the code you need for your steps. Copy paste in dummy_steps.py

```python
from behave import fixture, given, then, use_fixture, when

@given(u'a dummy given')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a dummy given')


@when(u'a dummy thing happens')
def step_impl(context):
    raise NotImplementedError(u'STEP: When a dummy thing happens')


@then(u'a dummy result happens too')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a dummy result happens too')
```

Maybe you would want to change the exceptions for assert(True) for the example.

## 9. Behave plugins in Visual Studio Code
You can execute behave with "Run and Debug->BDD Execution"







