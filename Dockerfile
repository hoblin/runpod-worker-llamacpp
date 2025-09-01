FROM nvidia/cuda:12.1.0-devel-ubuntu22.04 

RUN apt-get update -y \
    && apt-get install -y python3-pip wget git

RUN ldconfig /usr/local/cuda-12.1/compat/

# Install Python dependencies
COPY /requirements.txt /requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip \
    python3 -m pip install --upgrade pip && \
    python3 -m pip install --upgrade -r /requirements.txt
ENV GGML_CUDA=on
RUN pip install llama-cpp-python \
  --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cu121

RUN wget -O /model.gguf https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF/resolve/main/qwen2.5-0.5b-instruct-q4_k_m.gguf

# Copy your handler file
COPY handler.py /
COPY test_input.json /

# Start the container
CMD ["python3", "-u", "handler.py"]
