# Caffeine-Shot

This is a simple python script written to move the mouse cursor.

### Prerequisites
homebrew,
python3,
pyautogui,
xcode,
terminal enabled accessibility rights
### Getting Started

1. Clone the repository.
```bash
git clone https://github.com/aaronlamtran/caffeine-shot.git
```
2. Navigate into the directory.
3. To create a virtual enviromment, run:
``` bash
python -m venv <your env name here>
```

4. To activate the virtual environment, run:
``` bash
source <your env name here>/bin/activate
```

5. Install dependencies.
````bash
pip3 install -r requirements.txt
````
6. Run the script
```bash
make coffee
```

7. To be able to run this script globally, make an alias in your .zshrc or .bashrc file.
```Language
alias order-coffee=cd <path to repo> && make coffee
```

You will then be able to enter the alias into your terminal to run the script
```Terminal
order-coffee
```
