import runpod
import json
from llama_cpp import Llama

args = json.loads(os.environ.get("LLAMA_ARGS", "{}"))
if "model_path" not in args:
    args["model_path"] = "model.gguf"
llm = Llama(**args)


def handler(event):
    print(f"Worker start")
    input = event['input']

    prompt = input.get('prompt')

    print(f"Received prompt: {prompt}")

    if 'messages' in input:
        return llm.create_chat_completion(**input)
    else:
        return llm(**input)

    return result


if __name__ == '__main__':
    runpod.serverless.start({'handler': handler})
