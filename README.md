## [Kaggle - Software Defect Prediction](https://www.kaggle.com/competitions/playground-series-s3e23/overview)

This repository is based on my submission to the Software Defect Prediction competition, where I achieved 1st place among 1704 participants.  

*Goal:* A binary classification task and the goal was to predict the probability of positive defects in C programs based on various attributes of the code.  

Evaluation: Submissions were evaluated based on the area under the ROC curve (AUC) comparing the predicted probabilities to the observed targets.  

Target column:
- `defects`, Binary variable indicating whether the module has defects (1 for yes, 0 for no).

Feature columns:
- `loc`: Lines of Code - Total number of lines of code in the software module
- `v(g)`: Cyclomatic Complexity - Measures the number of linearly independent paths through a program's source code
- `ev(g)`: Essential Complexity - Reflects the number of decision points that are strictly necessary in a program module.
- `iv(g)`: Design Complexity - Measures the complexity of the software architecture design.
- `n`: Total Operators + Operands - The total count of all operators and operands in the code.
- `v`: Halstead Volume - Reflects the size of the implementation; calculated using the number of operations and operands.
- `l`: Halstead Program Length - Measures the program length based on unique operators and operands.
- `d`: Halstead Difficulty - A measure of how difficult the code is to understand and maintain.
- `i`: Halstead Intelligence - Indicates the difficulty of understanding the program logic.
- `e`: Halstead Effort - Represents the effort required to write or understand the software.
- `b`: Halstead Error Estimate - Estimates the number of errors in the implementation.
- `t`: Halstead Time to Implement - Estimates the time it would take to implement the software.
- `lOCode`: Lines of Code without Comments - The number of lines of code excluding comments.
- `lOComment`: Lines of Comments - The number of lines that contain only comments.
- `lOBlank`: Blank Lines - Lines with no code or comments.
- `locCodeAndComment`: Lines of Code and Comment - Lines containing both code and comments.
- `uniq_Op`: Unique Operators - The count of unique operators used in the code.
- `uniq_Opnd`: Unique Operands - The count of unique operands used in the code.
- `total_Op`: Total Operators - The total count of operators in the code.
- `total_Opnd`: Total Operands - The total count of operands in the code.
- `branchCount`: Branch Count - Number of branches in the code; often correlates with the cyclomatic complexity.

[Streamlit App](https://theod9-kaggle-softwaredefectpredicition-app2-tqtlny.streamlit.app/)
