cache = {}


def get_data_from_server(url):
    return url


def get_page(url):

    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data

print(get_page("google"))
print(get_page("bing"))
print(get_page("google"))
print(cache)
