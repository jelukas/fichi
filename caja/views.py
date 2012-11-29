# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from caja.models import Fichero
from caja.forms import FicheroForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

import sys



def response_mimetype(request):
    if "application/json" in request.META['HTTP_ACCEPT']:
        return "application/json"
    else:
        return "text/plain"



from django.utils import simplejson
class JSONResponse(HttpResponse):
    """JSON response class."""
    def __init__(self,obj='',json_opts={},mimetype="application/json",*args,**kwargs):
        content = simplejson.dumps(obj,**json_opts)
        super(JSONResponse,self).__init__(content,mimetype,*args,**kwargs)


def subir_fichero(request):
    if request.method == 'POST': # If the form has been submitted...
        fichero_form = FicheroForm(request.POST,request.FILES) # A form bound to the POST data
        if fichero_form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            fichero = fichero_form.save(commit=False)
            fichero.nombre = fichero.file.path
            fichero.save()

            #Devolvemos un JSon para poder formar el nuevo nodo HTML una vez subido
            data = [{'name': fichero.file.name}]
            response = JSONResponse(data, {}, response_mimetype(request))
            response['Content-Disposition'] = 'inline; filename=files.json'
            return response
            #return HttpResponseRedirect(reverse('caja.views.subir_fichero')) # Redirect after POST
        else:
            print >>sys.stderr, 'Failed to save Fichero'
            print >>sys.stderr, fichero_form.errors
    else:
        fichero_form = FicheroForm() # An unbound form

    return render_to_response('caja/subir_fichero.html',{'fichero_form':fichero_form},context_instance = RequestContext(request))



