#!/usr/bin/env python

# WS server example that synchronizes state across clients
# https://websockets.readthedocs.io/en/stable/intro.html

import asyncio
import json
import logging
import ssl
import websockets
import time


logging.basicConfig()

#
PORT = 8081
HOST = '0.0.0.0'
#
clientes = set()


async def handle_client(websocket, path):
   # Aqui separaremos as rotas pelo path
    if path == '/chat':
        await handle_chat(websocket)
    elif path == '/metadata':
        await handle_metadata(websocket)

async def handle_metadata(websocket):
   # Envia quantas pessoas estão online
    while True:
        print(len(clientes))
        views = len(clientes);
        # await websocket.send(f"{views}")
        time.sleep(10)

async def handle_chat(websocket):
    try:
        clientes.add(websocket)
        print(len(clientes))
        while True:
            # Receive a message from the client
            logging.info(clientes)  # will not print anything
            message = await websocket.recv()
            
            # Broadcast the message to all connected clients
            for client in clientes:
                await client.send(message)
                
    finally: 
        clientes.remove(websocket)    

# Start server
start_server = websockets.serve(handle_client, HOST, PORT)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
