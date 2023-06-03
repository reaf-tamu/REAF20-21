%% load network
load('AUV_detector2.mat')

% initialize webcam
cam = webcam(2)

%% capture image and detect
for idx = 1:100
    Im = snapshot(cam);
    smallIm = imresize(Im, [227 227]);
    
    [label,conf] = classify(myNet2, smallIm)

    imshow(smallIm);
    title(sprintf('%s %.2f', label, max(conf)))

    pause(3);
end

%% end camera
cam = 0
