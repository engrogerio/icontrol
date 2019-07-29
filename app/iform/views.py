from app.iform.forms import IFormForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from app.iform.models import IForm, IFormTag
#from app.iform.forms import IFormTagFormSet
from django.contrib import messages
from django.forms import inlineformset_factory
from app.iform.forms import IFormTagForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

def IFormIndex(request):
    return HttpResponse ('Form list')

class IFormList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = ('iform.change_iform',) 
    model = IForm
    template_name = 'iform/iform_list.html'
    paginate_by = 6


class IFormDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ('iform.delete_iform',) 
    model = IForm
    form_class = IFormForm
    template_name = 'iform/iform_delete.html'
    success_url = reverse_lazy('iform:iform_list')

@login_required
def iform_create (request):
    IFormTagFormSet = inlineformset_factory(IForm, IFormTag, form=IFormTagForm, extra=1)

    if request.method == 'POST':
       
        # Create a blank Iform form with empty fields
        iform_form = IFormForm(request.POST)
        iform_form.created_by = request.user
        # Create a blank formset from the tags related to the iform
        iform_tag_formset = IFormTagFormSet(request.POST)

        if iform_form.is_valid() and iform_tag_formset.is_valid():
            # creates blank iform
            iform = iform_form.save(commit=False)
            iform.created_by = request.user
            iform.save()

            for forms in iform_tag_formset.forms:
                iform_tag = forms.save(commit=False)
                iform_tag.iform = iform
                iform_tag.save()
           
            messages.add_message(request, messages.SUCCESS, 'Form was succefully created!')
            return HttpResponseRedirect(reverse('iform:iform_list'))

    if request.method == 'GET':
        # create empty fields for iform
        iform_form = IFormForm()
        # Create an empty fields for formset
        iform_tag_formset = IFormTagFormSet()
    c = {'iform': iform_form, 'iform_tag': iform_tag_formset}
    # c.update(csrf(request)) # for invalidate every request
    return render(request, 'iform/iform_form.html', c)

@login_required
def iform_update(request, pk=None):
    # get iform being updated
    iform = IForm.objects.get(id=pk)
    iform_tags_len = IFormTag.objects.filter(iform=iform).count()
    # get the form related to iform
    iform_form = IFormForm(request.POST, instance=iform)
     
    # get the iform_tags form instance.
    IFormTagFormSet = inlineformset_factory(IForm, IFormTag, form=IFormTagForm, 
                        extra = 1 if iform_tags_len==0 else 0 , can_delete = True)

    if request.method == 'POST':

        # Brings iform and iform_tag forms
        iform_form = IFormForm(request.POST, instance= iform)
        #iformtag_form = IFormTagForm(request.POST, iform_id=iform.id)

        # Create formset from the tags related to the iform ordering by field order     
        iform_tag_formset = IFormTagFormSet(request.POST, instance = iform, queryset=IFormTag.objects.filter(iform=iform).all().order_by('order')) #iform.iforms.tag.order_by('order'))

        if iform_form.is_valid() and iform_tag_formset.is_valid():
            # saves iform form with the user
            iform = iform_form.save(commit=False)
            iform.updated_by = request.user
            iform.save()
            # delete when marked as delete loop
            for iform_tag_form in iform_tag_formset.forms:
                if iform_tag_form.cleaned_data['DELETE'] == True:
                    IFormTag.objects.filter(iform=iform).filter(tag__name=iform_tag_form.cleaned_data['tag']).delete()
                    
            # save them adjusting the order
            for n, iform_tag_form in enumerate(iform_tag_formset.forms):
                iform_tag = iform_tag_form.save(commit=False)
                iform_tag.iform = iform
                iform_tag.order = n + 1
                iform_tag.save()
                
            messages.add_message(request, messages.SUCCESS, 'Form was succefully updated!')
            return HttpResponseRedirect(reverse('iform:iform_list'))
            

    if request.method == 'GET':

        # get iform with the values
        iform_form = IFormForm(instance=iform)
        # get iform_tags formset with the values
        iform_tag_formset = IFormTagFormSet(instance=iform,
                                            queryset=iform.iforms.order_by('order'))
    c = {'iform': iform_form, 'iform_tag': iform_tag_formset}
    # c.update(csrf(request)) # for invalidate every request
    return render(request, 'iform/iform_form.html', c)