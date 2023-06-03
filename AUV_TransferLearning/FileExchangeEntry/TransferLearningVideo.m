% Copyright 2017 The MathWorks, Inc.

%% Load a pre-trained, deep, convolutional network
alex = alexnet;
layers = alex.Layers

%% Modify the network to use five categories
layers(23) = fullyConnectedLayer(2); 
layers(25) = classificationLayer

%% Set up our training data
allImages = imageDatastore('myImages', 'IncludeSubfolders', true, 'LabelSource', 'foldernames');
[trainingImages, testImages] = splitEachLabel(allImages, 0.8, 'randomize');

%% Re-train the Network
opts = trainingOptions('sgdm', 'InitialLearnRate', 0.001, 'MaxEpochs', 20, 'MiniBatchSize', 64, 'Plots', 'training-progress');
trainingImages.ReadFcn = @readFunctionTrain;
myNet2 = trainNetwork(trainingImages, layers, opts);

%% Measure network accuracy
testImages.ReadFcn = @readFunctionTrain
predictedLabels = classify(myNet2, testImages); 
accuracy = mean(predictedLabels == testImages.Labels)

[labels, err_test] = classify(myNet2,testImages);

%% Save network
AUV_detector2 = myNet2
save AUV_detector2
