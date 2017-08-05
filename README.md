# stenocomplete

Inspired by [StenoTray](https://github.com/brentn/StenoTray), stenocomplete provides stroke suggestions based on the currently typed letters.

Some feature are:

* Logging typed/stroked letters directly instead of reading the plover logs
    * Allows to type words on a QWERTY keyboard while plover is listening to a different protocol such as TX Bolt (for example when using the [Stenomod](https://stenomod.blogspot.com/))
    * Allows the detection of non-alphabetical characters such as space and backspace
    * Plover logging does not have to be activated
* Output is displayed in the terminal
    * Follows the font and color configuration of your system
    * Uses few resources
* Handles dictionary entries that contain multiple words such as `New York City`
* Handles backspace keys for the current word or phrase
* Allows the lookup of commands such as `#Control_L(c)` by typing `#C`
* Written in Python 3
    * Python 3 is installed on your computer if you're running Plover
    * Makes a future integration as a Plover plugin easier


## Installation

### Linux

Stenocomplete uses the Python library [marisa-trie](http://marisa-trie.readthedocs.io/en/latest/) to allow a fast word completion.

A popular program for installing python libraries is `pip`.
The following command is used to install pip for Python 3 on Ubuntu:
```bash
sudo apt-get install python3-pip
```

To install `marisa-trie`, use:
```bash
pip3 install --user marisa_trie
```


Further, the code relies on `python-xlib` for logging the keys.
Chances are that you already have it installed if you're using Plover. If the following command does not throw a `ModuleNotFoundError`, you're good to go:
```bash
echo "import Xlib" | python3  
```

If you don't have `python-xlib` installed, you can use pip:
```bash
pip3 install --user python-xlib
```


Finally, download and unzip the content of this repository: <https://github.com/mkrnr/stenocomplete/archive/master.zip>

### Windows

Windows is currently not supported. 

### macOS

MacOS is currently not supported.


## Usage

Currently, the only information that is provided to the [`main.py`](stenocomplete/main.py) class is a list of paths to the dictionaries that should be loaded.
Additional options such as the simplification of strokes are planned.

To run stenocomplete, open a terminal and execute [`stenocomplete/main.py`](stenocomplete/main.py) with the dictionaries that should be loaded. For example:
```bash
python3 path/to/stenocomplete/main.py ~/.local/share/plover/*.json
```

If you want to prioritize a dictionary, put it at the end of the list.

## Known Issues

Please let me know if you have any issues!
