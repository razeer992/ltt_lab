from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Conveyor, Splice, Belt, Press

#def splices_view(request):
#    return render(request, )
def profile(request):
    return render(request, 'profile.html')

def base_view(request):
    return render(request, 'base_view.html')

def home(request):
    return render(request, 'home.html')

def conveyors_view(request):  
    conveyors = Conveyor.objects.all()
    context = {'conveyors': conveyors}
    return render(request, 'connectors/only_view/conveyors_view.html', context)

def conveyor_view(request, id):  
    conveyor = Conveyor.objects.get(id=id)
    context = {'conveyor': conveyor}
    return render(request, 'connectors/only_view/conveyor_view.html', context)

def belts_view(request):  
    belts = Belt.objects.all()
    context = {'belts': belts}
    return render(request, 'connectors/only_view/belts_view.html', context)

def belt_view(request, id):  
    belt = Belt.objects.get(id=id)
    context = {'belt': belt}
    return render(request, 'connectors/only_view/belt_view.html', context)

def splices_view(request):  
    splices = Splice.objects.all()
    context = {'splices': splices}
    return render(request, 'connectors/only_view/splices_view.html', context)

def splice_view(request, id):  
    splice = Splice.objects.get(id=id)
    context = {'splice': splice}
    return render(request, 'connectors/only_view/splice_view.html', context)

def presses_view(request):  
    presses = Press.objects.all()
    context = {'presses': presses}
    return render(request, 'connectors/only_view/presses_view.html', context)

def press_view(request, id):  
    press = Press.objects.get(id=id)
    context = {'press': press}
    return render(request, 'connectors/only_view/press_view.html', context)

class OwnerMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)
    
class OwnerEditMixin:
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    

#CONVEYOR    
    
class OwnerConveyorMixin(OwnerMixin, LoginRequiredMixin, PermissionRequiredMixin):
    model = Conveyor
    fields = ['name', 'mine']
    success_url = reverse_lazy('manage_conveyor_list')

class OwnerConveyorEditMixin(OwnerConveyorMixin, OwnerEditMixin):
    template_name = 'connectors/manage/conveyor/form.html'

class ManageConveyorListView(OwnerConveyorMixin, ListView):
    model = Conveyor
    template_name = 'connectors/manage/conveyor/list.html'
    permission_required = 'connectors.view_conveyor'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)
    
class ConveyorCreateView(OwnerConveyorEditMixin, CreateView):
    permission_required = 'connectors.add_conveyor'
    

class ConveyorUpdateView(OwnerConveyorEditMixin, UpdateView):
    permission_required = 'connectors.change_conveyor'
    

class ConveyorDeleteView(OwnerConveyorMixin, DeleteView):
    template_name = 'connectors/manage/conveyor/delete.html'
    permission_required = 'connectors.delete_conveyor'

#BELT    
    
class OwnerBeltMixin(OwnerMixin, LoginRequiredMixin, PermissionRequiredMixin):
    model = Belt
    fields = ['name', 'endurance', 'width', 'describe']
    success_url = reverse_lazy('manage_belt_list')

class OwnerBeltEditMixin(OwnerBeltMixin, OwnerEditMixin):
    template_name = 'connectors/manage/belt/form.html'

class ManageBeltListView(OwnerBeltMixin, ListView):
    model = Belt
    template_name = 'connectors/manage/belt/list.html'
    permission_required = 'connectors.view_belt'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)
    
class BeltCreateView(OwnerBeltEditMixin, CreateView):
    permission_required = 'connectors.add_belt'
    

class BeltUpdateView(OwnerBeltEditMixin, UpdateView):
    permission_required = 'connectors.change_belt'
    

class BeltDeleteView(OwnerBeltMixin, DeleteView):
    template_name = 'connectors/manage/belt/delete.html'
    permission_required = 'connectors.delete_belt'

#PRESS    
    
class OwnerPressMixin(OwnerMixin, LoginRequiredMixin, PermissionRequiredMixin):
    model = Press
    fields = ['name', 'series_number', 'manufacture_date', 'width', 'manufacturer', 'length', 'manual']
    success_url = reverse_lazy('manage_press_list')

class OwnerPressEditMixin(OwnerPressMixin, OwnerEditMixin):
    template_name = 'connectors/manage/press/form.html'

class ManagePressListView(OwnerPressMixin, ListView):
    model = Press
    template_name = 'connectors/manage/press/list.html'
    permission_required = 'connectors.view_press'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)
    
class PressCreateView(OwnerPressEditMixin, CreateView):
    permission_required = 'connectors.add_press'
    

class PressUpdateView(OwnerPressEditMixin, UpdateView):
    permission_required = 'connectors.change_press'
    

class PressDeleteView(OwnerPressMixin, DeleteView):
    template_name = 'connectors/manage/press/delete.html'
    permission_required = 'connectors.delete_press'


#SPLICE

class OwnerSpliceMixin(OwnerMixin, LoginRequiredMixin, PermissionRequiredMixin):
    model = Splice
    fields = ['conveyor_machine', 'belt_type', 'press', 'photo', 'angle', 'angle_length', 'length', 'slevel_op', 'slevel_mag', 'time', 'temperature', 'pressure']
    success_url = reverse_lazy('manage_splice_list')

class OwnerSpliceEditMixin(OwnerSpliceMixin, OwnerEditMixin):
    template_name = 'connectors/manage/splice/form.html'

class ManageSpliceListView(OwnerSpliceMixin, ListView):
    model = Splice
    template_name = 'connectors/manage/splice/list.html'
    permission_required = 'connectors.view_splice'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)
    
class SpliceCreateView(OwnerSpliceEditMixin, CreateView):
    permission_required = 'connectors.add_splice'
    

class SpliceUpdateView(OwnerSpliceEditMixin, UpdateView):
    permission_required = 'connectors.change_splice'
    

class SpliceDeleteView(OwnerSpliceMixin, DeleteView):
    template_name = 'connectors/manage/splice/delete.html'
    permission_required = 'connectors.delete_splice'