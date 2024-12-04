FROM python:3.10

WORKDIR /app

COPY ./pinnacle .
COPY ./plugins .
COPY ./templates/pdf_rag templates/pdf_rag

RUN pip install -e . && pip install plugins/mongodb && pip install streamlit
RUN pip install --no-cache-dir ./templates/pdf_rag/requirements.txt

RUN pinnacle bootstrap ./templates/pdf_rag
RUN python3 add_data.py
RUN pinnacle apply pdf_rag

CMD ["streamlit", "run", "templates/pdf_rag/streamlit.py", "--server.runOnSave", "true"]
