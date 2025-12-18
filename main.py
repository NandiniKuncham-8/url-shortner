from fastapi import FastAPI,HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import string
app=FastAPI()
BASE62=string.digits+string.ascii_letters
url_store={}
counter=1
def encode_BASE62(num:int)->str:
    if num==0:
        return BASE62[0]
    result=[]
    while num>0:
        result.append(BASE62[num%62])
        num//=62
    return " ".join(reversed(result))
class URLRequest(BaseModel):
    long_url:str
@app.post("/shorten")
def shorten_url(request:URLRequest):
    global counter
    short_code=encode_BASE62(counter)
    url_store[short_code]=request.long_url
    counter+=1
    return {
        "short_url": f"http://localhost:8000/{short_code}",
        "long_url": request.long_url
    }
@app.get("/{short_code}")
def redirect_url(short_code:str):
    if short_code not in url_store:
        raise HTTPException(status_code=404,detail="URL Not Found")
    return RedirectResponse(url_store[short_code])
