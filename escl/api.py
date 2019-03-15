from .scanner import Scanner

def scan(url, **kwargs):
    with Scanner() as scanner:
        return scanner.scan(url, **kwargs)
