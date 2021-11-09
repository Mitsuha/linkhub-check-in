import requests
import os

host = 'https://linkhub.asia'

proxies = {
    'http': os.environ.get('HTTP_PROXY'),
    'https': os.environ.get('HTTPS_PROXY'),
}

if __name__ == '__main__':
    env = os.environ
    if env.get('ACCOUNT_EMAIL') == '' or env.get('ACCOUNT_PASSWORD') == '':
        print('Please enter your email address')
        exit(1)

    for i in range(5):
        try:
            response = requests.post(host + '/auth/login', data={
                'email': env.get('ACCOUNT_EMAIL'),
                'passwd': env.get('ACCOUNT_PASSWORD')
            }, timeout=10, proxies=proxies)

            content = response.json()

            if content['ret'] == 0:
                print('Error: Login failed ' + str(content))
                exit(1)

            cookie = response.cookies

            response = requests.post(
                host + '/user/checkin', cookies=cookie, timeout=10, proxies=proxies)

            print(response.json()['msg'])

            break
        except Exception as e:
            print(e)
            continue
