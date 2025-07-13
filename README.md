# capstone-anpr
# 🚗 Automatic Number Plate Recognition (ANPR)

A simple and cost-effective Automatic Number Plate Recognition (ANPR) system using **OpenCV** and **EasyOCR**, designed especially for **local households, shops, and small societies** to enhance security and automate vehicle monitoring.

---

## 📌 Project Overview

This project enables users to detect, extract, and recognize vehicle number plates from a **live video feed** and store them for security or analysis purposes. It aims to reduce manual surveillance and support faster vehicle identification in case of theft, hit-and-run, or suspicious activities.

---

## 🎯 Objective

To develop a lightweight ANPR system that:
- Captures live video feed from camera/CCTV.
- Detects and extracts number plates using OpenCV.
- Recognizes text using EasyOCR.
- Logs detected vehicle numbers with timestamps.
- Enables easy deployment in **homes, roadside shops, and housing societies**.

---

## 🛠️ Technologies Used

- **Python**
- **OpenCV** – Video processing and plate detection.
- **EasyOCR** – Text recognition from number plates.
- **Regex** – Format validation of license numbers.
- **CSV / Pandas** – Data storage and logging.

---

## 🔄 Workflow

1. **Live video capture** from webcam or IP camera.
2. **Frame preprocessing** for noise reduction.
3. **Number plate detection** using contours.
4. **Plate region extraction**.
5. **Text recognition** via EasyOCR.
6. **Regex validation** to match number plate format.
7. **Data logging** with date and time.

---

## ✅ Key Features

- Real-time number plate detection and recognition.
- Designed to work on Indian license plate formats.
- Low hardware requirements.
- Extendable and easy to integrate with alert systems.
- Helps reduce manual CCTV footage reviews.

---

## 👨‍💻 Team Contributions

| Name            | Responsibility                             |
|-----------------|---------------------------------------------|
| Raju Ranjan     | OpenCV-based plate detection & preprocessing |
| Aashish Ranjan  | Data collection, testing & validation       |
| Pranav Ranjan   | EasyOCR integration & project management    |

---

## 💡 Future Enhancements

- Detect vehicle **color** and **type** (bike/car/truck).
- Cloud database or mobile app integration.
- SMS/Email alert system for flagged plates.
- Local language plate support.

---

## 📷 Example Output

| Timestamp   | Number Plate | Confidence | Screenshot |
|-------------|--------------|------------|------------|
| 2025-07-13  | BR01AB1234   | 91.2%      | ✅         |

---

## 📂 How to Run

```bash
# Clone the repository
git clone https://github.com/yourusername/anpr-project.git
cd anpr-project

# Install dependencies
pip install -r requirements.txt

# Run the main script
python main.py

# License
This project is open-source and available under the MIT License.

# Acknowledgements
-OpenCV
-EasyOCR
-Python
