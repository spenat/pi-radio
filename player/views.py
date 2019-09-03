from django.shortcuts import render
from player.models import Channel
from player.forms import ChannelForm
import subprocess as sp


proc = False

def index(request):
    context = {
        'channel_list': Channel.objects.all()
    }
    return render(request, 'player/index.html', context)

def add_channel(request):
    if request.method == 'GET':
        context = {
            'channel_form': ChannelForm()
        }
        return render(request, 'player/addChannel.html', context)
    elif request.method == 'POST':
        new_channel_form = ChannelForm(request.POST)
        if new_channel_form.is_valid():
            new_channel_form.save()
        return render(request, 'player/index.html', {'channel_list': Channel.objects.all()})

def play_channel(request):
    global proc
    if request.method == 'POST':
        if proc:
            proc.terminate()
        url = request.POST['url']
        name = request.POST['name']
        command_list = ['mplayer', url]
        proc = sp.Popen(command_list)
        context = {
            'current_channel': name,
            'current_url': url
        }
        return render(request, 'player/playing.html', context)
    else:
        return render(request, 'player/index.html', {'channel_list': Channel.objects.all()})

def stop_music(request):
    global proc
    if proc:
        proc.terminate()
    return render(request, 'player/index.html', {'channel_list': Channel.objects.all()})

