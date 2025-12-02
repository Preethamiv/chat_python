# server.py
import asyncio
import websockets
import json

connected_clients = set()

async def handler(websocket):
    print("✅ A user connected")
    connected_clients.add(websocket)

    try:
        async for message in websocket:
            print("📩 Received:", message)
            # Broadcast to all connected clients
            await asyncio.gather(*(client.send(message) for client in connected_clients))
    except:
        pass
    finally:
        print("❌ A user disconnected")
        connected_clients.remove(websocket)

async def main():
    async with websockets.serve(handler, "localhost", 3000):
        print("🚀 WebSocket Python server running on ws://localhost:3000")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
