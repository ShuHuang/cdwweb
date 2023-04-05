from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, StreamingHttpResponse, FileResponse
import os
from pathlib import Path


@login_required()
def home(request):
    return render(request, 'about/home.html')


@login_required()
def about(request):
    return render(request, 'about/about.html', {'title': 'About'})


@login_required()
def reader(request):
    return render(request, 'about/reader.html', {'title': 'Reader'})


# @login_required()
def citing(request):
    return render(request, 'about/citing.html', {'title': 'Citing'})


def acknowledgement(request):
    return render(request, 'about/acknowledgement.html', {'title': 'Acknowledgement'})


# @login_required()
def contact(request):
    return render(request, 'about/contact.html', {'title': 'Contact'})


def file_response_download(request, file_path):
    ext = os.path.basename(file_path).split('.')[-1].lower()
    # cannot be used to download py, db and sqlite3 files.
    if ext not in ['py', 'db',  'sqlite3']:
        BASE_DIR = Path(__file__).resolve().parent.parent
        response = FileResponse(open(os.path.join(BASE_DIR, 'about/static/images', file_path), 'rb'))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
        return response
    else:
        raise Http404

