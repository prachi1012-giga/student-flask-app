from flask import Flask 
app=Flask(_name_)

@app.route("/")
defhome():
 return"Hello!Application deployed automatically."

if_name_=="_main_":
app.run(host-"0.0.0.0",port=5000)