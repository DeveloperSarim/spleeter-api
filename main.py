from fastapi import FastAPI, UploadFile, File
import subprocess
import tempfile
import os

app = FastAPI()

@app.post("/separate")
async def separate_audio(file: UploadFile = File(...)):
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tmp.write(await file.read())
    tmp.close()

    output_dir = tempfile.mkdtemp()
    cmd = ["spleeter", "separate", "-i", tmp.name, "-o", output_dir]
    subprocess.run(cmd)

    return {"output_dir": output_dir}
