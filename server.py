import asyncio
from websockets.server import serve

CLIENTS=set()

async def handler(websocket):
    CLIENTS.add(websocket)
    async for message in websocket:
        print("connected clients:", len(CLIENTS))
        print(message)
        for client in CLIENTS.copy():
            try:
                await client.send(message)
            except:
                CLIENTS.remove(client)

async def main():
    async with serve(handler, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())
