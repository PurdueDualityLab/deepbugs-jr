# DeepBugs Replication

## Approach

```mermaid
graph LR
    code_corpus[Code Corpus] --> ast[AST Tokenizer]
    ast --> tokens[Tokens]
    tokens --> Word2Vec
    Word2Vec --> Tensorflow
```
