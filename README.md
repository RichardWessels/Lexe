# Lexe

#### Purpose

Lexe is a simple tool that helps you store interesting words you come across. With the help of some APIs, it allows you to access the relevant definition, syllable breakdown and more of a word you're interested in. 

#### How to Run

You will need Python 3.6 (or later) installed on your system (due to the use of f-strings). 

To run the program, navigate to the program's directory via your terminal and run: `python3 main.py`

#### Note

To use this program on your own computer, you will need an API key from Merriam-Webster. To obtain such a key, visit: https://dictionaryapi.com/register/index and under "Request API Key (1)", enter: "Collegiate Dictionary". The second API key doesn't matter. 

After this process, you will be given an API key that you can add to your program by changing the following lines in `main.py`:

```python
with open("hidden_info.json") as f:
	API_KEY = json.load(f)['API_KEY']
```

to:

```python
API_KEY = "Your API Key"
```



This program is honestly just a way for me to keep track of some nice words I come across and was not created with other users in mind. I do however hope someone finds this program helpful in some way.