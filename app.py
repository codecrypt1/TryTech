from fastapi import FastAPI, Form, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from datetime import datetime

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456789",
    database="dora"
)
mycursor = mydb.cursor()

good_thing={}
bad_thing={}
dates={"2023-11-01":4,"2023-11-05":2,"2023-11-11":5, "2023-11-12":4}
logined=2

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/reg")
def reg(
    username: str = Form(...),
    password: str = Form(...),
): 
    global good_thing, bad_thing
    good_thing={}
    bad_thing={}
    global logined
    result = "INSERT INTO user_main (username, password) VALUES (%s,%s)" 
    userpass = [(username, password)]
    mycursor.executemany(result, userpass)
    mydb.commit()
    mycursor.execute("SELECT * FROM user_main")
    myresult = mycursor.fetchall()
    for x in myresult:
        if x[1]==username and x[2]==password:
            logined=x[0]
    return RedirectResponse(url="/home")

@app.post("/login")
def login(
    username: str = Form(...),
    password: str = Form(...),
):
    global good_thing, bad_thing
    good_thing={}
    bad_thing={}
    global logined
    mycursor.execute("SELECT * FROM user_main")
    myresult = mycursor.fetchall()
    for x in myresult:
        if x[1]==username and x[2]==password:
            logined=x[0]
            return RedirectResponse(url="/window")
    # Simple authentication logic
    return {"message": "Login failed"}

@app.get("/logout")
def logout(request: Request):
    global logined
    logined=0
    return RedirectResponse(url="/")

@app.route("/home", methods=["GET", "POST"])
def home(request: Request):
    return templates.TemplateResponse("user_page.html", {"request": request, "good": good_thing, "bad": bad_thing})


@app.route("/window", methods=["GET", "POST"])
def window(request: Request):
    mycursor.execute(f"SELECT * FROM good_main where id={logined}")
    myresult = mycursor.fetchall()
    for x in myresult:
        good_thing[x[1]]=x[2]
    mycursor.execute(f"SELECT * FROM bad_main where id={logined}")
    myresult = mycursor.fetchall()
    for x in myresult:
        bad_thing[x[1]]=x[2]
    return templates.TemplateResponse("home.html", {"request": request, "good": good_thing, "bad": bad_thing, "dates": dates})

@app.post("/add")
def add(request: Request, gpara: str = Form(...), bpara: str = Form(...)):
    gthing=gpara.split(',')
    bthing=bpara.split(',')
    result = "INSERT INTO good_main (id, habits, state) VALUES (%s,%s,%s)" 
    print(logined)
    userpass = [(logined,goodthing, 1 ) for goodthing in gthing]
    mycursor.executemany(result, userpass)
    bresult = "INSERT INTO bad_main (id, bhabits, state) VALUES (%s,%s,%s)"
    userpass = [(logined,badthing, 1 ) for badthing in bthing]
    mycursor.executemany(bresult, userpass)
    mydb.commit()

    mycursor.execute(f"SELECT * FROM good_main where id={logined}")
    myresult = mycursor.fetchall()
    for x in myresult:
        good_thing[x[1]]=x[2]
    mycursor.execute(f"SELECT * FROM bad_main where id={logined}")
    myresult = mycursor.fetchall()
    for x in myresult:
        bad_thing[x[1]]=x[2]
    return templates.TemplateResponse("home.html", {"request": request, "good": good_thing, "bad": bad_thing, "dates": dates})

@app.post("/delete")
def delete(request: Request,key: str = Form(...)):
    current_datetime = datetime.now()
    formatted_date = current_datetime.strftime("%Y-%m-%d")
    id_value = logined
    name_value = key

    # Select the row by ID and Name
    select_query = "SELECT * FROM good_main WHERE id = %s AND habits = %s"
    mycursor.execute(select_query, (id_value, name_value))
    selected_row = mycursor.fetchone()
    if selected_row:
        # Display the selected row
        print("Selected Row:", selected_row)

        if selected_row[2] == 0:
            status = 1
        else:
            status = 0
        update_query = f"UPDATE good_main SET state = {status} WHERE id = %s AND habits = %s"
        mycursor.execute(update_query, (id_value, name_value))
        mydb.commit()

        print("Row updated successfully.")
    else:
        print("Row not found.")
    select_query = "SELECT * FROM bad_main WHERE id = %s AND bhabits = %s"
    mycursor.execute(select_query, (id_value, name_value))
    selected_row = mycursor.fetchone()
    if selected_row:
        # Display the selected row
        print("Selected Row:", selected_row)

        if selected_row[2] == 0:
            status = 1
        else:
            status = 0
        update_query = f"UPDATE bad_main SET state = {status} WHERE id = %s AND bhabits = %s"
        mycursor.execute(update_query, (id_value, name_value))
        mydb.commit()
        
    if formatted_date not in dates:
        dates[formatted_date]=0
    if key in good_thing:
        if good_thing[key]==1:
            good_thing[key]=0
            dates[formatted_date]+=1
        else:
            good_thing[key]=1
            dates[formatted_date]-=1
    if key in bad_thing:
        if bad_thing[key]==1:
            bad_thing[key]=0
            dates[formatted_date]-=1
        else:
            bad_thing[key]=1
            dates[formatted_date]+=1
    print(dates[formatted_date])
    return templates.TemplateResponse("home.html", {"request": request, "good": good_thing, "bad": bad_thing, "dates": dates})
#1
