import cv2
import easyocr
import os
import re
from datetime import datetime

# Path to Haar Cascade file
harcascade = "model/haarcascade_indian_plate_number.xml"

# Create directory for saving plate images
if not os.path.exists("plates"):
    os.makedirs("plates")

# Webcam setup
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

min_area = 500
count = 0

# Initialize EasyOCR Reader (CPU version)
reader = easyocr.Reader(['en'], gpu=False)

# Function to fix common OCR mistakes
def correct_ocr_text(text):
    text = text.upper()
    corrections = {
        'I': '1',
        'O': '0',
        'Q': '0',
        'Z': '2',
        'S': '5',
    
    }
    corrected = ''
    for char in text:
        corrected += corrections.get(char, char)
    return corrected

while True:
    success, img = cap.read()
    plate_cascade = cv2.CascadeClassifier(harcascade)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    for (x, y, w, h) in plates:
        area = w * h
        if area > min_area:
            # Draw rectangle & label
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "Number Plate", (x, y - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)

            # Extract ROI (Region of Interest)
            img_roi = img[y: y + h, x: x + w]
            cv2.imshow("ROI", img_roi)

    # Display main webcam frame
    cv2.imshow("Result", img)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('s') and 'img_roi' in locals():
        # Save plate image with time and date stamp in filename
        timestamp = datetime.now().strftime("%d%m%y_%H%M%S")
        file_path = f"plates/scaned_img_{count}_{timestamp}.jpg"
        cv2.imwrite(file_path, img_roi)

        # Preprocess for better OCR: sharpen + grayscale
        gray = cv2.cvtColor(img_roi, cv2.COLOR_BGR2GRAY)
        sharpened = cv2.addWeighted(gray, 1.5, cv2.GaussianBlur(gray, (3, 3), 0), -0.5, 0)

        # OCR using EasyOCR
        result = reader.readtext(sharpened)

        # Extract and correct plate text
        plate_text = result[0][1] if result else ""
        plate_text = re.sub(r'[^A-Z0-9]', '', plate_text.upper())
        plate_text = correct_ocr_text(plate_text)

        # Try to match valid Indian plate format
        match = re.match(r'[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}', plate_text)
        final_plate = match.group() if match else plate_text

        now_str = datetime.now().strftime('%d/%m/%y %H:%M:%S')
        print(f"Detected Plate: {final_plate} | Time: {now_str}")

        # Save the detected plate text with time to a text file
        with open("plates/detected_plates.txt", "a") as f:
            f.write(f"{final_plate} | {now_str}\n")

        # Show feedback on screen
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, f"Saved: {final_plate}", (50, 265),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.putText(img, now_str, (50, 295),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.imshow("Results", img)
        cv2.waitKey(500)

        count += 1

    elif key == ord('q'):
        break
