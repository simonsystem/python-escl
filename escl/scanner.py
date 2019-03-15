from requests import Session
from xmltodict import unparse
from urlparse import urlsplit, urlunsplit

MM = 1 / 25.4
INCH = 1
SIZES = {
    'a4': (210 * MM, 297 * MM),
    'letter': (8.5 * INCH, 11 * INCH),
}

class Scanner(Session):
    def __init__(self, url=None, username='admin', password=False, verify=False, cert=False, **kwargs):
        Session.__init__(self, **kwargs)
        self.url = url
        self.resolution = 300
        self.size = 'a4'
        self.compression = 35
        self.brightness = 1000
        self.contrast = 1000
        self.color_mode = 'RGB24'
        self.document_format_ext = 'application/pdf'
        self.username = username
        self.password = password
        self.verify = verify
        self.cert = cert

    def scan(self, url=None, username=None, password=None, resolution=None, size=None, compression=None, brightness=None, contrast=None, color_mode=None, document_format_ext=None, **kwargs):
        if url is None: url = self.url
        if resolution is None: resolution = self.resolution
        if size is None: size = self.size
        if compression is None: compression = self.compression
        if brightness is None: brightness = self.brightness
        if contrast is None: contrast = self.contrast
        if color_mode is None: color_mode = self.color_mode
        if document_format_ext is None: document_format_ext = self.document_format_ext
        if username is None: username = self.username
        if password is None: password = self.password

        data = unparse({
          'scan:ScanSettings': {
            '@xmlns:scan': 'http://schemas.hp.com/imaging/escl/2011/05/03',
            '@xmlns:copy': 'http://www.hp.com/schemas/imaging/con/copy/2008/07/07',
            '@xmlns:dd': 'http://www.hp.com/schemas/imaging/con/dictionaries/1.0/',
            '@xmlns:dd3': 'http://www.hp.com/schemas/imaging/con/dictionaries/2009/04/06',
            '@xmlns:fw': 'http://www.hp.com/schemas/imaging/con/firewall/2011/01/05',
            '@xmlns:scc': 'http://schemas.hp.com/imaging/escl/2011/05/03',
            '@xmlns:pwg': 'http://www.pwg.org/schemas/2010/12/sm',
            'pwg:Version': '2.1',
            'scan:Intent': 'Document',
            'pwg:ScanRegions': {
              'pwg:ScanRegion': {
                'pwg:Height': int(SIZES[size][0] * resolution),
                'pwg:Width': int(SIZES[size][1] * resolution),
                'pwg:XOffset': '0',
                'pwg:YOffset': '0',
              },
            },
            'pwg:InputSource': 'Platen',
            'scan:DocumentFormatExt': document_format_ext,
            'scan:XResolution': resolution,
            'scan:YResolution': resolution,
            'scan:ColorMode': color_mode,
            'scan:CompressionFactor': compression,
            'scan:Brightness': brightness,
            'scan:Contrast': contrast,
          },
        })
        auth = (username, password) if password else None
        response = self.post(url + '/eSCL/ScanJobs', auth=auth, data=data, allow_redirects=False, **kwargs)
        location = urlunsplit(urlsplit(url)[:2] + urlsplit(response.headers['Location'])[2:])
        return self.get(location + '/NextDocument', auth=auth, **kwargs)
