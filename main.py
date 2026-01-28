from fastapi import FastAPI, UploadFile, File
import subprocess
import tempfile
import os

app = FastAPI(title="GDAL Service")

@app.post("/inspect")
async def inspect(file: UploadFile = File(...)):
    with tempfile.TemporaryDirectory() as tmp:
        file_path = os.path.join(tmp, file.filename)

        with open(file_path, "wb") as f:
            f.write(await file.read())

        try:
            result = subprocess.run(
                ["ogrinfo", file_path],
                capture_output=True,
                text=True,
                check=True
            )

            return {
                "success": True,
                "output": result.stdout
            }

        except subprocess.CalledProcessError as e:
            return {
                "success": False,
                "error": e.stderr
            }
