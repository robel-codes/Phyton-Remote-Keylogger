# Phyton-Remote-Keylogger

**Disclaimer:** This project is intended solely for educational purposes. It should not be used for any malicious activities. Use responsibly and ensure compliance with legal and ethical standards. Unauthorized access to or monitoring of computer systems is illegal and unethical.

## Overview

This project creates a remote keylogger that captures keystrokes and screenshots from a user’s machine and sends this data to a remote server hosted on Replit. The server displays the keystrokes and screenshots in a web interface.

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Required Libraries
- **pynput**: Library for capturing keyboard events.
- **mss**: Library for capturing screenshots.
- **pillow**: Library for image processing.
- **requests**: Library for sending HTTP requests.
- **Flask**: Web framework for creating the server.

To install the required libraries, run the following command:

```bash
pip install -r requirements.txt
```

### Additional Tools
- **Nuitka**: Python compiler for creating standalone executables. (requires windows visual studio build tools)
```bash
pip install nuitka
```

## Project Setup

### Keylogger Script
- **Capture Keystrokes**: Uses `pynput` to listen for and log keystrokes.
- **Capture Screenshots**: Uses `mss` to take screenshots at regular intervals.
- **Send Data**: Sends keystrokes and screenshots to the Flask server using `requests`.

### Flask Server
- **Install Flask**: Install Flask on your remote server ```pip install Flask```
- **Setup Server**: Handles incoming POST requests at `/keystrokes` and `/screenshots`.
- **Data Storage**: Saves received screenshots in the `static` folder and displays them on the `index.html` page.
- **Display Data**: Shows captured keystrokes and screenshots with timestamps.

## Replit Configuration
- **Create Replit Account**: Sign up at [Replit](https://replit.com).
- **New Project**: Create a new Python project.
- **Add Flask Code**: Implement the Flask server code and create `index.html` in the `templates` folder.
- 


## Usage

### Compile Keylogger Script:
- Add you remote server ur inside the python script line #10
- Complile the keylogger script using Nuitka into standalone excutable. Example command:

```bash
py -m nuitka --mingw64 '<ScriptName>' --standalone --onefile --output-filename=<outputFile.exe>
```
### Run Keylogger executable: 
- You can check Task manager to see the keylogger is running in the background

## License
This project is for educational purposes only. Use responsibly and ensure compliance with legal and ethical standards.

## Resources
- [David Bombal Youtube](https://www.youtube.com/watch?v=LBM3EzBXhdY)
- **Replit**: For providing a platform to host the Flask server.
- **Python Libraries**: For their contributions to the development of the keylogger and server.
- **Nuitka Documentation**: For guidance in setting up the web server.



