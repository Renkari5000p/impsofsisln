import requests
import shutil 

class Llamadasinternet():
    def primer_request(self):
        url = 'https://github.com/'
        r = requests.get('https://github.com/')
        print(r )
        print(r.content)
        print(r.status_code)
    def imagen(self, url, file_name):

        res = requests.get(url,stream = True)
        if 200==res.status_code:
            with open(file_name, 'wb')as f:
                shutil.copyfileobj(res.raw, f)
            print('imagen descargada corectamente')
        else:
            print('No se encontro la imagen')

    def clima(self, city, api_key):
        base_url= 'https://api.openweathermap.org/data/2.5/weather?'
        params = {'q':city, 'appid':api_key,'units':'metric'}
        try:
            r = requests.get(base_url, params=params)
            r.raise_for_status()

            weather_data = r.json()
            if 200==weather_data['cod']:
                print(f'El clima en{weather_data['name']}:')
                print(f'Descripcion{weather_data['weather'][0]['description']}')
                print(f'Temperatura{weather_data['main']['temp']}°c')
                print(f'Humedad{weather_data['main']['humidity']}%')
                print(f'Viento{weather_data['wind']['speed']}m/s')
        except:
            print('error')    
url = "https://thenaturalhistorian.com/wp-content/uploads/2023/01/image-14.png"
req = Llamadasinternet()
req.primer_request()
req.imagen(url, "WALL-E.png")
api_key = '69ec8ca2037d63a120d31c59efd0f604'
city = 'Zapopan'
req.clima(city, api_key)