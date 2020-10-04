from flask import Flask, jsonify, request, url_for, redirect, session, render_template, g,sessions
from elasticapm.contrib.flask import ElasticAPM
from elasticapm.handlers.logging import LoggingHandler
import requests
from flask.templating import render_template
import hashlib
import redis
import json
import time



app = Flask(__name__)
apm = ElasticAPM(app, server_url='http://0.0.0.0:8200', service_name='flask', logging=True)




rediss = redis.Redis('localhost')
rediss.flushdb()



def checkWithRedis(word,wordHash):
    userObject=rediss.get(wordHash)
    if userObject is not None:
        data_fetch = json.loads(userObject)
        return (data_fetch["definition"],'linear-gradient(to right, #ff9900, #ff9966)')
    else:
        apiReturnedObj=searchInAPI(word)
        try:
            translation=apiReturnedObj["definitions"][0]["definition"]
        except:
            translation="Can't find any translation"
        myobj = {}
        myobj['word'] = word
        myobj['definition'] = translation
        rediss.set(wordHash, json.dumps(myobj))
        return (json.dumps(myobj['definition']),'linear-gradient(to right, #00b09b, #96c93d)')
    


def searchInAPI(yourWord):
    token="8da4e0d5b6995a13620460201a10f887e3824ea8"
    headers = { 'Authorization' : 'Token ' + token }
    serachContent=yourWord
    urls=f"https://owlbot.info/api/v4/dictionary/{serachContent}"
    response = requests.get(urls, headers=headers,verify=False)
    if response.status_code==200:
        return response.json()
    else:
        return response.json()


@app.route('/',methods=['POST','GET'])
def login():
    return render_template('search.html')


@app.route('/findtheword',methods=['POST','GET'])
def findtheword():
   
    userWord = request.args.get('userword')
    wordHash=int(hashlib.sha256(userWord.encode('utf-8')).hexdigest(), 16) % 10**8
    outData=checkWithRedis(userWord,wordHash)
   
    return jsonify ({'code': '1', 'message' : str(outData[0])  ,
                        'noticetype':outData[1] }),200
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

    # return jsonify({"message": "response ok"}), 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)