import recognizer.core.PostCardSaver as s
import recognizer.core.PostCardMatcher as m
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

import numpy as np

import io
import PIL
import os
from  django.shortcuts import render_to_response

saver = s.PostCardSaver()
matcher = m.PostCardMatcher()

@csrf_exempt
def save(request):
    if request.method == 'POST':
        id  = request.POST['id']
        file = request.FILES['file']

        picture_stream = io.BytesIO(file.read())
        picture = PIL.Image.open(picture_stream)
        open_cv_image = np.array(picture)
        # Convert RGB to BGR
        open_cv_image = open_cv_image[:, :, ::-1].copy()
        saver.saveImage(id, open_cv_image)
        return HttpResponse(status=200)

@csrf_exempt
def match(request):
    if request.method == 'POST':
        file = request.FILES['file']

        picture_stream = io.BytesIO(file.read())
        picture = PIL.Image.open(picture_stream)
        img =  np.array(picture)
        return HttpResponse(str(matcher.findPicture(img)))

@csrf_exempt
def postcards(request):
    if request.method == 'GET':
        path="Output/"
        img_list = os.listdir(path)
        return render_to_response('gallery.html', {'images': img_list})