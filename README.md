# Project : COVID-19 Face Mask Detector
Face Mask Detection system built with OpenCV, Keras/TensorFlow using Deep Learning in order to detect face masks in static images and videos as well as in real-time video streams

## Motivation
The COVID-19 mask detector we’re building here today could potentially be used to help ensure your safety and the safety of others.

<p align="center"><img src="https://github.com/samjung68/Face-Mask-Detection/blob/master/COVID19.png" width="700" height="400"></p>

## Demo/Screenshot

:movie_camera: [YouTube Demo Link](https://youtu.be/sCDdkOFIkmM)

<p align="center"><img src="https://github.com/samjung68/Face-Mask-Detection/blob/master/capture_result.png" width="700" height="400"></p>

## Tech/framework used

- [OpenCV](https://opencv.org/)
- [Keras](https://keras.io/)
- [TensorFlow](https://www.tensorflow.org/)

## :key: Prerequisites

All the dependencies and required libraries are included in the file <code>requirements.txt</code> [See here](https://github.com/samjung68/Face-Mask-Detection/blob/master/requirements.txt)

## :file_folder: Dataset

The dataset used can be downloaded here - [Click to Download](https://drive.google.com/drive/folders/1I8FtAT-Ozpk_wg813R1z5C80oth6Jtwt?usp=sharing)

The dataset we’ll be using here was created by PyImageSearch reader [Prajna Bhandary](https://www.linkedin.com/feed/update/urn%3Ali%3Aactivity%3A6655711815361761280/) and [Data Augmentation](https://www.pyimagesearch.com/2019/07/08/keras-imagedatagenerator-and-data-augmentation/) was applied to increase the generalizability of the model.

This dataset consists of __615 images__ belonging to two classes:
*	__with_mask: 218 images__
*	__without_mask: 397 images__

## Working

1. Open terminal. Go into the cloned project directory folder and type the following command:
```
$ python3 mask_detector_webcam_py.py --dataset dataset
```

2. Now detect the face masks in images 
```
$ python3 mask_detector_webcam_py.py --image images/pic1.jpeg
```

3. Detection in real-time video streams
```
$ python3 mask_detector_webcam_py 
```
## Results

- We got the following accuracy/loss training curve plot
![](https://github.com/samjung68/Face-Mask-Detection/blob/master/loss_graph.png)

## Contribution
Feel free to **file a new issue** with a respective title and description on the the [Face-Mask-Detection](https://github.com/samjung68/Face-Mask-Detection/issues) repository. If you already found a solution to your problem, **I would love to review your pull request**! 

## Owner
Made by [Jae Hwa, Samuel Jung](https://github.com/samjung68) (samjung00@naver.com)

## Credits
* [⁠https://www.pyimagesearch.com/2020/05/04/covid-19-face-mask-detector-with-opencv-keras-tensorflow-and-deep-learning/](https://www.pyimagesearch.com/2020/05/04/covid-19-face-mask-detector-with-opencv-keras-tensorflow-and-deep-learning/)
* [https://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_Image_Object_Detection_Face_Detection_Haar_Cascade_Classifiers.php](https://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_Image_Object_Detection_Face_Detection_Haar_Cascade_Classifiers.php)
* [http://datahacker.rs/001-how-to-read-a-video-and-access-a-webcam-with-opencv-in-python/](http://datahacker.rs/001-how-to-read-a-video-and-access-a-webcam-with-opencv-in-python/)
* [https://www.dlology.com/blog/how-to-do-hyperparameter-search-with-baysian-optimization-for-keras-model/](https://www.dlology.com/blog/how-to-do-hyperparameter-search-with-baysian-optimization-for-keras-model/)
⁠
## License
MIT © [Jae Hwa, Samuel Jung](https://github.com/samjung68/Face-Mask-Detection/blob/master/LICENSE)

