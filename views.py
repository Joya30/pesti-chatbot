from django.shortcuts import render
from django.http import JsonResponse
import google.generativeai as genai
import os
import nltk
os.getenv('AIzaSyDt1TMqr33BAknZCKEIIFxMzCRGkuLkEVc')
# Create your views here.
def index(request):
    return render(request, 'index.html')

def bot(request):
    if request.method == 'POST':
        text=request.POST.get('text')
        result=sent_message(text)
        return render(request, 'bot.html',{'result':result,'usertext':text})
    return render(request,'bot.html',{'result':None})


def sent_message(txt):
        b=nltk.word_tokenize(txt)
        print(b)
        if 'pesticide' in b:
            genai.configure(api_key='AIzaSyDt1TMqr33BAknZCKEIIFxMzCRGkuLkEVc')
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(txt)
            res = response.text
            print(res)
            return res
        else:
            res='Sorry We Didn\'t understand'
            return res


