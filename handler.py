import runpod
import time
import json
from llama_cpp import Llama

llm = Llama(model_path="model.gguf")


def handler(event):
    print(f"Worker start")
    input = event['input']

    prompt = input.get('prompt')
    seconds = input.get('seconds', 0)

    print(f"Received prompt: {prompt}")
    print(f"Sleeping for {seconds} seconds...")

    if 'messages' in input:
        return llm.create_chat_completion(**input)
    else:
        return llm(**input)

    return result


if __name__ == '__main__':
    runpod.serverless.start({'handler': handler})
