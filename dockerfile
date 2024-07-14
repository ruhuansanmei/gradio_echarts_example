from python:3.12.4-alpine3.19
RUN pip install gradio
COPY ./demo /wk/demo
COPY ./dist/gradio_mycomponent-0.0.1-py3-none-any.whl /wk/gradio_mycomponent-0.0.1-py3-none-any.whl
RUN pip install /wk/gradio_mycomponent-0.0.1-py3-none-any.whl
workdir /wk
entrypoint [ "python", "./demo/app.py"]










