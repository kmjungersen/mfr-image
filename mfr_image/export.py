# -*- coding: utf-8 -*-
""" exporter module."""
from PIL import Image
from cStringIO import StringIO


def export_gif(fp):
    im = Image.open(fp)
    sio = StringIO()
    im.save(sio, format='gif')
    return sio.getvalue(), '.gif'

def export_tiff(fp):
    im = Image.open(fp)
    sio = StringIO()
    im.save(sio, format='tiff')
    return sio.getvalue(), '.tiff'