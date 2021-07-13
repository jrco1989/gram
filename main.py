import requests
import json
if __name__ == '__main__':
    url='https://datos.gov.co/'
    #url2='http://httpbin.org/get?name=jr&age=99'
    url2='http://httpbin.org/get'
    url_post='http://httpbin.org/post'
    args ={'status':'activate'}
    payload ={'status':'activate'}
    headers ={'Content-Type':'application/json',
              'access-token':'fsdfsd'}#le iindicamos al servidor que estamos enviando datos en formato jsaon  
    response = requests.get(url2, params=args)
    response_post = requests.post(url_post, json=payload)
    response_post2 = requests.post(url_post, data=payload)
    response_post3 = requests.post(url_post, data=json.dumps(payload), headers=headers)#serializando el diccionario
    #print(response)

if response.status_code ==200:
    #print(response.content)
    content = response.content
    data_json = response.json()
    print(content)
    print('*****************')
    print(data_json['args'])
    print('*****************')
    response_json = json.loads(response.text)
    print(response_json['origin'])

    """file = open('dp.html', 'wb') #wb escritura binaria
    file.write(content)
    file.close()"""

if response_post.status_code ==200:
    print('///////////////')
    print(response_post.content)
    print(response_post2.content)
    print(response_post3.content)
    headers_response3 = response_post3.headers#read response of the server
    print(headers_response3)