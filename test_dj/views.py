from django.shortcuts import render
from django.db import transaction
# Create your views here.
from django.http import HttpResponse

from test_dj.models import User,Poll,Choice
from django.shortcuts import render_to_response

from django.views import generic 

@transaction.atomic
def atomic(request,save=False):
    
    try:
        for o in User.objects.all():
            o.delete()
    except:
        pass
    error=False
    user1=User(name="deen")
    user2=User(name="deen")
    
    user3=User(name='root1')
    user4=User(name='root2')
    
    '''
    this is test atomic
    '''
    
    try:
        with transaction.atomic():
           
            user1.save()
            
            '''this is wrong as root has exist'''
            user2.save()
    except Exception,e:
        error=True
        print e
    
    
    '''
    this is another test of savepoint
    '''
    
    try:
        user3.save()
    except:
        pass
    sid=transaction.savepoint()
    
    try:
        user4.save()
    except:
        pass
    
    
    if save:
        #save both user3 and user4
        transaction.savepoint_commit(sid)
    else:
        #don not save user4
        transaction.savepoint_rollback(sid)
        
        
    #spt=transaction.savepoint()
    #if save==False:
        #print 'save point false'
        #transaction.savepoint_rollback(spt)    
    return HttpResponse("atomic response Error="+str(error))




## the generic views test here 
    

def index(request):
    latest_poll_list=Poll.objects.order_by('-pub_date')[:5]
    return render_to_response('test_dj/index.html',{'latest_poll_list':latest_poll_list})
class IndexView(generic.ListView):       
    template_name='test_dj/index.html'
    content_object_name='latest_poll_list'
    def get_queryset(self):
        objs=Poll.objects.order_by('-pub_date')[:2]
        for obj in objs:
            print obj.question,obj.pub_date
        return Poll.objects.order_by('-pub_date')[:2]
    
class DetailView(generic.DetailView):
    model=Poll
    template_name='test_dj/detail.html' 