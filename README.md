# VITYarthi-project
Simple Encrypted Password Manager in Python: This project is a console based Password Manager application written in Python. It enables users to securely store, retrieve, and manage their passwords for various accounts by using a simple symbol substitution encryption method.

# Password Manager System

# Project title
- Simple Password Manager System (console-based)

# Overview of the project
- A small console application to store and retrieve account passwords using a lightweight letter-mapping "encryption".
- The repository contains the original single-file script (unchanged) and a modular split version (src/).

# Features
- Set and confirm a master password.
- Add account passwords (optionally generate random passwords).
- Store encrypted passwords in memory for the running session.
- Retrieve encrypted passwords and optionally decrypt them for viewing.

# Technologies/tools used
- Python 3 (standard library only)
- Modules used: random, string

# Steps to install & run the project
1. Clone the repository:
   - git clone https://github.com/<owner>/<repo>.git
2. Option A — Run the original (unchanged) script:
   - python3 src/password_manager_original.py
3. Option B — Run the modular version:
   - python3 run.py

# Instructions for testing
- Start the program, set a master password when prompted.
- Try adding a password (generate a random one or provide your own).
- Retrieve the password and choose to decrypt it.
- Try invalid inputs (e.g., non-existent account) and menu choices.

# Notes / Limitations
- Passwords are stored only in-memory (no persistence to disk). If you exit the program, stored passwords are lost.
- The encryption is a simple character substitution for demonstration and is NOT secure for production.
- Master password is kept in-memory in plain text for the session.

Screenshots
- Console run screenshot included below.

![Console screenshot](assets/screenshot.png)
