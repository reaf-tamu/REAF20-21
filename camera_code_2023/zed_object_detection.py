git clone https://github.com/ultralytics/yolov5
# Install the dependencies if needed
cd yolov5
pip install -r requirements.txt

# Downloading by commmand line
# wget https://github.com/ultralytics/yolov5/releases/download/v6.0/yolov5m.pt
wget https://github.com/reaf-tamu/REAF20-21/blob/master/camera_code_2023/best.pt

python detector.py --weights best.pt # [--img_size 416 --conf_thres 0.4 --svo path/to/file.svo]