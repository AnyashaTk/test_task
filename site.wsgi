import os, sys
activate_this = '/home/username/python/bin/activate_this.py'
with open(activate_this) as f:
   exec(f.read(), {'__file__': activate_this})
sys.path.insert(0, os.path.join('/home/username/domains/domain.ru/public_html/'))
from myapp import app as application
DirectoryIndex site.wsgi
Options +ExecCGI
AddHandler wsgi-script .wsgi
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ /site.wsgi/$1 [QSA,PT,L]

if __name__ == "__main__":
    application.run()