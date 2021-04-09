# DeepBugs Replication

## Description
For our ECE 595, Advanced Software Engineering, we are doing a replication of the [DeepBugs](https://arxiv.org/abs/1805.11683) study. The following sections describe our approach to conducting the replication.

## Process
Add info about specific dependencies and tools used (Python, Tensorflow, Github)
### Work Breakdown
*WBS here*

### Work Schedule
```mermaid
gantt
    title DeepBugs Replication
        dateFormat YYYY-MM-DD
        excludes weekend
        section Prep Tokens
            Setup Automated Test Pipeline with Github CI       :done, p1, 2021-02-26, 6d
            Prepare Code Corpus                                :done, p2, 2021-02-28, 3d 
            Develop AST Function Extractor                     :done, p3, after p2, 5d
            Extract Tokens from AST                            :done, p4, after p3, 3d
        section Prep Training
            Build Word2Vec Model                               :done, w1, after p4, 7d
        section Prep NN
            Build Bug Detector Neural Network                  :done, b1, after p4, 4d
        section Early Test
            Generate Training Set                              :done, e1, after w1, 3d
            Train Neural Network                               :done, e2, after e1, 3d
            Invent Bugs                                        :active, e3, 2021-04-01, 7d
        section Report
            Ethical Analysis                                   :      r1, after e3, 5d
            Report Sections                                    :      r2, after r1, 7d
            Prepare Delivables                                 :      r3, after r2, 5d
            
```

## Approach
```mermaid
graph LR
    code_corpus[Code Corpus] --> ast[AST Tokenizer]
    ast --> tokens[Tokens]
    tokens --> Word2Vec
    Word2Vec --> Tensorflow
```

### Code Corpus

### AST Tokens & Word2Vec
*UML of deepbugs-jr.py*

### Tensorflow
*Depiction of DL layers*

## Usage

## References
