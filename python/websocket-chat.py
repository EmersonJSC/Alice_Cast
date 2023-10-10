#!/usr/bin/env python

# WS server example that synchronizes state across clients
# https://websockets.readthedocs.io/en/stable/intro.html

import asyncio
import json
import logging
import ssl
import websockets

logging.basicConfig()
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG) 

clientes = set()

async def handle_connection(websocket, path):
   # Add the websocket to a list of connected clients
    clientes.add(websocket)
   

    try:
        while True:
            # Receive a message from the client
            logging.info(websocket.recv())  # will not print anything
            message = await websocket.recv()

            # Broadcast the message to all connected clients
            for client in clientes:
                await client.send(message)
    finally:
        clientes.remove(websocket)

# Start server
start_server = websockets.serve(handle_connection, '0.0.0.0', 33001)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


