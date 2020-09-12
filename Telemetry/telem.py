#import flask
import os
import zipfile
import time
from flask import Flask, send_file, request, abort, jsonify, send_from_directory




UPLOAD_DIRECTORY = os.getcwd()+"/Files"
CUR_DIRECTORY = os.getcwd();

app = Flask(__name__)

#Endpoint to list folders on the server.
@app.route('/', methods=['GET'])
def home():
    files = []
    s = "<html>";
    for filename in os.listdir(CUR_DIRECTORY):
        path = os.path.join(CUR_DIRECTORY, filename)
        if os.path.isdir(path):
            s += "<a href = /dl?filename=" + filename +">" + filename + "</a>\t"
    s+="</html>"
    return s;



#Zips and downloads file "filename" in the get request to the client
@app.route("/dl", methods=['GET'])
def list_files():
    name = request.args.get('filename', '')
    zipf = zipfile.ZipFile('Name.zip','w', zipfile.ZIP_DEFLATED)
    for root,dirs, files in os.walk(name):
        for file in files:
            zipf.write(name+"/"+file)
    zipf.close()
    return send_file("Name.zip", as_attachment=True);


"""
print("here")
def parse_data(can):
    SingleCanFrame = can.Message
    print(SingleCanFrame)
    f = open(CUR_DIRECTORY+"/hi/data.txt","a")
    #s = str(SingleCanFrame)
    f.write("hi")
    f.close()
"""
"""def test_listener():
    print("HERE")"""



app.run(host='0.0.0.0')


