
import pyzed.sl as sl

zed = sl.Camera()

init_params = sl.InitParameters()
init_params.camera_resolution = sl.RESOLUTION.HD720  # Use HD720 video mode
init_params.depth_mode = sl.DEPTH_MODE.PERFORMANCE
init_params.coordinate_units = sl.UNIT.METER
init_params.sdk_verbose = True

err = zed.open(init_params)
if err != sl.ERROR_CODE.SUCCESS:
    exit(1)
    
# Define the Objects detection module parameters
obj_param = sl.ObjectDetectionParameters()
obj_param.enable_tracking=True
obj_param.image_sync=True
#obj_param.enable_mask_output=True

# Object tracking requires the positional tracking module
camera_infos = zed.get_camera_information()
if obj_param.enable_tracking :
    zed.enable_positional_tracking()
    
err = zed.enable_object_detection(obj_param)
if err != sl.ERROR_CODE.SUCCESS :
    print (repr(err))
    zed.close()
    exit(1)
    
# Detection Output
objects = sl.Objects()
# Detection runtime parameters
obj_runtime_param = sl.ObjectDetectionRuntimeParameters()
while zed.grab() == sl.ERROR_CODE.SUCCESS:
    zed_error = zed.retrieve_objects(objects, obj_runtime_param);
    if objects.is_new :
        print(str(len(objects.object_list))+" Object(s) detected")
        for object in objects.object_list:
          print(f"{object.id} \t {object.position}")

