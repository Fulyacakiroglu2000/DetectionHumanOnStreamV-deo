# myFile
 

I used OPENCV library in this project. OpenCV (Open Source Computer Vision) is an open source image processing library. Developed by Intel in 1999.I import many library as numpy,matplotlib for graph,time.
After that,I create a function.This function name is motionDetection().This function provide implemeting video url.Python not accepted direct YouTube link,so I right click on YouTube video and searched “m3u8”.I did copy-paste https between m3u8 part and Python worked succesfully.
I took frame1 and frame2.In this way,when I run codes,video countınue and I can see.

After that,I create while loop and actualized some instruction steps
 while cap.isOpened():
     diff = cv2.absdiff(frame1, frame2)
     gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
     blur = cv2.GaussianBlur(gray, (5,5), 0)
     _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
     dilated = cv2.dilate(thresh, None, iterations=3)
     contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

Firstly,diff provides make out the differences.Gray command converted to video gray color,Because this instruction provide getting to know people better.After,I used blur command.(5.5) is my matrices value and other value is sigma.This is optimum values.
I used threshold.Minimum value is 20 and maximum value is 255.This command ensured black and near black values convert black compeletely.This process also applied to whites.Dilated command to ensure declaring and values are thickness a little more.Iterations =3 meaning tells how many times to run the threshold applicationContours provided to edge detection.

I writed x,y,w,h in for loop.Thus, my edge determination process has started.
0,001 value I found it by trying and found it to be the optimum value.After that,I used rectangle command and drew rectangle in around people.
I writed Puttext command,Because I wanted writing on the video.
(10, 50)
My text ‘s coordinates.
.FONT_HERSHEY_SIMPLEX
Meaning is font style
 0.8, (0, 0, 0), 1
First value is magnitute.
(0,0,0) is to indicate font color
Last value is thickness.
 
frame1=frame2
     ret,frame2=cap.read()
     
This equality is provides examining the betweences frames when run each loop.


  
     if cv2.waitKey(30) & 0xff == ord("q"):
    

      break
    
    

This if purpose is If I press “q” ,I’m out of the loop.Destroy all Windows.



REFERENCES:
https://sogrekci.com/ders-notu/python-ve-bilimsel-hesaplama/42-grafik-cizimi/
http://mavienginberk.blogspot.com/2017/01/opencv-python-ile-arac-sayma.html
https://gist.github.com/pknowledge/623515e8ab35f1771ca2186630a13d14?permalink_comment_id=3179528
http://ibrahimdelibasoglu.blogspot.com/2016/08/python-opencv-ile-kisi-sayma.html
https://data-flair.training/blogs/python-project-real-time-human-detection-counting/
https://github.com/guptavasu1213/Yolo-Vehicle-Counter



