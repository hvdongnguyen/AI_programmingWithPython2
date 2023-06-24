# Dog-Breed-Identifier
This is for a mandatory project of the Udacity Nanodagree program - course "Ai Programming with Python"

This program can identify dog breeds on images.
* -- Please put your dog images into `pet_images` folder
* -- There will be a stats summary assumed that dog file name indicate dog breed to measure how accurate the identifier run. If you are lazy to name the file, please ignore the stats summary

You will need the followings to run:
* Python 3
* Pillow PIL Fork
* Pytorch 0.4 or higher

Execute this command to run:
`python check_images.py --dir pet_images/`

There are 3 trained models to choose from:
* - vgg
* - alexnet
* - resnet

To change learning model, please edit `get_input_args.py` and change the `default` value of argument `--arch`.

If you want to test all 3 models. Please run `batch.sh` and put photos into `uploaded_images`. After finish, results will be stored in `alexnet_uploaded-images.txt`, `resnet_uploaded-images.txt` and `vgg_uploaded-images.txt` file of the according model


