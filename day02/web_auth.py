import requests

def main():
    auth = ('test','12345')
    response = requests.get('http://192.168.199.107', auth = auth)
    print(response.text)
    # urllib2 泪奔...

if __name__ == '__main__':
    main()