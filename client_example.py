# -*- coding: utf-8 -*-

from suds.client import Client

import urlparse, urllib, os

url = urlparse.urljoin('file:', urllib.pathname2url(os.path.abspath("ClientEInvoiceServices-2.0.wsdl")))

web_client = Client(url=url)

print web_client