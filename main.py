from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import requests
app = Flask(__name__, template_folder='templates', static_url_path='/static', static_folder='static')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}


@app.route('/', methods=['POST'])
def home():
    response = requests.get("https://www.gismeteo.kz/weather-astana-5164/", headers=headers)
    text1 = response.text
    sep1 = '<div class="date">Сейчас</div>'
    text2 = text1.split(sep=sep1)[1]
    sep2 = '</div></div><svg class'
    arr3 = text2.split(sep=sep2)
    text3 = arr3[0]
    sep3 = 'class="unit unit_temperature_c">'
    text4 = text3.split(sep=sep3)[-2::]
    sep4 = '</span>'
    arr = []
    for i in text4:
        arr.append(i.split(sep=sep4)[0].replace("&minus;", "-"))


    response = requests.get("https://www.gismeteo.kz/weather-almaty-airport-14397/", headers=headers)
    atext1 = response.text
    asep1 = '<div class="date">Сейчас</div>'
    atext2 = atext1.split(sep=asep1)[1]
    asep2 = '</div></div><svg class'
    aarr3 = atext2.split(sep=asep2)
    atext3 = aarr3[0]
    asep3 = 'class="unit unit_temperature_c">'
    atext4 = atext3.split(sep=asep3)[-2::]
    asep4 = '</span>'
    massive = []
    for i in text4:
        massive.append(i.split(sep=asep4)[0].replace("&minus;", "-"))

    massive[0], massive[1] = "День: " + massive[1], "Ночь: " + massive[0]

    arr[0], arr[1] = "День: " + arr[1], "Ночь: " + arr[0]
    #city: str = Form()
    #print(city)
   # city = request.get("city", None)
    if request.form == 'POST':
        weather = request.form['cities']
        if weather == 'Astana':
            print(arr)
        elif weather == 'Аlmaty':
            print(massive)

    return render_template("home.html", text=weather)

#@app.route('/astana')
#def astana():
  #  response = requests.get("https://www.gismeteo.kz/weather-astana-5164/", headers=headers)
   # text1 = response.text
  #  sep1 = '<div class="date">Сейчас</div>'
   # text2 = text1.split(sep=sep1)[1]
   # sep2 = '</div></div><svg class'
   # arr3 = text2.split(sep=sep2)
   # text3 = arr3[0]
   # sep3 = 'class="unit unit_temperature_c">'
   # text4 = text3.split(sep=sep3)[-2::]
   # sep4 = '</span>'
  #  arr = []
   # for i in text4:
   #     arr.append(i.split(sep=sep4)[0].replace("&minus;", "-"))

 #   arr[0], arr[1] = "День: " + arr[1], "Ночь: " + arr[0]
  #  return render_template("astana.html", text=arr)

#@app.route('/almaty')
#def almaty():
 #   response = requests.get("https://www.gismeteo.kz/weather-almaty-airport-14397/", headers=headers)
   # atext1 = response.text
  #  asep1 = '<div class="date">Сейчас</div>'
   # atext2 = atext1.split(sep=asep1)[1]
  #  asep2 = '</div></div><svg class'
  #  aarr3 = atext2.split(sep=asep2)
  #  atext3 = aarr3[0]
  #  asep3 = 'class="unit unit_temperature_c">'
   # atext4 = atext3.split(sep=asep3)[-2::]
    #asep4 = '</span>'
   # massive = []
  #  for i in text4:
      #  arr.append(i.split(sep=asep4)[0].replace("&minus;", "-"))

   # massive[0], massive[1] = "День: " + massive[1], "Ночь: " + massive[0]

   # return render_template("almaty.html", text=masssive)