# Automated Web Form Submission with Selenium

## Overview

This project automates the process of filling and submitting a web form using **Python** and **Selenium**. The script reads user data from a CSV file and automatically enters it into a web form, reducing manual effort and demonstrating browser automation.

## Features

* Reads data from a CSV file
* Automatically fills text fields
* Selects radio buttons
* Chooses values from a dropdown menu
* Handles checkboxes
* Submits the form for each record
* Logs successful submissions and errors

## Project Structure

```text
Automated-Web-Form/
│── form.html
│── form_automation.py
│── data.csv
│── requirements.txt
│── submission.log
```

## Installation

1. Clone the repository.
2. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

Run the script with:

```bash
python form_automation.py
```

The script will open the local web form, read data from `data.csv`, submit each record automatically, and save the results in `submission.log`.

## Technologies Used

* Python
* Selenium
* WebDriver Manager
* CSV Module
* Logging Module
