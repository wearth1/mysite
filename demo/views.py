import datetime
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect
from django.utils import timezone
from django.db.models import Sum
from django.core.cache import cache
from read_statistics.utils import get_seven_days_read_data, get_today_hot_data, get_yesterday_hot_data
from polls.models import Polls
from django.urls import reverse





def get_seven_day_hot_data():
    today=timezone.now().date()
    date=today - datetime.timedelta(days=7)
    polls=Polls.objects.filter(read_details__date__lt=today, read_details__date__gte=date)\
                       .values('id', 'title')\
                       .annotate(read_num_sum=Sum('read_details__read_num'))\
                       .order_by('read_num_sum')
    return polls[:7]

def home(request):
    polls_content_type = ContentType.objects.get_for_model(Polls)
    dates, read_nums = get_seven_days_read_data(polls_content_type)

    #获取7天热门博客的缓存数据
    seven_day_hot_data = cache.get('seven_day_hot_data')
    if seven_day_hot_data is None:
        seven_day_hot_data=get_seven_day_hot_data()
        cache.set('seven_day_hot_data', seven_day_hot_data, 0)
        print('calc')
    else:
        print('use cache')

    context = {}
    context['dates']= dates
    context['read_nums'] = read_nums
    context['today_hot_data'] = get_today_hot_data(polls_content_type)
    context['yesterday_hot_data'] = get_yesterday_hot_data(polls_content_type)
    context['seven_day_hot_data'] = seven_day_hot_data
    return render(request, 'home.html', context)




