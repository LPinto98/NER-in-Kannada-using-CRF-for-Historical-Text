from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse,JsonResponse
from .forms import InputForm
import subprocess
from subprocess import run, PIPE
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# from .models import NER_form
def index(request):
    text=''
    if(request.method=="POST"):
        form = InputForm(request.POST,request.FILES)
        if form.is_valid():
            text = form.cleaned_data.get('inp')
            with open(os.path.join(BASE_DIR,'main/ner_input.txt'), mode='w+', encoding='utf-8') as f:
	            f.write(text)
	            f.close()
            run([sys.executable,os.path.join(BASE_DIR,'main/supervised.py'),os.path.join(BASE_DIR,'main/ner_input.txt')],shell=False, stdout=PIPE)
            run([sys.executable,os.path.join(BASE_DIR,'main/senno.py')],shell=False, stdout=PIPE)
            run([sys.executable,os.path.join(BASE_DIR,'main/ner.py')],shell=False, stdout=PIPE)
            run([sys.executable,os.path.join(BASE_DIR,'main/output_list.py')],shell=False, stdout=PIPE)
            lines=[]
            if os.path.exists(os.path.join(BASE_DIR,'main/ner_input.txt')):
                os.remove(os.path.join(BASE_DIR,'main/ner_input.txt'))
            with open(os.path.join(BASE_DIR,'main/op.txt'), mode='r',encoding='utf-8') as filey:
                for line in filey:
                    lines.append(line)
            return render(request, 'mainpage.html',{'text':lines,'form':form})
    else:
        form = InputForm()
    return render(request, 'mainpage.html',{'text':text,'form':form})