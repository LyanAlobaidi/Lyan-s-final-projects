#! /usr/bin/python

# import the necessary packages
from imutils.video import VideoStream
from imutils.video import FPS
import face_recognition
import imutils
import pickle
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import cv2
import os


# Initialize 'currentname' to trigger only when a new person is identified.
def emotional_mood(name, img_name):
    #with open("emotions.py") as f:
        #exec(f.read())
    from emotions import x
    print(x)

    if x=="Angry" or x=="Fearful" or x=="Sad":
        send_message(name, img_name,x)
    else:
        quit()



def send_message(name, img_name,x):

    os.chdir(r"C:\Users\Amany.Amahdy\Desktop\amany\facial-recognition-main")
    global stoop
    stoop = 1

    username = 'amanymahdy92@gmail.com'
    password = 'vljqpiocgymeshda'
    # the email objects
    subject = "ALERT"
    recipent = 'amanymahdy92@gmail.com'
    content = name + " came to school at " + time.ctime() + " and she is " + x +" take care of her"
    emailData = MIMEMultipart()
    emailData['Subject'] = subject
    emailData['To'] = recipent
    emailData['From'] = username

    # Attach our text data
    emailData.attach(MIMEText(content))

    imageData = MIMEImage(open(img_name, 'rb').read(), 'jpg')
    imageData.add_header('Content-Disposition', 'attachment; filename="image.jpg"')
    emailData.attach(imageData)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.ehlo()
    s.login(username, password)
    # send the email
    s.sendmail(username, recipent, emailData.as_string())
    #print(stoop)
    rslt = s.quit()


# load the known faces and embeddings along with OpenCV's Haar
# cascade for face detection
def Camera():
    global stoop

    currentname = "unknown"
    # Determine faces from encodings.pickle file model created from train_model.py
    encodingsP = "encodings.pickle"
    # use this xml file
    cascade = "haarcascade_frontalface_default.xml"
    print("[INFO] loading encodings + face detector...")
    data = pickle.loads(open(encodingsP, "rb").read())
    detector = cv2.CascadeClassifier(cascade)

    # initialize the video stream and allow the camera sensor to warm up
    print("[INFO] starting video stream...")
    vs = VideoStream(src=1).start()
    # vs = VideoStream(usePiCamera=True).start()
    time.sleep(2.0)

    # start the FPS counter
    fps = FPS().start()

    stoop = 0
    # loop over frames from the video file stream
    while True:

        frame = vs.read()
        frame = imutils.resize(frame, width=500)

        # convert the input frame from (1) BGR to grayscale (for face
        # detection) and (2) from BGR to RGB (for face recognition)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # detect faces in the grayscale frame
        rects = detector.detectMultiScale(gray, scaleFactor=1.1,
                                          minNeighbors=5, minSize=(30, 30),
                                          flags=cv2.CASCADE_SCALE_IMAGE)

        # OpenCV returns bounding box coordinates in (x, y, w, h) order
        # but we need them in (top, right, bottom, left) order, so we
        # need to do a bit of reordering
        boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]

        # compute the facial embeddings for each face bounding box
        encodings = face_recognition.face_encodings(rgb, boxes)
        names = []

        # loop over the facial embeddings
        for encoding in encodings:
            # attempt to match each face in the input image to our known
            # encodings
            matches = face_recognition.compare_faces(data["encodings"],
                                                     encoding)
            name = "Unknown"

            # check to see if we have found a match
            if True in matches:
                # find the indexes of all matched faces then initialize a
                # dictionary to count the total number of times each face
                # was matched
                matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                counts = {}

                # loop over the matched indexes and maintain a count for
                # each recognized face face
                for i in matchedIdxs:
                    name = data["names"][i]
                    counts[name] = counts.get(name, 0) + 1

                # determine the recognized face with the largest number
                # of votes (note: in the event of an unlikely tie Python
                # will select first entry in the dictionary)
                name = max(counts, key=counts.get)

                # If someone in your dataset is identified, print their name on the screen
                if currentname != name:
                    currentname = name
                    print(currentname)
                    # Take a picture to send in the email
                    img_name = "image.jpg"
                    cv2.imwrite(img_name, frame)

                    print('Taking a picture.')

                    fps.stop()
                    cv2.destroyAllWindows()
                    vs.stop()

                    emotional_mood(name, img_name)
                    break
            # update the list of names
            names.append(name)

        # loop over the recognized faces
        for ((top, right, bottom, left), name) in zip(boxes, names):
            # draw the predicted face name on the image - color is in BGR
            cv2.rectangle(frame, (left, top), (right, bottom),
                          (0, 255, 225), 2)
            y = top - 15 if top - 15 > 15 else top + 15
            cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                        .8, (0, 255, 255), 2)
        # display the image to our screen
        cv2.imshow("Facial Recognition is Running", frame)
        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop

        if stoop == 1:
            print(5)
            break
        # update the FPS counter
        fps.update()

    # stop the timer and display FPS information
    fps.stop()
    print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

    # do a bit of cleanup
    cv2.destroyAllWindows()
    vs.stop()


Camera()
