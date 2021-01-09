from aip import AipOcr
""" 你的 APPID AK SK """
APP_ID = '23520145'
API_KEY = 'rk0fp2z7GEO7GWVBoI97CI0Z'
SECRET_KEY = 'xLvGyvgAfGW4RYPRm0SbpmCTfqW4Z15W'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
def ImageRead(path):
    image = get_file_content(path)
    result = str(client.basicGeneral(image)['words_result'][0]['words'])
    where = result[result.index('到') + 1:result.index('的')]
    location = result[result.index('[') + 1:result.index(']')]
    x, y = location.split(',')
    return where, x, y