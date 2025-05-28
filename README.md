# Lyan-s-final-projects
Developed three AI-powered robotics projects: a pharmacy robot using facial recognition and Raspberry Pi to verify patient insurance; a school robot with emotion detection that alerts teachers via email if students seem upset; and an Arduino-based system that lights bulbs based on finger count detection.

----Pharmacy Robot: Facial Recognition-Based Insurance Verification System

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

---Emotion-Based Student Alert System Using Facial Recognition
This system uses a webcam to:

Recognize a known student's face.

Detect their emotional state.

Send an alert email if the student appears sad, angry, or scared.

