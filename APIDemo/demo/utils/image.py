# -*- coding: UTF-8 -*-
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse


class ImageStorage(FileSystemStorage):
    from django.conf import settings

    def __init__(self,
                 location=settings.MEDIA_ROOT,
                 base_url=settings.MEDIA_URL):
        #init
        super(ImageStorage, self).__init__(location, base_url)

    #rewrite _save
    def _save(self, name, content):
        import os, time
        print("Name Content:::", name, content)
        #extension name
        ext = os.path.splitext(name)[1]  #[0] name ; [1] extention
        #original path+name
        source_name = os.path.splitext(name)[0]
        #original name
        org_name = os.path.splitext(content.name)[0]
        # file path
        d = os.path.dirname(name)
        # define file name: date+org name
        fn = time.strftime('%Y%m%d%H%M%S')
        fn = fn + '_' + org_name
        # new name
        name = os.path.join(d, fn + ext)
        # call father functhion
        return super(ImageStorage, self)._save(name, content)
