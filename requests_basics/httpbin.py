import requests

# get with params
r = requests.get('https://httpbin.org/get', params = dict(page=2, count=15, name="rahul kumar"))

print(r.url)
print(r.text)



# a simple POST request
r = requests.post('https://httpbin.org/post', data = dict(user='rahul kumar kandula', password = 'testing'))
ret_data_dict = r.json()
print(type(ret_data_dict))
print(ret_data_dict)



# a basic BASIC authentication request
r = requests.get('https://httpbin.org/basic-auth/rahul/admin', auth=('rahul', 'admin'), timeout=2)
print(r.text)
