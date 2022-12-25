Here are some useful links for instance setup tasks. We also have 

* installing awscli
    * https://linuxhint.com/install_aws_cli_ubuntu/

* Python wheel install
    * https://stackoverflow.com/questions/65273035/how-to-fix-error-invalid-command-bdist-wheel
    
* Node
    * https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-20-04-pt

* Jupyter lab
    1. https://towardsdatascience.com/getting-the-most-out-of-jupyter-lab-9b3198f88f2d
    2. https://towardsdatascience.com/customizing-jupyter-lab-shortcuts-6857492647d2
    3. https://towardsdatascience.com/jupyter-workflow-for-data-scientists-d1ce05d67717
    
* Jupyter lab setup
Go to `Settings > Advanced settings > Keyboard Shortcuts` and add the following user settings, gotten from 2.

```
{
    "shortcuts": [
        {
            "command": "runmenu:restart-and-run-all",
            "keys": [
                "F6"
            ],
            "selector": "[data-jp-code-runner]"
        },
        {
            "command": "kernelmenu:restart-and-clear",
            "keys": [
                "F7"
            ],
            "selector": "[data-jp-kernel-user]:focus"
        },
        {
            "command": "kernelmenu:run-all-above",
            "keys": [
                "F8"
            ],
            "selector": "[data-jp-kernel-user]:focus"
        },
        {
            "command": "terminal:open",
            "keys": [
                "Alt T"
            ],
            "selector": "body"
        },
        {
            "command": "tabsmenu:activate-previously-used-tab",
            "keys": [
                "Alt ArrowUp"
            ],
            "selector": "body"
        },
        {
            "command": "application:activate-previous-tab",
            "keys": [
                "Alt ArrowLeft"
            ],
            "selector": "body"
        },
        {
            "command": "application:activate-next-tab",
            "keys": [
                "Alt ArrowRight"
            ],
            "selector": "body"
        }
    ]
}
```
