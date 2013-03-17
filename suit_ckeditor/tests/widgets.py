from django.test import TestCase
from suit_ckeditor.widgets import CKEditorWidget
from django.contrib.admin.templatetags.admin_static import static


class WidgetsTestCase(TestCase):
    def test_CKEditorWidget(self):
        widget = CKEditorWidget()
        self.assertEqual({}, widget.editor_options)

    def test_CKEditorWidget_with_editor_options(self):
        options = {'iframe': True}
        widget = CKEditorWidget(editor_options=options)
        self.assertEqual(options, widget.editor_options)


    def test_CKEditorWidget_output(self):
        widget = CKEditorWidget()
        name = 'body'
        value = '123'
        output = widget.render(name, value)
        self.assertHTMLEqual(output, (
            '<textarea cols="40" name="%s" rows="10">%s</textarea><script '
            'type="text/javascript">CKEDITOR.replace("%s", {});</script>' % (
                name, value, name)))

    def test_CKEditorWidget_output_with_editor_options(self):
        widget = CKEditorWidget(editor_options={'iframe': True})
        name = 'body'
        value = '123'
        output = widget.render(name, value)
        self.assertHTMLEqual(output, (
            '<textarea cols="40" name="%s" rows="10">%s</textarea><script '
            'type="text/javascript">CKEDITOR.replace("%s", {"iframe": '
            'true});</script>' % (
                name, value, name)))

    def test_CKEditorWidget_media(self):
        widget = CKEditorWidget()
        js_url = static(widget.Media.js[0])
        css_url = static(widget.Media.css['all'][0])
        self.assertHTMLEqual(str(widget.media),
                             '<link href="%s" media="all" rel="stylesheet" '
                             'type="text/css" /><script src="%s" '
                             'type="text/javascript" />'
                             % (css_url, js_url))
