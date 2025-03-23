
# Hybrid Keylogger Detection System



##  Overview
The *Hybrid Keylogger Detection System* is an AI-powered tool designed to detect and prevent keylogger attacks in real-time. It combines *behavioral analysis* and *machine learning* to identify suspicious activity, ensuring data security and privacy. This system is crucial for protecting sensitive information from malicious keylogging software.

##  Tech Stack
The project is built using the following tools and technologies:
- *Programming Languages & Libraries*: Python, Pandas, NumPy, Scikit-learn, Joblib.
- *Keystroke Logging & System Monitoring*: Pynput, Psutil.
- *User Interface*: Tkinter.
- *Data Visualization*: Matplotlib.


##  Installation
Follow these steps to set up the project locally:

1. *Clone the repository*:
   ```bash
   git clone https://github.com/ananya-thakur25/keyEagle.git

2. *Install dependencies:*:
   ```bash
   pip install -r requirements.txt

## Usage

Here’s how to use the Hybrid Keylogger Detection System:

1. *Collect Keystroke Data:*
Run the following script to collect keystroke data for analysis:
    
    python3 scripts/collect_keystrokes.py
    
2. *Train the Model:*
Train the machine learning model using the collected data:
    
    python3 scripts/train_model.py
3. *Run the Detection System:*
Launch the user interface to start detecting keylogger activity:
    

    python3 scripts/ui_tkinter.py


##  Future Enhancements

Planned improvements for the project include:

- Add network activity monitoring.
- Develop a mobile version for Android and iOS.
- Integrate cloud-based logging and alerts.
- Improve the accuracy of the machine learning model.


