from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    django_template= {

        'proverb' : ['Time','and','tide','wait', 'for', 'none'],
        'birthday' : datetime.datetime.now(),
        'val' : '',
        'num' : 56 ,
        'numList' : [1,2,3,4],
        'cap' : 'django',
        'strCut' : 'Python is awesome.',
        'strCut1' : 'Python - is - awesome',
        'sort' : [
            {'name' : 'labib', 'age' : 16},
            {'name' : 'sabbir', 'age' : 14},
            {'name' : 'abir', 'age' : 10}
        ],
        'Escape' : '<p>This <em>should be</em> fun!</p>',
        'list' : ['jone', 'joe', 'adam'],
        'leng' : ['jone', 'joe', 'adam'],
        'lengt' : 'ahdjfjdf',
        'linenum' : "cat dog horse",
        'lowercase' : 'HeLlO  I  Am',
        'uppercase' : 'HeLlO  i  Am',
        'titlefi' : 'I LOvE doGs',
        'ran' : ['jone', 'joe', 'adam', 'fafu' , 'lepa', 'lalu'],
        'slicelist' : ['jone', 'joe', 'adam', 'fafu' , 'lepa', 'lalu'],
        'timefi' : datetime.datetime(2022,2,12,4,0,0),
        'mydate' : datetime.datetime(2021, 1, 1, 12, 0, 0),
        'brief' : 'You can do a lot of modifications with template filters',
        'scrip' : '<b>I</b> <button>love</button> <span>dogs</span>' ,
        'makeList' : 'Hello'


    }
    
    return render(request, 'index.html', django_template)
    