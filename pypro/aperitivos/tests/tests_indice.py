import pytest
from django.urls import reverse

from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:indice'))


def test_status_code(resp):
    assert resp.status_code == 200

@pytest.mark.parametrize(
    'titulo',
    [
        'Video Aperitivo: Motivação',
        'Instalação Windows'
    ]
)
def test_titulo_video(resp, titulo):
    assert_contains(resp, titulo)
#
#
# def test_conteudo_video(resp):
#     assert_contains(resp, '<div class="mb-4" style="padding:56.25% 0 0 0;position:relative;">'
#                           '<iframe src="https://player.vimeo.com/video/600249135?badge=0&amp;autopause='
#                           '0&amp;player_id=0&amp;app_id=58479&amp;h=9513c7690d" frameborder="0" allow="autoplay; fullscreen; '
#                           'picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;" '
#                           'title="AULA 01 - MOTIVA&amp;Ccedil;&amp;Atilde;O &amp;mdash; Curso de Python Gr&amp;aacute;tis.mp4"></iframe>'
#                           '</div><script src="https://player.vimeo.com/api/player.js"></script>')
