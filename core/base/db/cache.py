import os
database = '/usr/share/blest-framework'
core = '/usr/share/blest-framework/src/data'
modules = core+'/modules'
banners = core+'/core/base/banners/banner.py'

class cache:
    def generate(self):
        try:
            if os.path.exists(database+'/files/cache'):
                pass
            else:
                os.mkdir(database+'/files/cache')
        except:
            pass