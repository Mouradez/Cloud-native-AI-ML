from locust import HttpUser, task
from random import choice
from string import ascii_uppercase

class User(HttpUser):
    @task
    def predict(self):
        payload = {
                 "question": "What is extractive question answering?",
                 "context": "Extractive Question Answering is the task of extracting an answer from a text given a question. An example of a question answering dataset is the SQuAD dataset, which is entirely based on that task. If you would like to fine-tune a model on a SQuAD task, you may leverage the run_squad.py."
                  }
        self.client.post("/question_answering",json=payload)

