import recognizer.core.PostCardSaver as s
import recognizer.core.PostCardMatcher as m
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

import numpy as np

import io
import PIL

saver = s.PostCardSaver()
matcher = m.PostCardMatcher()

@csrf_exempt
def save(request):
    if request.method == 'POST':
        id  = request.POST['id']
        file = request.FILES['file']

        picture_stream = io.BytesIO(file.read())
        picture = PIL.Image.open(picture_stream)
        img =  np.array(picture)
        saver.saveImage(id, img)
        matcher.reloadFeatures()
        return HttpResponse(status=200)

@csrf_exempt
def match(request):
    if request.method == 'POST':
        file = request.FILES['file']

        picture_stream = io.BytesIO(file.read())
        picture = PIL.Image.open(picture_stream)
        img =  np.array(picture)
        return HttpResponse(str(matcher.findPicture(img)))

