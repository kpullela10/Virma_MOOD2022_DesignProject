import random
import json
import torch
from chatbot_models import NeuralNetwork
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as f:
    intents = json.load(f)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNetwork(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Virma"
print("Lets chat! Type 'Goodbye' or 'Quit' to exit")

while True:
    sentence = input("You: ")
    if sentence == "quit" or sentence == "Quit":
        print(f"{bot_name}: {random.choice(intent['responses'])}")
        quit()
        break

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probability = torch.softmax(output, dim=1)
    actual_probability = probability[0][predicted.item()]
    if actual_probability.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                print(f"{bot_name}: {random.choice(intent['responses'])}")
    else:
        print(f"{bot_name}: I'm sorry, I'm not sure I understand. Do you mind rephrasing what you just said?"
              f" Also, make sure that your messages are in English, coherent,"
              f" aren't links, and don't have special characters."
              f" Thanks, sorry about that!")