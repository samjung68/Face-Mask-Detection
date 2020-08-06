# Project : COVID-19 Face Mask Detector
Face Mask Detection system built with OpenCV, Keras/TensorFlow using Deep Learning in order to detect face masks in static images and videos as well as in real-time video streams

## Motivation
The COVID-19 mask detector we’re building here today could potentially be used to help ensure your safety and the safety of others.

## Screenshots
<p align="center"><img src="https://github.com/samjung68/Face-Mask-Detection/blob/master/capture_result.png" width="700" height="400"></p>

## Tech/framework used

- [OpenCV](https://opencv.org/)
- [Keras](https://keras.io/)
- [TensorFlow](https://www.tensorflow.org/)

## Working

1. Open terminal. Go into the cloned project directory folder and type the following command:
```
$ python3 train_mask_detector.py --dataset dataset
```

2. Now detect the face masks in images 
```
$ python3 detect_mask_image.py --image images/pic1.jpeg
```

3. Detection in real-time video streams
```
$ python3 detect_mask_video.py 
```
## Results

#### We got the following accuracy/loss training curve plot
![](https://github.com/chandrikadeb7/Face-Mask-Detection/blob/master/plot.png)

## Contribution
Feel free to **file a new issue** with a respective title and description on the the [Face-Mask-Detection](https://github.com/chandrikadeb7/Face-Mask-Detection/issues) repository. If you already found a solution to your problem, **I would love to review your pull request**! 

## Owner
Made by [Jae Hwa Jung, Samuel](https://github.com/samjung68)

## Credits
* [⁠https://www.pyimagesearch.com/2020/05/04/covid-19-face-mask-detector-with-opencv-keras-tensorflow-and-deep-learning/](https://www.pyimagesearch.com/2020/05/04/covid-19-face-mask-detector-with-opencv-keras-tensorflow-and-deep-learning/)
* [https://www.tensorflow.org/tutorials/images/transfer_learning](https://www.tensorflow.org/tutorials/images/transfer_learning)

## License
MIT

