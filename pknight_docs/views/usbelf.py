import os
import markdown
from django.shortcuts import render

from my_application import settings
settings.BASE_DIR
md_file_path = os.path.join(settings.BASE_DIR, 'pknight_docs/static/pknight_docs/md_projects/usbelf/usbelf.md')
def usbelf_doc(request):
    with open(md_file_path, 'r') as f:
        content = f.read()
        md_html = markdown.markdown(content)
        print(md_html)
    return render(request, 'usbelf_doc.html', {'md_html': md_html})
