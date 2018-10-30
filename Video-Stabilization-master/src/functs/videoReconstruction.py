import cv2
import os

def reconVideo (videoInPath, videoOutPath, trans, BORDER_CUT):
    # video in info
    videoIn = cv2.VideoCapture(videoInPath)
    N_FRAMES = int(videoIn.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
    FPS = videoIn.get(cv2.cv.CV_CAP_PROP_FPS)
    FOURCC = videoIn.get(cv2.cv.CV_CAP_PROP_FOURCC)
    VID_WIDTH = videoIn.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
    VID_HEIGHT = videoIn.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
    print(VID_WIDTH,"VID_WIDTH------------------")
    print(VID_HEIGHT,"VID_HEIGHT-----------------------------------")
    print("////////////////////////////////////////////////////////")
    # video out creation
    videoInSize = (int(VID_WIDTH), int(VID_HEIGHT))
    print(videoInSize,"ppppppppppppppppppppppppppp")
    videoOutSize = (int(VID_WIDTH) - 2*BORDER_CUT, int(VID_HEIGHT) - 2*BORDER_CUT)
    print(videoOutPath,"?????????????????????????????")
    print(FOURCC,";;;;;;;;;;;;;;;;;;")
    print(FPS,"********************************")
    print(videoOutSize,"......................")
    videoOut = cv2.VideoWriter('xyz.mp4',int(FOURCC), int(FPS), videoOutSize)
    print(videoOut,"))))))))))))))))))))))))))))))")
    # frame transformation
    for i in range(N_FRAMES):
        ret, frame = videoIn.read()
        frameOut = cv2.warpPerspective(frame, trans[i,:,:], videoInSize, flags=cv2.INTER_NEAREST)
        frameOut = frameOut[BORDER_CUT:-BORDER_CUT, BORDER_CUT:-BORDER_CUT]
        videoOut.write(frameOut)
    print(videoInSize,"1111111111111111111111111111111111111111111111111111111")
    print(videoOutSize,"1111111111111111111111111111111111111111111111111111111")
    print(videoOut,"1111111111111111111111111111111111111111111111111111111")
    print(videoIn,"2222222222222222222222222222222222222222222222222222222")
    videoIn.release()
    videoOut.release()
