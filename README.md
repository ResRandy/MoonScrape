# MoonScrape

## About
This is a python program that is used to collect moon data at certain dates in certain locations. This is meant to do so with large excel files, CVS or Docs.

### Structure

- `/src`: Holds Python files

## Required packages

- `pandas`
- `tkinter`
- `selenium`


# Setting up the program
You will need a python version newer than 3.6. This project was altered in python 3.12

### Installing and running the program through windows VS code
If you are using a Windows system, open up the command prompt (seach cmd in the serach bar). Start by cloning this repository by running `git clone https://github.com/ResRandy/MoonScrape`.

1. install Python
2. Go to VScode
3. Navigate to the MoonScrape directory
4. (optional) create an environment with `python -m venv .venv` and run `.venv\Scripts\activate` to activate the environment
5. run `pip install pandas tk selenium` to install modules or `.venv\Scripts\pip install pandas tk selenium` if you are using a vscode environment.
6. run the program with `.venv\Scripts\python.exe src\moon_scrape_app.py`

### Packaging the program into one excecutible
You can use `pyinstaller`

1. run `pip install pyinstaller`
2. run `pyinstaller --onefile src\moon_scrape_app.py`

## Known issues
The program isn't 100% accurate when scraping the data. The idea was that you would have to rerun the program multiple times to ensure accurate data. This can be changed later on.
