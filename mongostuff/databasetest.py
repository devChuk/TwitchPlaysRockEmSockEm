import pymongo
from pymongo import MongoClient


client = MongoClient()
db = client['test-database']
#The thing is that MongoDB does not like documents which grow, like chat pages. 
#MongoDB always stores documents in a contiguous section in the database files. This makes reading much simpler and faster, 
#because no seeking on the hard-drive needs to be done to read a single document.

#That means when a document grows so large that it would overlap the space of 
#the next document in the file, that document needs to be removed and new hard-drive 
#space needs to be allocated to store it. This is an expensive operation. When your documents 
#grow all the time, this will happen very frequently and write-performance will suffer.

#So which would be faster, having two documents for each robot or one large document for both robots?
#If we have two documents, writing will probably be slower than reading. If we have one, reading will be slower than writing.
#Long story short, we're probably going to have lag with Python no matter what happens. Better to have two documents so 
#programming the reading code will be easier.

#There will be two documents. Each document is for each robot.
#For now, just making one document.
chat = {"text": "blah"}

chats = db.chats
chat_id = chats.insert(chat)
str(chat_id)

db.collection_names()