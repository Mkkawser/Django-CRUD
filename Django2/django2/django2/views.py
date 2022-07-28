from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from CRUD.forms import CrudForm

from CRUD.models import crudDB


def HomePage(req):
    ob = CrudForm()
    if req.method == 'POST':
        ob = CrudForm(req.POST)
        if ob.is_valid():
            ob.save()
            return HttpResponseRedirect('/')
    dic = {
        'value': crudDB.objects.all()
    }
    return render(req, 'index.html', dic)


def update(req, id):
    si = crudDB.objects.get(pk=id)
    ob = CrudForm(req.POST, instance=si)
    if req.method == 'POST':
        ob = CrudForm(req.POST, instance=si)
        if ob.is_valid():
            ob.save()
            print('save')
            return HttpResponseRedirect('/')
    dic = {
        'val': crudDB.objects.get(pk=id)
    }
    return render(req, 'update.html', dic)


def delete(req, id):
    ob = crudDB.objects.get(pk=id)
    ob.delete()
    return HttpResponseRedirect('/')
