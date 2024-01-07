from transformers import TFBertForSequenceClassification

model = TFBertForSequenceClassification.from_pretrained("nateraw/bert-base-uncased-imdb", from_pt=True)
model.save_pretrained("tfx_model", saved_model=True)