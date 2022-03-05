import cv2
import os

video_pth = "/Users/arghamukherjee/Downloads/Codebase/GithbProjects/VideoToImgConvertorPython/source_video/running_with_a_kite.mp4"

data = cv2.VideoCapture(video_pth)
try:

    # creating a folder named data
    if not os.path.exists('extracted_frames_data'):
        os.makedirs('extracted_frames_data')

# if not created then raise error
except OSError:
    print('Error: Creating directory of data')

# frame
currentframe = 0

while (True):

    # reading from frame
    ret, frame = data.read()

    if ret:
        # if video is still left continue creating images
        name = './source_video/frame' + str(currentframe) + '.jpg'
        print('Creating...' + name)

        # writing the extracted images
        cv2.imwrite(name, frame)

        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    else:
        break

# Release all space and windows once done
data.release()
cv2.destroyAllWindows()