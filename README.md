# Object Oriented Programming Lab - Bookstore 

This scenario should encompass all of the topics provided in the module. Now that you’ve delved into creating a new class in Python it is now time to practice this concept.

## Instructions

### Set Up

Before we begin coding, let's complete the initial setup for this lesson: 

* Part 1: Fork and Clone- For this lesson, you will need the previously linked GitHub Repo:
  * Go to the provided GitHub repository link.
  * Fork the repository to your GitHub account.
  * Clone the forked repository to your local machine.
* Part 2: Open and Run File
  * Open the project in VSCode.
  * Run `pipenv install` to install all necessary dependencies.
  * Run `pipenv shell` to enter the virtual environment.

This lab is test-driven. You will write your code in `lib/book.py` and
`lib/coffee.py`. Run the tests and work your way through the test errors one by
one until you get everything passing.

You're also encouraged to look at the test files to see what the tests are
expecting to be able to do with your classes. These tests won't force you to
use everything that you've learned in this module- feel free to add any
features that might be useful!

Note that there are separate test files for the two classes inside the `testing`
folder. If you'd like to run the tests separately for the two classes, you can
specify which test file to run:

```console
$ pytest -x testing/book_test.py
```

or:

```console
$ pytest -x testing/coffee_test.py
```

Remember that the optional `-x` flag makes your tests stop after the first
failure - this setting is ideal for test-driven development!

### Task 1: Define the Problem

Build a model for a book and a coffee
<br />
As a user, one should be able to:
* Build a book object
* Build a coffee object
* Call to turn a book page
* Call to tip for the coffee

### Task 2: Determine the Design

Book
* Attributes:
  * title
  * page_Count
* Methods:
  * turn_page()
Coffee
* Attributes:
  * size
  * price
* Methods:
  * tip()

### Task 3: Develop, Test, and Refine the Code

#### Step 1: Feature Branch and Book Class

* Create Feature Branch

* Create Book class:
  * __init__:
    * title
      * Require user to input
    * page_count
      * Require user to input
* Properties:
  * page_count:
    * Ensure it is an integer
    * if not print “page_count must be an integer”
* Methods:
  * turn_page():
    * Will print “Flipping the page...wow, you read fast!”

#### Step 2: Create Coffee Class & Push Feature Branch and Merge

* __init__:
  * size
    * Require user to input
  * price
    * Require user to input
* Properties:
  * Size
    * Ensure size is either Small, Medium, or Large
    * If not print “size must be Small, Medium, or Large”
* Methods:
  * tip():
    * Will print “This coffee is great, here’s a tip!”
    * Will increase price by 1 
