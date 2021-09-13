from flask import Flask, render_template
from flask import Flask, request, jsonify
import os
from flask import send_from_directory
from keras.models import load_model
from keras.preprocessing import image
import numpy as np

app = Flask(__name__)
dic = {0 : '三杯雞', 1 : '什錦炒麵',2:"咖哩雞",3:"塔香海茸",4:"大陸妹",5:"客家小炒",6:"小番茄",7:"有機小松菜",8:"有機青松菜",9:"木瓜",
        10:"柳丁",11:"棗子",12:"橘子",13:"沙茶肉片",14:"油菜",15:"洋蔥炒蛋",16:"滷蛋",17:"滷雞腿",18:"玉米炒蛋",19:"瓜仔肉",
        20:"番茄炒蛋",21:"白米飯",22:"白菜滷",23:"福山萵苣",24:"空心菜",25:"糖醋雞丁",26:"紅蘿蔔炒蛋",27:"義大利麵",28:"芥藍菜",29:"菠菜",
        30:"葡萄",31:"蒜泥白肉",32:"蒸蛋",33:"蓮霧",34:"螞蟻上樹",35:"西瓜",36:"豆芽菜",37:"關東煮",38:"青江菜",39:"香蕉",40:"香酥魚排",
        41:"馬鈴薯燉肉",42:"高麗菜",43:"鳳梨'",44:"鵝白菜",45:"鹽酥雞",46:"麥克雞塊",47:"麻婆豆腐",48:"麻油雞",49:"黑胡椒豬柳"}

model = load_model('model.h5')

def predict_label(img_path):
    i = image.load_img(img_path, target_size=(224,224))
    #i = image.img_to_array(i)/255.0
	#i = i.reshape(None,224,224,3)
    #i = np.expand_dims(i,axis=0)
    i  = np.expand_dims( i , axis = 0) 
    p = model.predict(i)[0]
    top = p.argsort()[::-1][:5]
    return dic[top[0]]

@app.route('/', methods=['GET', 'POST'])
def main():
        return  render_template('index.html')

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']

		img_path = "static/" + img.filename	
		img.save(img_path)

		p = predict_label(img_path)
	return render_template("index.html", prediction = p, img_path = img_path)

if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug=True)






"""如果不用render_template跑得出來
def main():
        return '''
        <!doctype html>
        <head>
            <title>Upload new File</title>
        </head>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
        <p><input type=file name=image>
        <input type=submit value=Upload>
        </form>
        '''
"""




