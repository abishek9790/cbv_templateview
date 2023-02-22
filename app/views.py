from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
class cbv_template(TemplateView):
    template_name='cbv_template.html'

class cbv_context(TemplateView):
    template_name='cbv_context.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='abishek'
        context['course']='python'
        return context

class cbv_form(TemplateView):
    template_name='cbv_form.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['form']=jsprider()
        return context

    def post(self,request):
        data=jsprider(request.POST)
        if data.is_valid():
            return HttpResponse(str(data.cleaned_data))