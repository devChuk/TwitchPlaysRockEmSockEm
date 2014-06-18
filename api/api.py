from flask import Flask, render_template, jsonify, request
import pymongo

app = Flask(__name__)

@app.route("/api",methods=['GET'])
def api():
    if request.method == 'GET':
        json_results=[]
        #db_data=pymongo.MongoClient().twitchdb.twitchcollect.find_one({'twitch':'yes'})
        d={
           # 'commands':db_data['commands']
            'commands':[(1,'a'),(2,'b'),(3,'c'),(4,'d')]
            }
        json_results.append(d)
        
    return jsonify(items=json_results)

if __name__=='__main__':
    app.debug=True
    app.run()
    """host='0.0.0.0',port=22222"""
