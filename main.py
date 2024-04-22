from fastapi import FastAPI,Response
import rc
from starlette.responses import HTMLResponse
# from fastapi.responses import responses
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/divination/yi")
async def rc_yi():
    content = rc.rc_r()
    response = Response(content, media_type="text/plain")
    response.headers["Cache-Control"] = "no-store"
    return response

# print(rc.rc_r())


@app.get("/divination/yihtml")
# async def rc_yi():
#     reped_text=rc.rc_r().replace('\n', '<br />')
#     return reped_text
async def rc_yi():
    # return rc.rc_r()
    return  HTMLResponse(rc.rc_r(), status_code=200)

# print(rc.rc_r())





