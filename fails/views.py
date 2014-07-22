from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.template import RequestContext

def add(request):
	return render_to_response('fails/add.html',{
		'form':False,
		}, context_instance=RequestContext(request))


def list(request):
	return HttpResponseRedirect(reverse(add))