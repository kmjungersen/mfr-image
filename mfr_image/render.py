"""Image rendering module"""

import os

import logging
logging.basicConfig(level=logging.DEBUG)

def render_html(fp, *args, **kwargs):
    url = kwargs['url']
    img = '''
        <img src='%s' id='target'/>
        ''' % (url)
    return img

