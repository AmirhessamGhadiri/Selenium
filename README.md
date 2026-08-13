# usBIM Angle Snapshot Automation

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/selenium-4.x-green.svg)](https://www.selenium.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An automated Python script using **Selenium** to capture multi-angle snapshots of 3D BIM objects uploaded to the **usBIM online model viewer**.

---

## Overview

Automating image acquisition for 3D Building Information Modeling (BIM) components can be tedious. This project automates the process of opening an uploaded model in the usBIM viewer, rotating the object to specified camera angles, and taking consistent high-quality snapshots automatically.

### Key Features
* **Automated Interaction:** Logs in and loads models directly in the usBIM viewer.
* **Customizable Angles:** Easily configure the number of snapshots and precise camera orientations.
* **Batch Processing:** Reduces manual effort required for generating visual datasets or reports.

---

## Prerequisites

Before running the script, make sure you have:
* Python 3.8 or higher installed
* Google Chrome (or your preferred web browser) installed
* A registered account on [usBIM](https://www.usbim.com/)

---

## Getting Started

### 1. Clone the Repository
`git clone https://github.com/AmirhessamGhadiri/Selenium.git`  
`cd Selenium`

### 2. Set Up a Virtual Environment & Install Dependencies
`python -m venv venv`  
`source venv/bin/activate`  *(On Windows use: `venv\Scripts\activate`)*  
`pip install -r requirements.txt`

### 3. Environment Configuration
To keep your credentials secure, create a `.env` file in the root directory:

USBIM_EMAIL=your_email@example.com  
USBIM_PASSWORD=your_secure_password  

---

## Usage

1. Upload your target 3D model file to your usBIM account.
2. Update the target model URL or parameters in `selenium.py` if needed.
3. Run the automation script:

`python selenium.py`

The script will automatically execute, capture the designated angles, and save the resulting images to your local directory.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
