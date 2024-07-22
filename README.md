# Video-Editing-Application
This Python application allows users to display, navigate, and crop videos. It features a user-friendly interface created with Qt Designer and leverages QThreads for efficient performance. The application supports videos captured with Kinect cameras and provides functionality for saving joints data to a text file.

## Features
Video Display: Load and display videos with frame-by-frame navigation.
Cropping Tool: Select a portion of the video to crop and save it.
User Interface: Intuitive UI with a scrolling area for frames and keyboard controls for navigation.
Frame Selection: Use sliders to choose start and end frames for cropping.
Path Display: Shows the path where the cropped video is saved.
Kinect Support: Handles videos captured with Kinect cameras and saves joints data.

## Application Workflow
1. Load Video:
Select a video file through the file dialog.
The video will be displayed frame by frame in the scrolling area.
2. Navigate Video:
Use keyboard controls to navigate through the frames.
Utilize sliders to select the start and end frames for cropping.
3. Crop Video:
Select the area to crop using the cropping tool.
Save the cropped video to the desired location.
3. Kinect Data Handling:
If the video is captured with a Kinect camera, the application can save the joints data to a text file.