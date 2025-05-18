from fastapi import FastApi


app = FastApi()

@app.get("/hotels")
def get_hotels():
    return "owihuiqhduq"
