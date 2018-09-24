import requests
import codecs


def main():
    with open('id.dat', 'r') as id_file:
        v0_data = id_file.readline()
    req = requests.Request('POST', 'http://dd.hasmodai.com/backend16/login_sorath.php',
                           files={'name': (None, 'sorath'), 'v0': (None, codecs.decode(v0_data, 'hex'))}).prepare()
    res = requests.session().send(req)
    print(res.content)
    pass


if __name__ == '__main__':
    main()
