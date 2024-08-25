from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
from django.http import HttpResponse
from . forms import HTMLFileForm
from . utils import convert_html_to_dtl
import os

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        file_path = fs.save(f'html_files/{uploaded_file.name}', uploaded_file)
        
        with open(fs.path(file_path), 'r') as file:
            content = file.read()
        
        dtl_content = convert_html_to_dtl(content)
        
        # Save the converted content to a new file
        base_name = os.path.splitext(uploaded_file.name)[0]
        dtl_file_name = f"{base_name}_dtl.html"
        dtl_file_path = fs.save(f'dtl_files/{dtl_file_name}', ContentFile(dtl_content))
        
        return render(request, 'result.html', {
            'dtl_content': dtl_content,
            'dtl_file_name': dtl_file_name
        })
    else:
        form = HTMLFileForm()
    return render(request, 'upload.html', {'form': form})

def download_dtl(request, file_name):
    fs = FileSystemStorage()
    file_path = fs.path(f'dtl_files/{file_name}')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='text/html')
            response['Content-Disposition'] = f'attachment; filename="{file_name}"'
            return response
    return HttpResponse("File not found", status=404)