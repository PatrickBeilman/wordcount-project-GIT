from django.http import HttpResponse
from django.shortcuts import render
import operator




def home(request):
        return render(request, 'home.html', {'seggs': 'narc',
                                             'eat': 'im the king of the world',
                                             'ate': "6250",
                                             'welcome': "welcome traveler, please enter your text below"})
def count(request):

        fulltext = request.GET['fulltext']
        wordlist = fulltext.split()
        wrdcntdict = {}

        for word in wordlist:
                if word in wrdcntdict:
                        wrdcntdict[word] += 1
                else:
                        wrdcntdict[word] = 1
        worddictsort = sorted(wrdcntdict.items(), key = operator.itemgetter(1), reverse = True)       
        return render(request,'count.html',{'fulltext': fulltext,
                                            'length': len(wordlist),
                                            'dict': worddictsort})

def about(request):
        return render(request, 'about.html')

def secret(request):
        return render(request, 'secret.html')


#dead code
'''#def eggs(request):
#        return HttpResponse("THE WORLD SHALL TASTE MY EGGS!!!!")

#def new(request):
#        return HttpResponse('<h1> remeber what they took from you </h1>')
'''
