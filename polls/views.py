from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.conf import settings
from django.db.models import Count
from . models import PollsType, Polls
from read_statistics.utils import read_statistics_once_read
from django.contrib.contenttypes.models import ContentType


each_page_polls_number = 8

# Create your views here.
def get_polls_list_common_data(request, polls_all_list):
    paginator=Paginator(polls_all_list, each_page_polls_number) #每2页进行分页
    page_num=request.GET.get('page', 1) #获取url的页面参数(GET请求)
    page_of_polls=paginator.get_page(page_num)
    currentr_page_num=page_of_polls.number #获取当前页码
    page_range=list(range(max(currentr_page_num -2, 1), currentr_page_num)) + \
               list(range(currentr_page_num, min(currentr_page_num + 2,paginator.num_pages) + 1))

    # 加上省略页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 加上首页和尾页
    if page_range[0] !=1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)
    
    #获取日期归档对应的数量
    polls_dates=Polls.objects.dates('created_time', 'month', order="ASC")
    polls_dates_dict= {}
    for polls_date in polls_dates:
        polls_count=Polls.objects.filter(created_time__year=polls_date.year,\
        created_time__month=polls_date.month).count()
        polls_dates_dict[polls_date]= polls_count
 
    context={}
    context['pollss']=page_of_polls.object_list
    context['page_of_polls']=page_of_polls
    context['page_range']=page_range
    context['polls_types']=PollsType.objects.annotate(polls_count=Count('polls'))   #获取单个分类  #获取博客分类的对应博客数量 方案二
    context['poll_dates']=polls_dates_dict  #DESC OR ASC #获取日期归档对应的数量 方案一
    return context

def polls_list(request):
    polls_all_list=Polls.objects.all()
    context=get_polls_list_common_data(request, polls_all_list)
    return render(request,'polls/polls_list.html', context)

def polls_with_type(request, polls_type_id):
    polls_type=get_object_or_404(PollsType, pk=polls_type_id)
    polls_all_list=Polls.objects.filter(polls_type=polls_type)
    context=get_polls_list_common_data(request, polls_all_list)
    # context=['polls_type']=polls_type
    return render(request,'polls/polls_with_type.html', context)

def polls_with_date(request, year, month):
    polls_all_list=Polls.objects.filter(created_time__year=year, created_time__month=month)
    context=get_polls_list_common_data(request, polls_all_list)
    context['polls_with_date']='%s年%s月' % (year, month)
    return render(request,'polls/polls_with_date.html', context)

def polls_detail(request, polls_id):
    polls=get_object_or_404(Polls, pk=polls_id)
    read_cookie_key=read_statistics_once_read(request, polls)  
    
    context={}   
    context['previous_polls']=Polls.objects.filter(created_time__gt=polls.created_time).first()
    context['next_polls']=Polls.objects.filter(created_time__lt=polls.created_time).last()
    context['polls']=polls
    response=render(request,'polls/polls_detail.html', context) #响应
    response.set_cookie(read_cookie_key, 'true')
    return response

