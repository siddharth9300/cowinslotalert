

# Automate Your COVID-19 Vaccine Slot Alerts with Cowin Slot Alert

## Introduction

The COVID-19 pandemic brought a surge in demand for vaccinations, making the availability of slots a critical concern. Cowin Slot Alert is a Python project that automates the process of searching for open vaccination slots and notifies users through a Telegram group. This blog dives into how the project works, the technology behind it, and how you can use or extend it for your needs.

---

## What Problem Does It Solve?

Booking a vaccination slot on the CoWIN platform in India was often a race against time—slots would appear and disappear within minutes. Constantly refreshing the website was tedious and inefficient. Cowin Slot Alert solves this by monitoring the CoWIN API for available slots in specified areas and instantly sending alerts to a Telegram group, helping users secure a booking as soon as a slot opens up.

---

## How Does Cowin Slot Alert Work?

### 1. Core Workflow

- **Periodically Check CoWIN API:**  
  The script uses the official public CoWIN API to fetch vaccination session data for specific pincodes or districts.
- **Parse Availability:**  
  It inspects the response for sessions where slots are available (especially for Dose 1 and for the 18+ age group).
- **Send Telegram Alert:**  
  When available slots are found, the script sends a formatted message to a predefined Telegram group using the Telegram Bot API.
- **Repeat:**  
  The process runs in an infinite loop, checking for new slots at regular intervals.

### 2. Key Components in the Code

- **API Integration:**  
  The script constructs requests to the CoWIN API endpoint for calendarByPin, providing pincodes and the current date.
- **Response Parsing:**  
  For each vaccination center and its sessions, it checks if the slot meets the criteria (like age limit and available capacity).
- **Notification:**  
  An alert message is formatted with all the relevant details (center name, address, pin, age limit, vaccine type, slots available, doses, and a booking link).
- **Telegram Bot:**  
  Using a bot token and group ID, the script sends the notification via Telegram’s HTTP API.

### 3. Tech Stack

- **Python 3.9.5**
- **requests** – For HTTP requests to the CoWIN and Telegram APIs.
- **DateTime** – For date formatting and manipulation.
- **Heroku Compatibility:**  
  Includes a `Procfile` and `runtime.txt` for easy deployment on Heroku.

---

## Example Message Sent to Telegram

```bash

Name: [Center Name]
Address: [Center Address]
Pin: [Pin Code]
Minimum Age: [18 or 45]
Vaccine: [Covishield, Covaxin, etc.]
Slots: [List of available slots]
Total [N] slots are available on [Date]
Dose 1 Available: [Number]
Dose 2 Available: [Number]
COWIN: https://selfregistration.cowin.gov.in/
```

---

## How To Deploy and Run

1. **Clone the Repository**
2. **Install Requirements**
   ```bash
   pip install -r requirements.txt
   ```
3. **Edit the Configuration**
   - Update the `group_id` and `api_url_telegram` with your Telegram bot and group details.
   - Set your preferred pincodes in `pincode_near`.
4. **Run the Script**
   ```bash
   python final.py
   ```
   Or, deploy to Heroku using the provided `Procfile`.

---

## Who Can Use This?

- Individuals looking for COVID-19 vaccination slots for themselves or family.
- Community admins who want to broadcast slot availability to a group.
- Developers who want to extend the script for other notification channels.

---

## Potential Improvements

- Customizable notification intervals.
- Support for district-wise search.
- Web interface for configuration.
- Rate-limiting and error handling improvements.

---

## Conclusion

Cowin Slot Alert is a practical, real-world automation tool that helped countless people secure vaccination slots during the pandemic. Its open-source approach means anyone can use, adapt, or contribute to making vaccine access smoother and fairer.

Check out the code, contribute, and never miss a slot again!

---
