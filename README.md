# rps-starter

A Starter Repository for the [Rock Paper Scissors Exercise](https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md).

## Rock-Paper-Scissors Exercise
In this exercise you will play/compete with the computer in a game of rock, paper, scissors. 

## Purpose
The purpose of this exercise is to declare a rock, paper, scissors winner. The developer used basic Python code without a loop for continuous games. This game only plays once. 

## Prerequisites

+ ["Run the App" Exercise](https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/run-the-app/README.md)
+ Python Language Overview (focusing on [Variable](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/variables.md) and [Conditionals](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/control-flow.md)


## Setup

Checklist to steps for setup.

+ Select the green "Code" button
+ Choose the option "Open with GitHub Desktop" 
+ Clone onto your local computer

Optionally fork this [remote repository](https://github.com/hfrey1995/rock-paper-scissors), to create a copy under your own control. Then "clone" or download the remote repository (or your forked copy) onto your local computer, for example to your Desktop or C Drive (exampled). Then navigate to wherever you downloaded the repo.

```sh
cd ~Hunte@FreyPC MINGW64 /c/my-first-rep-folder/rock-paper-scissors (main)
```

Use your text editor or the command-line to create a file in that repo called "game.py"' and then place the following contents inside:

```sh
print("Rock, Paper, Scissors, Shoot!")
```

Make sure to save Python files like this whenever you're done editing them. After setting up a virtual environment, we will be ready to run this file. 

Create a virtual environment:

```sh
conda create -n rps-env python=3.8
```

Activate the virtual environment:

```sh
conda activate rps-env
```

Install package dependencies (mainly for testing):

```sh
pip install -r requirements.txt
```
## Testing

Run tests:

```sh
pytest
```

## RPS Game

```sh
python game.py
```

# Environment Setup

Create and activate a new project-specific Anaconda for the program using:

```sh
conda create -n my-game-env python=3.8 # (first time only)
conda activate my-game-env
```

Check for Anaconda installation in command-line to ensure Anaconda has been installed:

```sh
conda --version
```

If an error message populates please install [Anaconda](https://www.anaconda.com/products/distribution) to successfully play a game of rock, paper, scissors. 

## Usage

After the setup is complete, please demonstrate your ability to run the Python script from the command-line:

```sh
python game.py
```

Run the rock paper scissors game:

```sh
python game.py
```
If you see "Rock, Paper, Scissors, Shoot!" message, you are ready to move on to play the game. You will be prompted to make a selection of ("rock", "paper", or "scissors"). if you mistype or type in a different word you will be notified of an "OOPS INVALID TRY AGAIN" message. In this case please re-run the below:

```sh 
python game.py
```

Then select the approriate options of rock, paper or scissors and see if you WIN!

This is a one time game. To play multiple games please re-run the below (or press the up arrow if already played):

```sh
python game.py
```
## HAVE FUN and GOODLUCK!

## Demo

Below are examples of two invalid entries and one successful game. 

This is where I saved the rock, paper, scissors repo locally for reference:

```sh
Hunte@FreyPC MINGW64 /c/my-first-rep-folder/rock-paper-scissors (main)
```

Examples:

```sh
Hunte@FreyPC MINGW64 /
$ cd C:/my-first-rep-folder/rock-paper-scissors
(base)
Hunte@FreyPC MINGW64 /c/my-first-rep-folder/rock-paper-scissors (main)
$ python game.py
Rock, Paper, Scissors, Shoot!
Please make a selection ('rock', 'paper', 'scissors): rock
You chose:  rock
You chose: ' rock'
OOPS INVALID TRY AGAIN
(base)
Hunte@FreyPC MINGW64 /c/my-first-rep-folder/rock-paper-scissors (main)
$ python game.py
Rock, Paper, Scissors, Shoot!
Please make a selection ('rock', 'paper', 'scissors):rock
You chose: rock
You chose: 'rock'
Computer chose: scissors
Rock crushes scissors. You win!
(base)
Hunte@FreyPC MINGW64 /c/my-first-rep-folder/rock-paper-scissors (main)
$ python game.py
Rock, Paper, Scissors, Shoot!
Please make a selection ('rock', 'paper', 'scissors):Opps
You chose: opps
You chose: 'opps'
OOPS INVALID TRY AGAIN
```