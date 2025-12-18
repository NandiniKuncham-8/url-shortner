from fastapi import FastAPI,HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import string
from database import connect,cursor
app=FastAPI()
BASE62=string.digits+string.ascii_letters
def encode_BASE62(num:int)->str:
    if num==0:
        return BASE62[0]
    result=[]
    while num>0:
        result.append(BASE62[num%62])
        num//=62
    return ''.join(reversed(result))
class URLRequest(BaseModel):
    long_url:str
@app.post("/shorten")
def shorten_url(request:URLRequest):
    cursor.execute("SELECT short_code from urls WHERE long_url=?",(request.long_url,))
    row=cursor.fetchone()
    if row:
        short_code=row[0]
    else:
        cursor.execute("INSERT INTO urls (long_url, short_code) VALUES (?, '')", (request.long_url,))
        connect.commit()
        url_id = cursor.lastrowid
        short_code = encode_BASE62(url_id)
        cursor.execute("UPDATE urls SET short_code = ? WHERE id = ?", (short_code, url_id))
        connect.commit()
    return {
        "short_url": f"http://localhost:8000/{short_code}",
        "long_url": request.long_url
    }
@app.get("/{short_code}")
def redirect_url(short_code:str):
    cursor.execute("SELECT long_url FROM urls WHERE short_code = ?", (short_code,))
    row = cursor.fetchone()
    if row:
        return RedirectResponse(row[0])
    else:
        raise HTTPException(status_code=404, detail="URL not found")
