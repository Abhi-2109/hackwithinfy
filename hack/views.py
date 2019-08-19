from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CompileSerializer, VideoPlaySerializer, PictureSeeSerilizer
from time import sleep
import cv2
import numpy as np
import pickle

output_data_last = None
input_data_last = None


def index(request):
    return render(request, 'index.html')


def loadData():
    file = open('real_record.pkl', 'rb')
    frames = pickle.load(file)
    file.close()
    return frames


# def process_data(video_path,upper_threshold,lower_threshold):
def process_data(upper_threshold, lower_threshold):
    global input_data_last, output_data_last
    frames = loadData()
    input_data_last = frames

    # print("One Frame Shape Color Image ",frames[0]['color_image'].shape)
    # print("Total Number of Frames",len(frames))
    # print("Depth Shape",frames[0]['depth_image'].shape)
    # print(frames[0]['depth_image'][1].max())

    ctr = 0
    l = []
    for frame in frames:

        cv2.imshow('color', frame['color_image'])
        cv2.waitKey(1)
        sleep(0.1)
        me = []

        for depth in frame['depth_image']:
            # depth is  (840*680)
            a = depth.mean()
            me.append(a)

        men = sum(me) / len(me)
        print(ctr, men)

        # upper threshold can be 800 and lower_threshold can be zero
        if men < upper_threshold and men > lower_threshold:
            l.append((ctr, upper_threshold - men))
        ctr += 1
    cv2.destroyAllWindows()
    output_data_last = l
    sleep(5.0)
    for i in output_data_last:
        cv2.imshow('colorm', input_data_last[i[0]]['color_image'])
        print(i[1])
        cv2.waitKey(1)
        sleep(0.1)
    cv2.destroyAllWindows()


    return l




class ProcessIt(APIView):
    serializer_class = CompileSerializer

    def get(self, request, blah=None):
        return Response({'abnormal_frames': process_data(700,0)})


class PictureSee(APIView):
    serializer_class = PictureSeeSerilizer

    def get(self, request, blah=None):
        seePicAtFrame(request.data['frame_no'])
        return Response({"Status": "Picture Shown"})


class VideoPlay(APIView):
    serializer_class = VideoPlaySerializer

    def get(self, request, blah=None):

        global output_data_last,input_data_last
        if output_data_last == None:
            return Response({"VideoPlay": "Error"})

        for i in output_data_last:
            cv2.imshow('colorm', input_data_last[i[0]]['color_image'])
            print(i[1])
            cv2.waitKey(1)
            sleep(0.1)
        cv2.destroyAllWindows()

        sleep(3.0)


        return Response({"VideoPlay": "Played"})



def seePicAtFrame(i):
    frames = input_data_last

    cv2.imshow('color', frames[i]['color_image'])
    cv2.waitKey(5000)
    sleep(0.1)
    cv2.destroyAllWindows()


def home(request):
    return render(request, 'templates/index.html')
