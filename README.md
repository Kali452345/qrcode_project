# QR Code Project

This is the **qrcode_project**, a web-based application designed to generate QR codes. The project leverages HTML for the frontend, Python for backend logic, and includes Docker support for containerized deployment.

---

## Project Overview

**Purpose:**  
The aim of this project is to provide an easy-to-use tool for generating QR codes. Users can input their desired data and receive a QR code image as output.

**Main Features:**
- Web-based interface for inputting data
- Real-time QR code generation
- Downloadable QR code images
- Additional pdftoword and wordtopdf converter
- Dockerfile in linux branch for easy deployment

---

## Setup Instructions
LINUX(linux branch):

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Kali452345/qrcode_project.git
   cd qrcode_project
   ```

2. **(Optional for building on linux web servers) Run with Docker:**
   ```bash
   docker build -t qrcode_project .
   docker run -p 8000:8000 qrcode_project
   ```

3. **Manual Python Setup:**
   - Ensure you have Python 3 installed.
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Run the application:
     ```bash
     python main.py
     ```
   - Open your browser at `http://localhost:8000` (or specified port).

---
Windows MAIN BRANCH 

## Usage

- Enter the text or URL you want to encode.
- Click the "Generate" button.
- Download or use the generated QR code image.

---

## Project Details

- **Frontend:** HTML
- **Backend:** Python
- **Containerization:** Dockerfile included

---

## Group/Project Slots

| Slot            | Value                |
|-----------------|---------------------|
| Group Name      |      High Devs      |
| Group Member 1  |                     |
| Group member 2  |                     |
| Group Member 3  |                     |
| Group Member 4  |                     |
| Group Member 5  |                     |



---

> **Repository:** [qrcode_project](https://github.com/Kali452345/qrcode_project)
