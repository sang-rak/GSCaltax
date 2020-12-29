# _*_ coding: utf-8 _*_
from flask import Flask, render_template, request

from keras.models import model_from_json
import pandas as pd
import numpy as np


app = Flask(__name__)

# model load

json_file = open("./model/model.json", "r")
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

# model weight load
loaded_model.load_weights("./model/model_weight.h5")


json_file2 = open("./model/model2.json", "r")
loaded_model_json2 = json_file2.read()
json_file2.close()
loaded_model2 = model_from_json(loaded_model_json2)

# model weight load
loaded_model2.load_weights("./model/model_weight2.h5")


json_file3 = open("./model/model3.json", "r")
loaded_model_json3 = json_file3.read()
json_file3.close()
loaded_model3 = model_from_json(loaded_model_json3)

# model weight load
loaded_model3.load_weights("./model/model_weight3.h5")


json_file4 = open("./model/model4.json", "r")
loaded_model_json4 = json_file4.read()
json_file4.close()
loaded_model4 = model_from_json(loaded_model_json4)

# model weight load
loaded_model4.load_weights("./model/model_weight4.h5")


json_file5 = open("./model/model5.json", "r")
loaded_model_json5 = json_file5.read()
json_file5.close()
loaded_model5 = model_from_json(loaded_model_json5)

# model weight load
loaded_model5.load_weights("./model/model_weight5.h5")


json_file6 = open("./model/model6.json", "r")
loaded_model_json6 = json_file6.read()
json_file6.close()
loaded_model6 = model_from_json(loaded_model_json6)

# model weight load
loaded_model6.load_weights("./model/model_weight6.h5")


json_file7 = open("./model/model7.json", "r")
loaded_model_json7 = json_file7.read()
json_file7.close()
loaded_model7 = model_from_json(loaded_model_json7)

# model weight load
loaded_model7.load_weights("./model/model_weight7.h5")





