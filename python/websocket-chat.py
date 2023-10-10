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

PORT = 8081
HOST = '0.0.0.0'
clientes = set()

async def handle_connection(websocket, path):
   # Add the websocket to a list of connected clients
    
    match path:
        case "/":
            logging.warning("/")
            await auth(websocket)
        case "/chat":
            logging.warning("/path")
            await chat(websocket)
        case "/auth":
            logging.warning("/auth")


async def chat(websocket):
    try:
        while True:
            clientes.add(websocket)
            # Receive a message from the client
            logging.info(websocket)  # will not print anything
            message = await websocket.recv()
            
            # Broadcast the message to all connected clients
            for client in clientes:
                await client.send(message)
                
    finally:
        clientes.remove(websocket)    

async def auth(websocket):
    with open("users/Users.json", encoding='utf-8') as usuarios:
        dados = json.load(usuarios)
        logging.warning(dados)
        

    
# Start server
start_server = websockets.serve(handle_connection, HOST, PORT)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
