from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.template import RequestContext

from django.contrib import messages

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Fieldset

from fails.models import Submission

class SubmissionForm(forms.ModelForm):

    def __init__(self,*args, **kwargs):
        super(SubmissionForm,self).__init__(*args, **kwargs)
        
        self.helper = FormHelper(self)
        self.helper.form_method = "POST"
        self.helper.form_action = reverse(add)

        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'

        self.helper.layout = Layout(
            Fieldset(
                "What software package are you talking about?",
                'vendor',
                'software',
                'location',
                ),
            Fieldset(
                "Describe the problem",
                'title',
                'description',
                ),
            Submit('submit', 'Submit'),
            )


    class Meta:
        model = Submission

def add(request):
    form = SubmissionForm()
    if request.POST:
        form = SubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save()
            messages.add_message(request,messages.SUCCESS,'Your submission has been saved')
            return HttpResponseRedirect(reverse(list))
    return render_to_response('fails/add.html',{
        'form':form,
        }, context_instance=RequestContext(request))


def list(request):
    return HttpResponseRedirect(reverse(add))