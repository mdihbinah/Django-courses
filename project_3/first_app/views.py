from django.shortcuts import render

# Create your views here.
# 'list' : ['python','is','best.'] , 'birthday' : datetime.datetime.now(),
def home(request):
    d = {'author' : 'Rahim', 'age' : 15 ,  'val': '    ','courses':
         [
             {
                'id': 1,
                'name' : 'Python',
                'fee' : 5000
             },

             {
                'id': 2,
                'name' : 'Djanogo',
                'fee' : 1000
             },

             {
                'id': 3,
                'name' : 'C',
                'fee' : 5000
             }

         ]
          }
    return render(request, 'home.html',d)

