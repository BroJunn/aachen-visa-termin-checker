# Städteregion Aachen Ausländeramt Appointment Checker

This project is designed to check the availability of ****visa-extention/visa-application** appointments for **NON-STUDENTS** on the "Städteregion Aachen Ausländeramt" website. It automates checking for available slots and sends notifications via AWS SNS when appointments become available.

---

## Configuration Guide

In the `config.py` file, configure the following parameters to customize the script:

### **Button IDs**
To identify the correct buttons on the webpage, locate each button's ID in the HTML source code. Use these IDs to set the parameters accordingly:

- `BUTTON_ID_AUFFENHALT` — ID for the "Aufenthalt" section. Example: `"header_concerns_accordion-456"`
- `BUTTON_ID_TEAM1` — ID for Team 1's appointment button. Example: `"button-plus-293"`
- `BUTTON_ID_TEAM2` — ID for Team 2's appointment button. Example: `"button-plus-296"`
- `BUTTON_ID_TEAM3` — ID for Team 3's appointment button. Example: `"button-plus-297"`

### **AWS SNS Keys**
Provide AWS credentials and settings to enable SMS notifications when appointments are found.

- `AWS_ACCESS_KEY_ID` — Your AWS access key.
- `AWS_SECRET_ACCESS_KEY` — Your AWS secret access key.
- `REGION_NAME` — AWS region. Example: `"eu-north-1"`
- `PHONE_NUMBER` — The phone number to receive notifications, formatted with the country code (e.g., `"+49 123456789"`).

### **Check Interval**
Set the interval (in seconds) for how frequently the script should check for appointments. **Note:** Keep this value reasonable to avoid triggering anti-scraping mechanisms.

- `CHECK_INTERVAL` — Example: `60`

---

## Running the Script

1. Install dependencies:
    ```bash
    conda create -n visaTerminBuchen python=3.9 -y
    conda activate visaTerminBuchen
    pip install -r requirements.txt
    ```

2. Run the script:
    ```bash
    python main.py
    ```
