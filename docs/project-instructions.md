# Project Instructions

## Goal

Apply **text preprocessing** to prepare raw text
for analysis and investigate how cleaning decisions
affect token frequencies.

## A. Set Up Machine

Complete [Workflow A: Set Up Machine](https://denisecase.github.io/pro-analytics-02/workflow-a-set-up-machine/)
if your machine is not ready.

## B. Explore Example Project

Follow [Workflow B: Explore Example Project](https://denisecase.github.io/pro-analytics-02/workflow-b-explore-example-project/).

Explore how the example:

- Reads text records from a local file.
- Tokenizes raw text.
- Applies lowercasing and punctuation removal.
- Filters stopwords and short tokens.
- Calculates token frequencies using Polars.
- Visualizes the effects of preprocessing.

Consider how cleaning decisions change
the resulting vocabulary and token counts.

## C. Start New Project

Follow [Workflow C: Start New Project](https://denisecase.github.io/pro-analytics-02/workflow-c-start-new-project/).

IMPORTANT: New repository name:
**nlp-02-text-preprocessing-custom**.

VERIFY: You have completed git add-commit-push to GitHub at least twice.

## D. Apply Skills

Follow [Workflow D: Apply Skills](https://denisecase.github.io/pro-analytics-02/workflow-d-apply-skills/).

**Your problem:** Investigate how preprocessing choices
affect the vocabulary of a collection of text documents.

Create a small text dataset from a topic of interest.

### Progression 1. Your Project Works Like the Example

Ensure your new custom project runs like the example.

Verify that key files have been updated to use **your GitHub account** and
the **new custom repository name**.

### Progression 2. Make a Technical Modification

Change one preprocessing decision.

For example, modify the stopword list
or the minimum token length.

Run the analysis again and compare:

- The number of remaining tokens.
- The most frequent tokens.
- The resulting visualization.

Explain what changed and why.

### Progression 3. Apply to a New Problem

Apply the preprocessing process to your own text dataset.

- Create a text file containing at least 10 text records.
- Choose a topic and explain the source or authorship of the text.
- Update the program to read your new dataset.
- Inspect the raw text before cleaning.
- Apply and evaluate the preprocessing steps.
- Compare raw and cleaned token counts.
- Identify frequently occurring cleaned tokens.
- Explain which cleaning decisions are appropriate for your data.

Consider whether any useful information
was removed during preprocessing.

The goal is to make deliberate preprocessing decisions,
not simply remove as many tokens as possible.

## E. Finalize Project

Follow [Workflow E: Finalize Project](https://denisecase.github.io/pro-analytics-02/workflow-e-finalize/).

Use `docs/index.md` to report:

- Text data and analytical question.
- Preprocessing methods and technical modification.
- Raw and cleaned token counts.
- Most frequent cleaned tokens.
- A relevant visualization.
- Interpretation and preprocessing tradeoffs.

Include a clickable link to your repository and artifacts.

## Success

- [ ] README.md project-specific links use **your GitHub account**.
- [ ] README.md project-specific links use **your custom repository name**.
- [ ] docs/index.md project-specific links use **your GitHub account**.
- [ ] docs/index.md project-specific links use **your custom repository name**.
- [ ] pyproject.toml `name` has been changed to use **your custom repository name**.
- [ ] The `src/nlp` folder reflects your authorship and custom work.
- [ ] Your custom text dataset is included in the project.
- [ ] The analysis runs successfully with your data.
- [ ] All necessary commands are provided and work successfully.
- [ ] Links to the Professional Python Guide (pro-analytics-02) remain unchanged.
- [ ] Commit history shows **at least** the git add-commit-push history required in the instructions.

---

[◄ Back to Home](index.md)
