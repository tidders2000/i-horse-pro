from django.shortcuts import render, reverse, redirect, get_object_or_404, HttpResponseRedirect
from training.models import CustomImages
from .forms import *
from django_ical.views import ICalFeed
from django.db.models import Q
from training.models import TrainingLog
from horse.models import Horse
from django.core.paginator import Paginator
from django.contrib import messages
from datetime import datetime
from datetime import date
import calendar
from django.contrib import messages
from training.models import Disipline


#allows users to find and add competitions
def competition(request):
    user = request.user
    comps =CompetitionLog.objects.all().filter(user=user).count()
    #limits competition entry for free members
    if user.profile.membership=="Free" and comps >=5:
         messages.error(request, 'Maximum reached') 
         return redirect('home')
  
    #gets list of disiplines update model in admin to add more
    customImg = Disipline.objects.all()
     #paginates query return for comps
    comps = CompetitionLog.objects.all().filter(user=user).order_by('-date')
    paginator = Paginator(comps, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

#process search request from user
 
    if request.method == "POST":
        keyword = request.POST.get('keyword')
        comps = CompetitionLog.objects.filter(
            Q(location__icontains=keyword)  | Q(date__icontains=keyword) | Q(disipline__icontains=keyword))
        paginator = Paginator(comps, 10)
        page_obj = paginator.get_page(page_number)
       
        

        


    return render(request, 'comp.html', {'customImg': customImg, 'page_obj': page_obj})

#saves competition record from competition then redirects to the edit screen
def comp_create(request, pk):
      
  #gets the disipline from model list
    Dis = get_object_or_404(Disipline, pk=pk)
    form = comp_form()
    
    user = request.user
    sessionSave = form.save(commit=False)
    sessionSave.disipline = Dis
    sessionSave.user = user

    sessionSave.save()
  

    return redirect(reverse('comp_edit', kwargs={'pk': sessionSave.pk}))


def comp_edit(request, pk):

    session = get_object_or_404(CompetitionLog, pk=pk)
    # checks a competition has been created then shows it
    if not session.location:
       show=False
    else:
     show=True
    user = request.user

    form = comp_form(instance=session)
    entry = entry_form()
    entry.fields["horse"].queryset = Horse.objects.filter(user=request.user)
    entries = Comphorse.objects.all().filter(competition=session)
    #post request for entry picking up on saveentry move to view when can
    if request.method == 'POST':

        if 'save_entry' in request.POST:
            ent = entry_form(request.POST)
            if ent.is_valid():

                newObj = ent.save(commit=False)
                newObj.user = user
                newObj.competition = session
                newObj.save()

                messages.error(request, "Entry Added")

                return redirect(reverse('comp_edit', kwargs={'pk': session.pk}) + '#entries')
            else:
                messages.error(request, "Sorry cannot save")
                return redirect(reverse('comp_edit', kwargs={'pk': session.pk}))

  #post request for competition move to view when can
        if 'save_log' in request.POST:

            log = comp_form(
                request.POST, request.FILES, instance=session)
            if log.is_valid():
                log.save()
                
                messages.error(request, "Competition Saved")
  #redirects back to competiton
                url = '/competing/comp_edit/{}'.format(session.pk)
                return redirect(url)
            else:
                 messages.error(request, "Sorry cannot save")
                 return redirect(url)



    return render(request, 'cedit.html', {'show':show, 'entry': entry, 'form': form, 'session': session, 'entries': entries})

#adds ics comp needs to be dry on job
class EventFeed2(ICalFeed):
    """
    A simple event calender
    """
    product_id = '-//example.com//Example//EN'
    timezone = 'UTC'
    file_name = "comp.ics"

    def __call__(self, request, *args, **kwargs):
        self.user = request.user
        self.pk = kwargs['pk']
        return super(EventFeed2, self).__call__(request, *args, **kwargs)
        print(self.user)

    def items(self):
    #    (user=self.user).order_by('-date')
       
        return CompetitionLog.objects.filter(pk=self.pk)

    def item_guid(self, item):
        return "{}{}".format(item.id, "global_name")

    def item_title(self, item):

        return "{}".format(item.location)

    # def item_description(self, item):
    #     return item.notes

    def item_start_datetime(self, item):
        return item.date

    def item_link(self, item):
        return "http://www.i-horse.co.uk"




#once a comp has been created an entry can be added and editied with this view
def editentry(request, pk):
    instance = get_object_or_404(Comphorse, pk=pk)
    comp = instance.competition.pk

    form = entry_form(instance=instance)
    if request.method == 'POST':
        entry = entry_form(request.POST, instance=instance)
        entry.save()
        return redirect('comp_edit', pk=comp)

    return render(request, 'editentry.html', {'form': form, 'comp': comp})
