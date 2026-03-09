# Maven Calculator Project

## Overview

This project is a simple **Java Calculator application** built using **Apache Maven**.
It demonstrates a basic Maven project structure, unit testing using **JUnit**, and version control using **Git**.

This project was created as part of the **ISWE406P – Agile Development Process and DevOps Lab** assignment at **VIT Vellore**.

---

## Project Structure

```
calculator-project
│
├── pom.xml
│
└── src
    ├── main
    │   └── java
    │       └── com
    │           └── example
    │               └── Calculator.java
    │
    └── test
        └── java
            └── com
                └── example
                    └── CalculatorTest.java
```

### Description

* **pom.xml** – Maven configuration file containing dependencies and build settings.
* **Calculator.java** – Implements basic calculator operations.
* **CalculatorTest.java** – Unit tests for verifying calculator functions using JUnit.

---

## Features

The calculator supports the following operations:

* Addition
* Subtraction
* Multiplication
* Division (with divide-by-zero handling)

---

## Technologies Used

* Java
* Apache Maven
* JUnit
* Git
* Visual Studio Code

---

## How to Run

Open a terminal in the project directory and execute:

```
mvn compile
```

To run unit tests:

```
mvn test
```

To build the project:

```
mvn clean install
```

---

## Expected Output

After running the tests successfully, Maven will display:

```
BUILD SUCCESS
```

---

## Author

Student – VIT Vellore
