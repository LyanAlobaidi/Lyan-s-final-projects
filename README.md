# Lyan-s-final-projects
Developed three AI-powered robotics projects: a pharmacy robot using facial recognition and Raspberry Pi to verify patient insurance; a school robot with emotion detection that alerts teachers via email if students seem upset; and an Arduino-based system that lights bulbs based on finger count detection.

----Pharmacy Robot: Facial Recognition-Based Insurance Verification System--- 

The robot is programmed in Python and uses facial recognition to identify patients and check their insurance validity. It relies on a Raspberry Pi as the microcontroller and uses the following algorithm: 
1) Face Detection & Recognition:
Detect faces in real-time video captured via the Raspberry Pi camera.

2) Recognition Handling:
When a face is recognized, the system compares it to known identities.
The most frequent match among the facial features determines the identity.
The recognized name is displayed in the video stream, and a snapshot is taken.

3) Communication System:
The code contains a section (currently disabled) that sends an automated email to request medicine approval.
The email includes the patient’s name, the time of request, and the captured image as an attachment

---Emotion-Based Student Alert System Using Facial Recognition ----

How the Algorithm Works (Step-by-Step)
1) Import Libraries:
Uses OpenCV, face_recognition, imutils, smtplib, and others for video capture, facial recognition, and email sending.

2) Face Data Loading:
Loads saved face data to identify students.
Loads a face detection model.

3) Start Video Stream:
Opens the webcam and starts reading video frames.

4) Detect and Recognize Faces:
Converts video frames to grayscale (for detection) and RGB (for recognition).
Detects faces in each frame.

5) Compares detected faces with known faces using embeddings.
If a Student is Recognized:
Saves an image of the student.
Calls an external emotion detection script (emotions.py) to find out how the student is feeling.

6) Emotion Check:
If the student is angry, fearful, or sad, it triggers an email alert to a specified address with:
The student’s name
The emotional state
A picture as an attachment

7)Email is Sent:
Uses Gmail SMTP to send the email.

8)End the Program:
If the alert is sent, the program stops.

----Finger Count-Based LED Display----

This project uses computer vision and Arduino to create an interactive LED display based on the number of fingers shown in front of a webcam. It combines Python programming with real-time hand tracking and hardware control to visually represent finger counts using 10 individual LEDs connected to an Arduino board.

1) Hand Tracking with OpenCV & Mediapipe:
The webcam captures real-time video.
Detects one or two hands and identifies which fingers are raised.

2) Finger Count Calculation:
The program calculates how many fingers are up across both hands (maximum: 10 fingers).
The total count is displayed on the video feed

3) LED Control via Arduino:
Each finger corresponds to a specific LED connected to digital pins on the Arduino (from D2 to D12).
Based on the total number of raised fingers, a Python function sends a signal to the Arduino using the pyfirmata library.
The corresponding LED lights up to match the finger count (e.g., if 3 fingers are up, LED 3 lights up).
