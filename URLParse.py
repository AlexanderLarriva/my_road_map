from urllib.parse import urlparse
a = urlparse("scheme://netloc/path;parameters?query#fragment")
print(a)
print(type(a))
print(a[2])

o = urlparse("http://docs.python.org:80/3/library/urllib.parse.html?"
             "highlight=params#url-parsing")
print(o)
# o.scheme
print(o.scheme)
# o.netloc
print(o.netloc)
# o.hostname
print(o.hostname)
# o.port
print(o.port)
# o._replace(fragment="").geturl()
print(o._replace(fragment="").geturl())


from urllib.parse import urlparse, urlunparse, ParseResult

def make(url):
    return urlparse(url)

def get_scheme(data):
    return data.scheme

def set_scheme(data, scheme):
    return data._replace(scheme=scheme)

def get_host(data):
    return data.hostname

def set_host(data, host):
    return data._replace(netloc=host, hostname=host)

def get_path(data):
    return data.path

def set_path(data, path):
    return data._replace(path=path)

def get_query_param(data, param_name, default=None):
    params = urlparse.parse_qs(data.query)
    return params.get(param_name, [default])[0]

def set_query_param(data, key, value):
    params = urlparse.parse_qs(data.query)
    if value is None:
        del params[key]
    else:
        params[key] = value
    return data._replace(query=urlencode(params, doseq=True))

def to_string(data):
    return urlunparse(data)