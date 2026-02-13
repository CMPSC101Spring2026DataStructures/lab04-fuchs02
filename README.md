[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/KqaKW0-E)
# CS101 Spring 2026: Lab 04

## Assignment: Build Your Own Game of *Rock, Paper, Scissors*!

Welcome to your programming assignment for CS101! In this lab, you will complete a Rock Paper Scissors game by filling in the missing parts of the provided `main.py` file.

## Assigned and Due

* __Assigned__: Friday, 13 Feb 2026 at 2:35pm
* __Due__:  Friday, 20 Feb 2026 at 2:35pm
* __Expiration__: Friday, 27 Feb 2026 at 2:35pm
Note: the *expiration* date is the last date you can submit your work for a grade.

![rock_paper_scissors logo](graphics/rock_paper_scissors.png)

## Table of Contents
- [CS101 Spring 2026: Lab 04](#cs101-spring-2026-lab-04)
  - [Assignment: Build Your Own Game of *Rock, Paper, Scissors*!](#assignment-build-your-own-game-of-rock-paper-scissors)
  - [Assigned and Due](#assigned-and-due)
  - [Table of Contents](#table-of-contents)
  - [Project Goals](#project-goals)
  - [Project Overview](#project-overview)
    - [Refactor and Rewrite the Source Code](#refactor-and-rewrite-the-source-code)
  - [Project Access](#project-access)
    - [Two Source Code Files](#two-source-code-files)
  - [Setup Instructions](#setup-instructions)
  - [UV Package Manager Setup and Usage](#uv-package-manager-setup-and-usage)
    - [Step 1: Install UV](#step-1-install-uv)
    - [Step 2: Initialize the Project and Install Dependencies](#step-2-initialize-the-project-and-install-dependencies)
    - [Step 3: Run the Spaghetti Code Example](#step-3-run-the-spaghetti-code-example)
    - [Step 4: Work on Your Refactored Code](#step-4-work-on-your-refactored-code)
    - [Step 5: Test Your Refactored Code](#step-5-test-your-refactored-code)
    - [Troubleshooting](#troubleshooting)
  - [Ideas for Extension](#ideas-for-extension)
  - [Deliverable](#deliverable)
  - [Submission](#submission)
  - [Project Assessment](#project-assessment)
  - [GatorGrade](#gatorgrade)
    - [Checks for GatorGrade](#checks-for-gatorgrade)
  - [Seeking Assistance](#seeking-assistance)


You are invited to complete a game of Rock, Paper, Scissors using UV, an editor and terminal commands. The rules of the game may be found at [https://en.wikipedia.org/wiki/Rock_paper_scissors](https://en.wikipedia.org/wiki/Rock_paper_scissors).

## Project Goals

* To practice breaking a program into functions to improve its structure and maintainability.
* To practice writing documentation and comments to help users understand how the code works.
* To gain experience in using UV to manage a Python project.

## Project Overview

While browsing GitHub, you come across an open source project of the famous, `Rock, Paper, Scissors`, game. You are immediately interested in playing this old favorite game, and so you clone the project. As you look at the code, you notice that has been written in a hurry because the code is so messy. Source code like this is often called `spaghetti code`.

For instance, the scripting does not seem to have much structure to help maintain its internal methods, there are few functions to break-up the work into manageable parts, and there is little documentation to assist users in understanding how the program works. In addition, there are some parts of the code are just *seemingly* impossible to understand!

This lab assignment invites you to rewrite this spaghetti code to prepare a carefully crafted piece of structured software. To rewrite it, you are to add functions and documentation to help its users to comprehend, use and maintain the code.

### Refactor and Rewrite the Source Code

Refactoring code means to break the code into smaller pieces (e.g., functions) and to add comments and documentation to help the user to understand how the code works. This is a very important skill for any programmer as it helps to make the code more maintainable and easier to understand. You are now ready to rewrite the source code using the original code that is provided to you in your working repository.

__Note__: you can run the `main_spaghetti_code.py` file to see how the game should work, but do not simply copy and paste its code directly into your restructured project! Instead, use the given code as a guide to help you implement the required functionality in `main.py` such as adding comments, docstrings, and functions to make the code more *readable* for comprehension and maintenance.

## Project Access

Once you gave accepted this assignment by clicking the **GitHub Classroom** link provided to you in **Materials** lab of the main website for the course [https://cmpsc101fall2025datastructures.github.io/site/](https://cmpsc101fall2025datastructures.github.io/site/), you are to clone the repository to your computer where you are to work. The clone command is the following; `git clone <your-github-repository`.

### Two Source Code Files

There are two course codes to use in this lab; `main.py` and `main_spaghetti_code.py`. The `main.py` file is the one that you will be working on to complete the assignment. The `main_spaghetti_code.py` file is provided as a reference if you get stuck or want to check your work.

![--- --- --- --- --- --- --- --- ---](graphics/div_bar.png)

## Setup Instructions

1. __Setup your Python environment using UV__

   * Clone your working repository to your computer if you have not already done so.
   * Start up your Python environment using UV as described in the [UV Package Manager Setup and Usage](#uv-package-manager-setup-and-usage) section below.
   * UV documentation available at [https://docs.astral.sh/uv/guides/projects/#creating-a-new-project](https://docs.astral.sh/uv/guides/projects/#creating-a-new-project).

2. __Open `main.py` On Your Own Machine__

   * You will see several functions with `TO-DO` comments. Your job is to complete these functions so the game works as described (e.g., will run to play a game of *Rock Paper Scissors*).
   * Please remove the `TO-DO` comments as you finish each part.

3. __Refactor the Code by Implementing Functions with Documentation__

   * Each function to complete has already been added to the code in `main.py` and should have a docstring and comments as needed. The  `TO-DO` tags guide the user to implement the following functionalities.

   * Please be sure that your program implements the following features:
     * The user can enter their choice (`rock`, `paper`, or `scissors`, or `1`, `2` or `3`, respectively).
     * The computer randomly selects its moves.
     * The winner of each round is determined and displayed with colorful output.
     * Scores are tracked and the overall winner is announced at the end.

   * As you write your refactored code, please be sure to add meaningful **comments** and enriched **doc strings** to help your *Future Self* understand what the code is doing.

4. __Test Your Program__

   * First, run the spaghetti code example to see how the game should work:

    ```sh
    uv run main_spaghetti_code.py
    ```

   * Then, as you work on your refactored code, test it regularly using:

    ```sh
    uv run main.py
    ```

   * Make sure it works for all valid and invalid inputs, and that the output is colorful and friendly!

The proper output should look something like the following.

``` bash
$ uv run main_spaghetti_code.py

Welcome to Rock, Paper, Scissors!
You can type 'rock', 'paper', 'scissors' or use 1 for rock, 2 for paper, 3 for scissors.

Round 1 of 3
Choose rock (1), paper (2), or scissors (3): 1
Computer chose: scissors
You win this round!

Round 2 of 3
Choose rock (1), paper (2), or scissors (3): 3
Computer chose: rock
Computer wins this round!

Round 3 of 3
Choose rock (1), paper (2), or scissors (3): 2
Computer chose: paper
It's a tie!

Game Over!
Your score: 1
Computer score: 1
It's a tie game!
```

5. __Submit Your Work__

   * Save your changes to `main.py` and ensure everything is working correctly.
   * Make your commits as you work. You are expected to have multiple commits showing your progress which will be checked by GatorGrade. These multiple commits are to help you build good programming habits.

![--- --- --- --- --- --- --- --- ---](graphics/div_bar.png)

## UV Package Manager Setup and Usage

This section describes how to set up and run the Rock Paper Scissors game for this lab using UV, a modern Python package manager. The game demonstrates basic Python concepts and features enhanced command-line interaction and colorful output using the `rich` library.

### Step 1: Install UV

First, you need to install UV on your system if you have not already. Choose the method appropriate for your operating system:

**macOS and Linux:**

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**

```sh
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Alternative (any platform with Python/pip):**

```sh
pip install uv
```

**Verify installation:**

To be sure that your installation worked.

```sh
uv --version
```

For more installation options, see the [official UV documentation](https://docs.astral.sh/uv/getting-started/installation/).

### Step 2: Initialize the Project and Install Dependencies

Initiate your virtual environment inside your project. Note: you should be able to see the source code files of the current project when you type `ls -l` (Windows: `dir`).

```sh
uv init
```

This command will create the File `pyproject.toml`.

Next, you can install the required dependencies:

```sh
uv add rich
```

This command will:

- Create a virtual environment automatically (if not already present)
- Add the `rich` library to your project dependencies
- Update or create `pyproject.toml` and `uv.lock` files

### Step 3: Run the Spaghetti Code Example

Before you start refactoring, run the original spaghetti code to see how the game should work:

```sh
uv run main_spaghetti_code.py
```

Play a few rounds to understand the game mechanics, the input options, and the expected output format. Pay attention to:

- How the game prompts for input
- How it handles both text (`rock`, `paper`, `scissors`) and numeric (`1`, `2`, `3`) inputs
- The colorful output using the `rich` library
- How scores are tracked and displayed

### Step 4: Work on Your Refactored Code

Now open `main.py` in your editor and complete the `TO-DO` items. As you work:

1. Break the code into functions
2. Add docstrings to each function
3. Add (meaningful) comments to explain complex logic. Remember Future-You will have questions about how and why your code works as it does!
4. Follow the structure outlined in the starter code

### Step 5: Test Your Refactored Code

Before you submit your finalized code, run your refactored code a few last times to ensure that all is as expected. Does its execution mirror that of the original spaghetti code?

```sh
uv run main.py
```

Test thoroughly:

- Try valid inputs: `rock`, `paper`, `scissors`, `1`, `2`, `3`
- Try invalid inputs to ensure error handling works
- Play multiple rounds to verify scoring works correctly
- Confirm the output matches the expected format

![--- --- --- --- --- --- --- --- ---](graphics/div_bar.png)

### Troubleshooting

If you encounter issues:

**Command not found errors:**
- Ensure UV is properly installed and in your PATH
- Try closing and reopening your terminal

**Module import errors:**
- Run `uv add rich` again to ensure dependencies are installed
- Verify you're using `uv run` to execute your scripts (this ensures the virtual environment is used)

**Permission errors (macOS/Linux):**
- You may need to run `chmod +x main.py` to make the script executable

![--- --- --- --- --- --- --- --- ---](graphics/div_bar.png)

## Ideas for Extension

If you are looking for an **extra challenge**, consider implementing one or more of the following features:

* Add a score history or leaderboard.
* Allow the user to play unlimited rounds until they choose to quit.
* Add ASCII art for each move.
* Let the user play against another human.
* Add sound effects (using a cross-platform library).
* Track and display statistics (win/loss/tie percentages).
* Implement a "best of N" mode.

![--- --- --- --- --- --- --- --- ---](graphics/div_bar.png)

## Deliverable

Once you have completed your work on the code, you are to submit the code along with your completed writing assessment at `writing/reflection.md`.

Writing assignment: [Reflections](writing/reflection.md)

Note: As you work, please periodically commit your changes and push them to your GitHub repository. This will ensure that your work is saved and can be reviewed by your instructor.

![--- --- --- --- --- --- --- --- ---](graphics/div_bar.png)

## Submission

As you are working on your lab, you are to commit and push regularly. The commands are the following.

 ``` bash
git add -A
git commit -m ``Your notes about commit here''
git push
```

After you have pushed your work to your repository, please visit the repository at the GitHub website (you may have to log-in using your browser) to verify that your files were correctly sent.

![--- --- --- --- --- --- --- --- ---](graphics/div_bar.png)

## Project Assessment

The grade that a student receives on this assignment will have the following components.

* **GitHub Actions CI Build Status [up to 10%]:**: For the lab repository associated with this assignment students will receive a checkmark grade if their last before-the-deadline build passes. This is only checking some baseline writing and commit requirements as well as correct running of the program. An additional reduction will given if the commit log shows a cluster of commits at the end clearly used just to pass this requirement. An addition reduction will also be given if there is no commit during lab work times. All other requirements are evaluated manually.

* **Mastery of Technical Writing [up to 50%]:**: Students will also receive a checkmark grade when the responses to the writing questions presented in the `reflection.md` reveal a proficiency of both writing skills and technical knowledge. To receive a checkmark grade, the submitted writing should have correct spelling, grammar, and punctuation in addition to following the rules of Markdown and providing conceptually and technically accurate answers.

* **Mastery of Technical Knowledge and Skills [up to 40%]**: Students will receive a portion of their assignment grade when their program implementation reveals that they have mastered all of the technical knowledge and skills developed during the completion of this assignment. As a part of this grade, the instructor will assess aspects of the programming including, but not limited to, the completeness and the correctness of the program and the use of effective source code comments.

![--- --- --- --- --- --- --- --- ---](graphics/div_bar.png)

## GatorGrade

### Checks for GatorGrade

For immediate feedback on submissions, we will be using Gator Grade to inform the of missing components in the submission. As you submit, you will notice that there is a thick red X that will change to a green check mark when all components have been included in the submission. You are encouraged to click on the red X to find a listing of the components to address.

You can check the baseline writing and commit requirements for this lab assignment by running department's assignment checking `gatorgrade` tool. To use `gatorgrade`, you first need to make sure you have Python3 installed (type `python --version` to check). If you do not have Python installed, please see:

- [Setting Up Python on Windows](https://realpython.com/lessons/python-windows-setup/)
- [Python 3 Installation and Setup Guide](https://realpython.com/installing-python/)
- [How to Install Python 3 and Set Up a Local Programming Environment on Windows 10](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-windows-10)

Then, if you have not done so already, you need to install `gatorgrade`:

- First, [install `pipx`](https://pypa.github.io/pipx/installation/)
- Then, install `gatorgrade` with `pipx install gatorgrade`

Finally, you can run `gatorgrade`: `gatorgrade --config config/gatorgrade.yml`

## Seeking Assistance

* Extra resources for using markdown include;
  + [Markdown Tidbits](https://www.youtube.com/watch?v=cdJEUAy5IyA)
  + [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
* Do not forget to use the above git commands to push your work to the cloud for the instructor to grade your assignment. You can go to your GitHub repository using your browser to verify that your files have been submitted. Please see the TL’s or the instructor if you have any questions about assignment submission.

Students who have questions about this project outside of the lab time are invited to ask them in the course's Discord channel or during instructor's or TL's office hours.

---
For questions or suggestions about the game, please contact the course instructor.
