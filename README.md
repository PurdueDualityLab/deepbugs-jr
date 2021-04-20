# DeepBugs Replication

## Description
For our ECE 595, Advanced Software Engineering, we are doing a replication of the [DeepBugs](https://arxiv.org/abs/1805.11683) study. The following sections describe our approach to conducting the replication.

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
The original Deepbugs study produced a code corpus which we made use of in our reproduction study. [It](https://www.sri.inf.ethz.ch/js150) contains over 100,000 javascript source files and their corresponding AST source files.

### AST Tokens & Word2Vec
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

## Usage
1. Obtain AST values of javascript source files
2. Vectorize the AST values using the deepbugs_jr.py
3. Create the neural network model using the nn_trainer.py

## Dependencies
### Python Modules
+ word2vec
+ json
+ numpy
+ math
+ unittest
+ keras
+ Sequential
+ Dense
+ Dropout
+ KerasClassifier

## Dependencies
### Python Modules
+ ast2id_or_lit
+ word2vec
+ json
+ numpy
+ math
+ unittest
+ keras
+ Sequential
+ Dense
+ Dropout
+ KerasClassifier

## References
