
#!/usr/bin/env python3

import pyzed.sl as sl
import time
import numpy as np
import cv2

init = sl.InitParameters()
camera = sl.Camera()

if not camera.is_opened():
    print("Opening ZED Camera...")
status = camera.open(init)
if status != sl.ERROR_CODE.SUCCESS:
    print(repr(status))

mat = sl.Mat()

runtime = sl.RuntimeParameters()

init = sl.InitParameters()
#init.camera_resolution = sl.RESOLUTION.RESOLUTION_VGA
#init.camera_resolution = sl.RESOLUTION.RESOLUTION_HD720
#init.camera_resolution = sl.RESOLUTION.RESOLUTION_HD1080
#init.camera_linux_id = 0
init.camera_fps = 10  # The framerate is lowered to avoid any USB3 bandwidth issues

camera = sl.Camera()
cam_status = camera.open(init)

mat = sl.Mat()
T=True
p=1
while T:

    camera.set_camera_settings(sl.VIDEO_SETTINGS.BRIGHTNESS, 0)
    camera.set_camera_settings(sl.VIDEO_SETTINGS.CONTRAST, 0)
    #cam.set_camera_settings(sl.VIDEO_SETTINGS.HUE, -1)
    #camera.set_camera_settings(sl.VIDEO_SETTINGS.SATURATION, 8)
    #cam.set_camera_settings(sl.VIDEO_SETTINGS.SHARPNESS, -1)
    #cam.set_camera_settings(sl.VIDEO_SETTINGS.GAIN, -1)
    #camera.set_camera_settings(sl.VIDEO_SETTINGS.EXPOSURE,100)
    #camera.set_camera_settings(sl.VIDEO_SETTINGS.WHITEBALANCE_TEMPERATURE, 4000)
    #camera.set_camera_settings(sl.VIDEO_SETTINGS.WHITEBALANCE, )    
    #init = sl.InitParameters()
    
    cam.set_camera_settings(sl.VIDEO_SETTINGS.GAMMA, 0)
    
    
    
    # Obtain camera image and get timestamps
    t1 = time.process_time()
    err = camera.grab(runtime)

    # If grabbing image successfull, save to buffer
    if err == sl.ERROR_CODE.SUCCESS:
        #camera.retrieve_image(mat, sl.VIEW.VIEW_SIDE_BY_SIDE)
        camera.retrieve_image(mat, sl.VIEW.LEFT)
        img = mat.get_data()

        #img_name = 'images/filename_{}.jpg'.format(time.time())


        img_name = '/home/nvidia-gh/Desktop/Communication-Nvidia/test_for_me/filename_{}.jpg'.format(time.time())
        # Saving as numpy array
        # t2 = time.process_time()
        # np.save(img_name, img)
        # print("np.save took {} ms".format((time.process_time()-t2)*1e3))
        p=p+1
        
        img = mat.write(img_name)
        T=False
    
        '''t1 = time.process_time()
        img = sl.ERROR_CODE.ERROR_CODE_FAILURE
        countdown = 5
        while img != sl.ERROR_CODE.SUCCESS or countdown > 0:
            img = mat.write(img_name)
            countdown -= 1
            if img == sl.ERROR_CODE.SUCCESS:
                break'''

        print("Saving file took {} ms".format((time.process_time()-t1)*1e3))
