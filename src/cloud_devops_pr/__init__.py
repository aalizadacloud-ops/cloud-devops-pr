import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Cloud DevOps CI/CD - test version (demo)", "version": "0.1.0"}


@app.get("/health")
def health():
    return {"status": "healthy"}


def main():
    uvicorn.run("cloud_devops_pr:app", host="0.0.0.0", port=8000)
