=======================
GPT2 Language Model API 
=======================
:Info: See `OpenAI site <https://openai.com/blog/chatgpt>`_ for the latest source.
:Documentation: Available at `ChatGPT <https://github.com/mramitdas/ChatGPT/README.rst>`_
:Author: Amit Das


About
=====
This code provides an API endpoint that generates text based on prompts given by users, using the pre-trained GPT2 language model from the transformers library.


Download Repo
=============
- `Download url <https://github.com/mramitdas/chatgpt/archive/refs/heads/main.zip>`_


Installation
============
You can install the dependencies using the following command:
    | $ pip install -r requirements.txt


Usage
=====
To start the server, simply run the following command:
    | $ python3 app.py

This will start the server on http://localhost:8000.


Endpoint
========
The API has a single endpoint /generate which accepts a POST request with a JSON payload containing the prompt string to generate text from. The generated text is then returned in the response.


Example Request
===============
.. code-block:: bash
    POST /generate HTTP/1.1
    Host: localhost:8000
    Content-Type: application/json

    {
        "prompt": "The quick brown fox"
    }


Example Response
================
.. code-block:: bash
    HTTP/1.1 200 OK
    Content-Type: text/plain

    jumps over the lazy dog.


References
==========
- `FastAPI: <https://fastapi.tiangolo.com/>`_
- `Uvicorn: <https://www.uvicorn.org/>`_
- `Pydantic: <https://pydantic-docs.helpmanual.io/>`_
- `Transformers: <https://huggingface.co/transformers/>`_

