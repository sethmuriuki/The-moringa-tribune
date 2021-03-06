from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from . models import Articles,NewsLetterRecipients
from .forms import NewsLetterForm ,NewArticleForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.
def welcome(request):
    # return HttpResponse('Welcome to Moringa Tribune')
    return render (request, 'welcome.html')

def news_today(request):
    date = dt.date.today()
    news = Articles.todays_news()
    form = NewsLetterForm()
       
    return render(request, 'all-news/today-news.html', {"date": date,"news":news, "letterForm":form})

def newsletter(request):
    name = request.POST.get('your_name')
    email = request.POST.get('email')

    recipient = NewsLetterRecipients(name = name, email = email) #object from the form to retrieve name and email
    recipient.save()
    send_welcome_email(name,email)

    data = {'success': 'You have been successfully added to mailing list'}
    return JsonResponse(data)



def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day


def past_days_news(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_today)

    news = Articles.days_news(date)

    return render(request, 'all-news/past-news.html', {"date": date,"news": news})

@login_required(login_url = '/accounts/login/')
def article(request,article_id):
    try:
        articles = Articles.objects.get(id = article_id)

    except DoesNotExist:
        raise Htpp404()

    return render(request,"all-news/article.html", {"article":article})

def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Articles.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def new_article(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.editor = current_user
            article.save()
    else:
        form = NewArticleForm()
    return render(request, 'new_article.html', {"form": form})