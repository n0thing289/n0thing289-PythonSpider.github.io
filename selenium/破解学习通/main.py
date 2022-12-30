import json

def insert_kv(cookie):
    my_keys = ['domain','httpOnly','name','path','secure','value']
    source_dict ={
        'domain': cookie.get('domain'),
        'httpOnly': cookie.get('httpOnly'),
        'name': cookie.get('name'),
        'path': '/',
        'secure': cookie.get('secure'),
        'value': cookie.get('value'),
        # 'HostOnly': False,
    }
    k, v = "expiry", cookie.get('expiry')
    my_keys.insert(my_keys.index('domain') + 1, k)
    source_dict[k] = v
    new_dict = {}
    for k in my_keys:
        new_dict.update({k: source_dict[k]})
    return new_dict


with open('xxt_cookies.txt', 'r', encoding='UTF-8') as f:
    listCookies = json.loads(f.read())

for cookie in listCookies:
    print("\n===" + str(cookie) + "===")
    if not cookie.get('expiry'):
        cookie_dict = {
            'domain': cookie.get('domain'),
            'httpOnly': cookie.get('httpOnly'),
            'name': cookie.get('name'),
            'path': '/',
            'secure': cookie.get('secure'),
            'value': cookie.get('value'),
            # 'HostOnly': False,
        }
        print(cookie_dict)
    else:
        print(insert_kv(cookie))