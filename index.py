from flask import Flask,render_template,request
from datetime import datetime
import firebase_admin

from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")

firebase_admin.initialize_app(cred)

app = Flask(__name__)

@app.route("/")
def index():
   homepage = "<h1>沈安妮Python網頁</h1>"
   homepage += "<a href=/mis>MIS</a><br>"
   homepage += "<a href=/today>顯示日期時間</a><br>"
   homepage += "<a href=/welcome?nick=tcyang>傳送使用者暱稱</a><br>"
   homepage += "<a href=/about>安妮簡介網頁</a><br>"

   homepage += "<a href=/allbooks>全部图书</a><br>"
   homepage += "<a href=/about>根据书名关键字查询图书</a><br>"

   return homepage

@app.route("/mis")
def course():
   return "<h1>資訊管理導論</h1>"

@app.route("/today")
def today():
   now = datetime.now()
   return render_template("today.html", datetime = str(now))

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
   user = request.values.get("nick")
   return render_template("welcome.html", name=user)

@app.route("/account", methods=["GET", "POST"])
def account():
   if request.method == "POST":
      user = request.form["user"]
      pwd = request.form["pwd"]
      result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd
      return result
   else:
      return render_template("account.html")

@app.route("/allbooks")
def allbooks():
   db = firestore.client()
   doc_ref = db.document("圖書精選")
   doc = doc_ref.get()
   result = doc.to_dict()
   return result

if __name__ == "__main__":
   app.run()