import shutil
import os
import time
import calendar
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

directorio="files"

@app.post("/uploadfile")
async def create_upload_file(file: UploadFile):
    current_GMT = time.gmtime()
    ts = calendar.timegm(current_GMT)
    file_location = f"{directorio}/{ts}-{file.filename}"
    try:
        os.mkdir(directorio)
    except:
        pass
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)    
    return {"info": f"file '{file.filename}' salvado en '{file_location}'"}
