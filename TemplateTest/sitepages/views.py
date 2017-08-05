from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader





def home_page(request):
    return render(request,"landing_page/home.html",
                  {"home": "Home",
                   "home_p": "Fantastic Portfolio Website Designs for Inspiration. Selection of Awwwards winning portfolio websites."})


def contact_page(request):
    return render(request,"landing_page/content.html",
                  { "contact":"Contact",
                    "contact_p":"40 Locks Yard, Headcorn, Ashford, Kent, UK ,Tn279AD"
                  })

def about_page(request):
    return render(request,"landing_page/about.html",
                  { "about":"About",
                    "about_p":"Following the latest update of portfolio builder Cargo, we round up the 10 best portfolio websites artists designers to showcase their work. Behance. Adobe Portfolio."

                  })