@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method =='GET':
        return render_template("index.html")
    if request.method =='POST':


        avg_temp = float(request.form['avg_temp'])
        avg_temp2 = float(request.form['avg_temp2'])
        avg_temp3 = float(request.form['avg_temp3'])
        avg_temp4 = float(request.form['avg_temp4'])
        avg_temp5 = float(request.form['avg_temp5'])
        avg_temp6 = float(request.form['avg_temp6'])
        avg_temp7 = float(request.form['avg_temp7'])
        avg_temp8 = float(request.form['avg_temp8'])
        avg_temp9 = float(request.form['avg_temp9'])
        avg_temp10 = float(request.form['avg_temp10'])
        avg_temp11 = float(request.form['avg_temp11'])
        avg_temp12 = float(request.form['avg_temp12'])
        avg_temp13 = float(request.form['avg_temp13'])
        avg_temp14 = float(request.form['avg_temp14'])
        avg_temp15 = float(request.form['avg_temp15'])
        avg_temp16 = float(request.form['avg_temp16'])
        avg_temp17 = float(request.form['avg_temp17'])
        avg_temp18 = float(request.form['avg_temp18'])
        avg_temp19 = float(request.form['avg_temp19'])
        avg_temp20 = float(request.form['avg_temp20'])
        avg_temp21 = float(request.form['avg_temp21'])
        avg_temp22 = float(request.form['avg_temp22'])
        avg_temp23 = float(request.form['avg_temp23'])
        avg_temp24 = float(request.form['avg_temp24'])
        avg_temp25 = float(request.form['avg_temp25'])
        avg_temp26 = float(request.form['avg_temp26'])
        avg_temp27 = float(request.form['avg_temp27'])
        avg_temp28 = float(request.form['avg_temp28'])
        avg_temp29 = float(request.form['avg_temp29'])
        avg_temp30 = float(request.form['avg_temp30'])
        avg_temp31 = float(request.form['avg_temp31'])
        avg_temp32 = float(request.form['avg_temp32'])
        avg_temp33 = float(request.form['avg_temp33'])
        avg_temp34 = float(request.form['avg_temp34'])
        avg_temp35 = float(request.form['avg_temp35'])
        avg_temp36 = float(request.form['avg_temp36'])
        avg_temp37 = float(request.form['avg_temp37'])
        avg_temp38 = float(request.form['avg_temp38'])
        avg_temp39 = float(request.form['avg_temp39'])
        avg_temp40 = float(request.form['avg_temp40'])
        avg_temp41 = float(request.form['avg_temp41'])

        min_temp = float(request.form['min_temp'])
        min_temp2 = float(request.form['min_temp2'])
        min_temp3 = float(request.form['min_temp3'])
        min_temp4 = float(request.form['min_temp4'])
        min_temp5 = float(request.form['min_temp5'])
        min_temp6 = float(request.form['min_temp6'])
        min_temp7 = float(request.form['min_temp7'])
        min_temp8 = float(request.form['min_temp8'])
        min_temp9 = float(request.form['min_temp9'])
        min_temp10 = float(request.form['min_temp10'])
        min_temp11 = float(request.form['min_temp11'])
        min_temp12 = float(request.form['min_temp12'])
        min_temp13 = float(request.form['min_temp13'])
        min_temp14 = float(request.form['min_temp14'])
        min_temp15 = float(request.form['min_temp15'])
        min_temp16 = float(request.form['min_temp16'])
        min_temp17 = float(request.form['min_temp17'])
        min_temp18 = float(request.form['min_temp18'])

        max_temp = float(request.form['max_temp'])
        max_temp2 = float(request.form['max_temp2'])
        max_temp3 = float(request.form['max_temp3'])
        max_temp4 = float(request.form['max_temp4'])
        max_temp5 = float(request.form['max_temp5'])
        max_temp6 = float(request.form['max_temp6'])
        max_temp7 = float(request.form['max_temp7'])
        max_temp8 = float(request.form['max_temp8'])
        max_temp9 = float(request.form['max_temp9'])
        max_temp10 = float(request.form['max_temp10'])
        max_temp11 = float(request.form['max_temp11'])
        max_temp12 = float(request.form['max_temp12'])
        max_temp13 = float(request.form['max_temp13'])
        max_temp14 = float(request.form['max_temp14'])
        max_temp15 = float(request.form['max_temp15'])
        max_temp16 = float(request.form['max_temp16'])
        max_temp17 = float(request.form['max_temp17'])
        max_temp18 = float(request.form['max_temp18'])
        max_temp19 = float(request.form['max_temp19'])
        max_temp20 = float(request.form['max_temp20'])
        max_temp21 = float(request.form['max_temp21'])
        max_temp22 = float(request.form['max_temp22'])

        rain_fall = float(request.form['rain_fall'])
        rain_fall2 = float(request.form['rain_fall2'])
        rain_fall3 = float(request.form['rain_fall3'])
        rain_fall4 = float(request.form['rain_fall4'])
        rain_fall5 = float(request.form['rain_fall5'])
        rain_fall6 = float(request.form['rain_fall6'])
        rain_fall7 = float(request.form['rain_fall7'])
        rain_fall8 = float(request.form['rain_fall8'])
        rain_fall9 = float(request.form['rain_fall9'])

    price = 0

    data = [[avg_temp,avg_temp2, avg_temp3,avg_temp4,avg_temp5,avg_temp6,avg_temp7,avg_temp8,avg_temp9,avg_temp10,
             avg_temp11,avg_temp12,avg_temp13,avg_temp14,avg_temp15,avg_temp16,avg_temp17,avg_temp18,avg_temp19,avg_temp20,
             avg_temp21,avg_temp22,avg_temp23,avg_temp24,avg_temp25,avg_temp26,avg_temp27,avg_temp28,avg_temp29,avg_temp30,
             avg_temp31,avg_temp32,avg_temp33,avg_temp34,avg_temp35,avg_temp36,avg_temp37,avg_temp38,avg_temp39,avg_temp40,
             avg_temp41,

             min_temp,min_temp2,min_temp3,min_temp4,min_temp5,min_temp6,min_temp7,min_temp8,min_temp9,min_temp10,
             min_temp11,min_temp12,min_temp13,min_temp14,min_temp15,min_temp16,min_temp17,min_temp18,

             max_temp,max_temp2,max_temp3,max_temp4,max_temp5,max_temp6,max_temp7,max_temp8,max_temp9,max_temp10,
             max_temp11,max_temp12,max_temp13,max_temp14,max_temp15,max_temp16,max_temp17,max_temp18,max_temp19,max_temp20,
             max_temp21,max_temp22,

             rain_fall,rain_fall2,rain_fall3,rain_fall4,rain_fall5,rain_fall6,rain_fall7,rain_fall8,rain_fall9], ]
    data = pd.DataFrame(data)
    data = data / 100
    # 스퀘어 처리
    density_result = np.square(loaded_model.predict(data))
    density_result = density_result[0]
    density_result = density_result[0]
    # 로그 처리
    FM_result = np.exp(loaded_model2.predict(data))
    FM_result = FM_result[0]
    FM_result = FM_result[0]
    FS_result = np.exp(loaded_model3.predict(data))
    FS_result = FS_result[0]
    FS_result = FS_result[0]
    HDT_result = np.exp(loaded_model4.predict(data))
    HDT_result = HDT_result[0]
    HDT_result = HDT_result[0]
    # 스퀘어 처리
    IZOD_result = np.square(loaded_model5.predict(data))
    IZOD_result = IZOD_result[0]
    IZOD_result = IZOD_result[0]
    # 로그 처리
    MI_result = np.exp(loaded_model6.predict(data))
    MI_result = MI_result[0]
    MI_result = MI_result[0]
    TS_result = np.exp(loaded_model7.predict(data))
    TS_result = TS_result[0]
    TS_result = TS_result[0]

    price = "비중"
    price_1 = density_result
    price2 = "굴곡탄성률"
    price2_1 = FM_result
    price3 = "굴곡강도"
    price3_1 = FS_result
    price4 = "HDT"
    price4_1 = HDT_result
    price5 = "IZOD 충격강도"
    price5_1 = IZOD_result
    price6 = "MI"
    price6_1 = MI_result
    price7 = "인장강도"
    price7_1 = TS_result

    return render_template('index.html',
                           price=price,
                           price_1=price_1,
                           price2=price2,
                           price2_1=price2_1,
                           price3=price3,
                           price3_1=price3_1,
                           price4=price4,
                           price4_1=price4_1,
                           price5=price5,
                           price5_1=price5_1,
                           price6=price6,
                           price6_1=price6_1,
                           price7=price7,
                           price7_1=price7_1)

if __name__=='__main__':
    app.run(debug=True)