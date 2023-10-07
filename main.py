import os

from discord.ext import ipcx
from dotenv import load_dotenv
from quart import Quart, Response, redirect, url_for

load_dotenv()

IPC_SECRET_KEY = os.environ["IPC_SECRET_KEY"]

app = Quart(__name__)
ipc_client = ipcx.Client(secret_key=IPC_SECRET_KEY)


@app.route("/")
async def main():
    return redirect(url_for("/ping"))


@app.route("/ping")
async def ping():
    res = await ipc_client.request("healthcheck")
    status_code = 200 if res is True else 500
    return Response(str(res), status=status_code)
