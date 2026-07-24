---
license: apache-2.0
datasets:
  - sst2
  - glue
metrics:
  - accuracy
  - f1
language: en
pipeline_tag: text-classification
tags:
  - sentiment-analysis
  - distilbert
---

# DistilBERT SST-2 Sentiment Classifier

## Model description

A DistilBERT model fine-tuned for binary sentiment classification of short
English text. It is a distilled version of BERT, roughly 40% smaller and
60% faster while retaining most of the original accuracy.

## Intended uses and limitations

Intended for classifying the sentiment of English-language product reviews
and social media posts. Not intended for medical, legal, or other
high-stakes decision-making, and it has not been evaluated on languages
other than English.

## Training data

Trained on the Stanford Sentiment Treebank (SST-2) subset of the GLUE
benchmark, comprising short movie-review sentences labelled positive or
negative.

## Evaluation results

Accuracy of 0.91 and F1 of 0.90 on the SST-2 validation split.
