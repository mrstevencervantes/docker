FROM jupyter/minimal-notebook

CMD ["start-notebook.sh", "--NotebookApp.token='MySuperStrongPassword'"]

COPY requirements.txt /tmp/requirements.txt

COPY teams.csv /tmp/

RUN pip install --quiet --no-cache-dir --upgrade pip setuptools

RUN pip install --quiet --no-cache-dir wheel

RUN pip install --quiet --no-cache-dir -r /tmp/requirements.txt

