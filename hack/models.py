from django.db import models
from time import sleep
import cv2
import numpy as np
import pickle

# Create your models here.


class RequestForAnalysis(models.Model):
    upper_threshold = models.IntegerField(default= 65536)
    lower_threshold = models.IntegerField(default= 0)


class VideoPlayModel(models.Model):
    frame_no = models.IntegerField(default=0)


class PictureModel(models.Model):
    frame_no = models.IntegerField(default=0)




class Abnormalities(models.Model):
    video_no = models.IntegerField(default= 0)
    frames = []








