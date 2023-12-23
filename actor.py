import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

doc = [{
  "name": "沈安妮",
  "birth": "2001",
  "role": "靜宜大學資管系學生"
},{"name": "王淨",
  "birth": "1998",
  "role": "公正黨文宣部黨工"
  },{"name": "黃健瑋",
  "birth": "1981",
  "role": "公正黨文宣部主任"
},{
  "name": "謝盈萱",
  "birth": "1979",
  "role": "公正黨文宣部副主任兼發言人"
},{
  "name": "戴立忍",
  "birth": "1966",
  "role": "民和黨籍現任立法院院長"
}]

doc_ref = db.collection("人選之人演員名單").document("anni0921")
doc_ref.set(doc)
