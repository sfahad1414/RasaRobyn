from robyn import Robyn
from rasa.core.agent import Agent
import uuid6

app = Robyn(__file__)
agent = Agent.load("./models/20230913-154420-devout-envelope.tar.gz")


@app.get("/")
async def h(request):
    return "Hello, world!"


@app.post("/chat")
async def chat(request):
    print("chat")
    return await agent.handle_text("Hi", sender_id=uuid6.uuid7().hex)


app.start(port=8080)
