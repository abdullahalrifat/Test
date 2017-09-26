from django.http import  HttpResponse
from django.http import  Http404
from django.template import loader
from django.shortcuts import render
from django.views import  generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from Test.settings import BASE_DIR
from .models import pdf
from django.template.loader import get_template
from django.template import Context
from django.conf import settings
import pdfkit

'''


def index(request):

    users=pdf.objects.all()
    context={
        'allUsers':users,
    }
        #pdfkit.from_file('PDFGenerate/templates/PDFGenerate/pdf_form.html', 'out.pdf')

    return render(request,'PDFGenerate/pdf_form.html',context)

def pdfgen(request):

    # Create a  URL of our project and go to the template route
    projectUrl = request.get_host() + '/template'
    pdf = pdfkit.from_url(projectUrl, False)
    # Generate download
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ourcodeworld.pdf"'

    return response
'''
class form(CreateView):
    model = pdf
    fields =['name','org','talk','person_image']

class view(generic.ListView):

    template_name = 'PDFGenerate/done.html'
    def get_queryset(self):
        return pdf.objects.all()

class admin(generic.ListView):
    template_name = 'PDFGenerate/admin.html'
    def get_queryset(self):
        return pdf.objects.all()




class gen(generic.ListView):
    template_name = 'PDFGenerate/done.html'


    def render_to_pdf(self,template_src, context_dict,id):
        #template = get_template(template_src)
        #context =Context({"data": context_dict})  # data is the context data that is sent to the html file to render the output.
        #html = template.render(context)  # Renders the template with the context data.
        html=get_template(template_src).render({
            "data": context_dict,
            "img" :BASE_DIR+context_dict.person_image.url
        })
        pdfkit.from_string(html, 'out'+str(id)+'.pdf')
        #pdf = open("out"+id+".pdf")
        #response = HttpResponse(pdf.read(), content_type='application/pdf')  # Generates the response as pdf response.
        #response['Content-Disposition'] = 'attachment; filename=output.pdf'
        #pdf.close()
        # os.remove("out.pdf")  # remove the locally created pdf file.
        #return response  # returns the response.

    def myview(self):
        # Retrieve data or whatever you need
        for pdfs in pdf.objects.all():
            self.render_to_pdf('PDFGenerate/temp.html',pdfs,pdfs.id)


    def get_queryset(self):
        self.myview()
        return pdf.objects.all()

