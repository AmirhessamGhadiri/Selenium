# usBIM Angle Snapshot Automation

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/selenium-4.x-green.svg)](https://www.selenium.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An automated Python script using **Selenium** to capture multi-angle snapshots of 3D BIM objects uploaded to the **usBIM online model viewer**.

---

## Overview

Automating image acquisition for 3D Building Information Modeling (BIM) components can be tedious. This project automates the process of opening a uploaded model in the usBIM viewer, rotating the object to specified camera angles, and taking consistent high-quality snapshots automatically.

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
```bash
git clone [https://github.com/AmirhessamGhadiri/Selenium.git](https://github.com/AmirhessamGhadiri/Selenium.git)
cd Selenium
