from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': 600249135},
        'instalacao-windows': {'titulo': 'Instalação Windows', 'vimeo_id': 251497688},
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
