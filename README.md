[![DOI](https://zenodo.org/badge/341390371.svg)](https://zenodo.org/badge/latestdoi/341390371)

# DeepBugs Replication

## Summary

We conducted a replication of the [DeepBugs](https://arxiv.org/abs/1805.11683) study.
This replication was accepted in the artifact track of ESEC/FSE'21 as a way to grant the "Results Replicated" badge to the original work.

For the one-page abstract and a longer technical report, look in the directory `paper/`.

For the description of our replication process, read below.

## Description

The following sections describe our approach to conducting the replication.

To properly view some of the diagrams below, the [Mermaid-Diagrams](https://chrome.google.com/webstore/detail/mermaid-diagrams/phfcghedmopjadpojhmmaffjmfiakfil/related?hl=en-US) Chrome extenstion may be necessary.

## Process
To complete this task we set up a project on this Github project. Here we managed our version control, project planning, and continuous integration. Like the origin paper, our project was built using Python 3 to provide acess to the Tensorflow, Keras, and gensim modules, each integral to the completion of this project. Our team held weekly tag ups to provide status updates and delegate work as needed. Additional information regarding the task breakdown and workflow can be found in the following sections.

### Work Breakdown
```mermaid
graph TD
    DR[DeepBugs Replication]
    CC[Develop Code Corpus]
    WV[Develop Word2Vec Model]
    NN[Develop Neural Network]
    T[Test the Model]
    R[Write the Report]

    DR --> CC
    CC --> CI[Setup Github CI]
    CI --> EX[Extract Tokens from Code Corpus]
    DR --> WV 
    WV --> AST[Identify AST Extractor] 
    AST --> CT[Tokenize AST]
    DR --> NN
    NN --> ID[Identify Layers for NN]
    ID --> BN[Build NN w/ Keras]
    DR --> T 
    T --> PT[Perform Training]
    PT --> TM[Run on Test Set]
    DR --> R
    R --> RS[Report Sections]
    RS --> A[Collect Artifacts]
```

### Work Schedule
```mermaid
gantt
    title DeepBugs Replication
        dateFormat YYYY-MM-DD
        section Prep Tokens
            Setup Automated Test Pipeline with Github CI       :done, p1, 2021-02-26, 6d
            Prepare Code Corpus                                :done, p2, 2021-02-28, 3d 
            Develop AST Function Extractor                     :done, p3, after p2, 5d
            Extract Tokens from AST                            :done, p4, after p3, 3d
        section Prep Training
            Build Word2Vec (CBOW) Model                               :done, w1, after p4, 7d
        section Prep NN
            Build Bug Detector Neural Network                  :done, b1, after p4, 4d
        section Early Test
            Generate Training Set                              :done, e1, after w1, 3d
            Train Neural Network                               :done, e2, after e1, 3d
            Invent Bugs                                        :active, e3, 2021-04-01, 7d
        section Report
            Ethical Analysis                                   :      r1, after e3, 8d
            Report Sections                                    :      r2, after r1, 7d
            Prepare Delivables                                 :      r3, after r2, 5d       
```

### Code Corpus
The original Deepbugs study produced a [code corpus](https://www.sri.inf.ethz.ch/js150) which we made use of in our reproduction study. It contains over 100,000 javascript source files and their corresponding AST source files. These files allow us to have enough javascript to properly train our model.

### Development Scripts
```mermaid
classDiagram
    class ast_token_extractor
        ast_token_extractor: +ast2id_or_lit()
        ast_token_extractor: -_acorn_json()


    class deepbugs_jr
        deepbugs_jr: +convert_to_ast()
        deepbugs_jr: +filter_token_list()
        deepbugs_jr: +main()

    class gen_train_eval
        gen_train_eval: +gen_good_bad_fun_args()

    class NN_basemodel
        NN_basemodel: +base_model_deepbugs()

    class swarg_fnargs2tokens
        swarg_fnargs2tokens: +get_all_2_arg_fn_calls_from_ast()
        swarg_fnargs2tokens: +get_fn_name()
        swarg_fnargs2tokens: +get_arg()

    class swarg_gen_train_eval
        swarg_gen_train_eval: +gen_good_bad_fn_args()

    deepbugs_jr o-- ast_token_extractor
```

### Tensorflow
```mermaid
graph TD
    dropoutA[20% Dropout]
    denseA[200 Relu Dense]
    dropoutB[20% Dropout]
    denseB[1 Sigmoid Dense]
    
    subgraph Sequential
        dropoutA --> denseA
        denseA --> dropoutB
        dropoutB --> denseB
    end
```

#### Dropout layers
Dropout in neural network in general is a regularization method that approximates training a large number of neural networks with different architectures in parallel. By "dropping out" neurons, the over-fitting problem can be mitigated. The original authors of Deepbugs states in the paper that they applied a dropout of 0.2 to the input and the hidden layer. To replicate their work, we follow their approach of applying dropout layers. 

#### Dense layers
Dense layer is most commonly found layer in the models. It is a neural network layer that is connected deeply, which means each neuron in the dense layer receives input from all neurons of its previous layer. 

The original authors claims in their paper that they applied a feedforward neural network with an input layer of a size that depends on the code representation
provided by the specific bug detector, a single hidden layer of size 200, and an output layer with a single element that represents the probability computed by a bug detector.


## Usage
Read the guide in [demo_deepbugs_jr.ipynb](https://github.com/deep-bugs-jr/deep-bugs-jr/blob/main/demo_deepbugs_jr.ipynb).



## Dependencies
### Python Modules
+ tensorflow
+ keras
+ gensim
+ numpy

