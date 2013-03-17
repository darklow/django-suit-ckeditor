# from django.core.serializers import json
from django.forms import Textarea
from django.utils.safestring import mark_safe

try:
    import json
except ImportError:
    import django.utils.simplejson as json


class CKEditorWidget(Textarea):
    class Media:
        css = {
            'all': ('suit-ckeditor/ckeditor.css',)
        }
        js = ('suit-ckeditor/ckeditor/ckeditor.js',)

    def __init__(self, attrs=None, editor_options=None):
        super(CKEditorWidget, self).__init__(attrs)
        self.editor_options = editor_options or {}


    def render(self, name, value, attrs=None):
        output = super(CKEditorWidget, self).render(name, value, attrs)
        output += mark_safe(
            '<script type="text/javascript">CKEDITOR.replace("%s", %s);</script>'
            % (name, json.dumps(self.editor_options)))
        return output
