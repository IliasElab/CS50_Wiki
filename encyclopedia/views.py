from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from markdown2 import markdown

from . import util
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    entry = util.get_entry(title)
    if entry is not None:
        return render(request, "encyclopedia/entry.html", {
            "entry": markdown(entry),
            "title": title.capitalize()
        })
    else:
        return render(request, "encyclopedia/error.html",{
            "name": "No entry has been found for {}".format(title)
        })

def search(request):
    if request.method == "POST":
        entry = util.get_entry(request.POST["title"])
        if entry is not None:
            return render(request, "encyclopedia/entry.html", {
                "entry": markdown(entry),
                "title": request.POST["title"]
            })
        else:
            entries = util.list_entries()
            results = []
            for entry in entries:
                if request.POST["title"].lower() in entry.lower():
                    results.append(entry)

            return render(request, "encyclopedia/search.html", {
                "results": results
            })

def create(request):
    if request.method == "POST":
        entries = util.list_entries()
        if request.POST["newtitle"] in entries:
            return render(request, "encyclopedia/error.html",{
                "name": "Impossible to create {} Page, it already exists".format(request.POST["newtitle"])
            })
        else:
            with open("entries\{}.md".format(request.POST["newtitle"]), "x") as f:
                f.write(request.POST["newcontent"])

            entry = util.get_entry(request.POST["newtitle"])

            return render(request, "encyclopedia/entry.html", {
                "entry": markdown(entry),
                "title": request.POST["newtitle"]
            })


    else:
        return render(request, "encyclopedia/create.html")

def edit(request, title):
    if request.method == "POST":
        with open("entries\{}.md".format(title), "w") as f:
            f.write(request.POST["editcontent"])

        entry = util.get_entry(title)

        return render(request, "encyclopedia/entry.html", {
            "entry": markdown(entry),
            "title": title
        })

    else:
        entry = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "entry": entry,
            "title": title.capitalize()
        })

def chance(request):
    entries = util.list_entries()
    rand = random.choice(entries)

    entry = util.get_entry(rand)
    return render(request, "encyclopedia/entry.html", {
        "entry": markdown(entry),
        "title": rand
    })