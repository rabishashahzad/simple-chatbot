import chainlit as lit
@lit.on_message
async def main (message: lit.Message):
    response = f"Received {message.content}"
    await lit.Message(content=response).send()