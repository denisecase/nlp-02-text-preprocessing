# Glossary

This module focuses on preparing raw text
for natural language processing and analysis.

## Quick Lookup

Common terms used in this module:

- **Text Preprocessing** - preparing text for analysis.
- **Tokenization** - dividing text into smaller units.
- **Token** - a unit produced by a tokenizer.
- **Normalization** - converting text to a consistent representation.
- **Stopword** - a word commonly filtered in some NLP tasks.
- **Text Cleaning** - identifying and handling unwanted text content.
- **Token Frequency** - the number of occurrences of a token.

## Text Preprocessing

**Text preprocessing** is the process of preparing
raw text for computational analysis.

Preprocessing may include tokenization,
normalization, cleaning, and filtering.

The appropriate operations depend on
the analytical task and the methods being used.

## Tokenization

**Tokenization** divides text into smaller units
called tokens.

Depending on the tokenizer, tokens may represent
words, subwords, characters, or punctuation.

Tokenization is a foundational operation
in both traditional NLP and modern language models.

## Token

A **token** is a unit of text
produced by a tokenization process.

Token boundaries depend on the tokenizer.

The same text may produce different token sequences
when processed by different tokenizers.

## Minimum Token Length

A **minimum token length** filter excludes tokens
shorter than a chosen number of characters.

It can remove fragments and noise,
but it also removes short meaningful words
such as "no" or "AI".

The threshold is a preprocessing decision
that should be tested, not assumed.

## Normalization

**Normalization** converts text into a more consistent representation.

Common operations include:

- Converting uppercase letters to lowercase.
- Standardizing whitespace.
- Applying Unicode normalization.
- Standardizing selected textual conventions.

Normalization may reduce unwanted variation,
but it can also remove useful distinctions.

## Text Cleaning

**Text cleaning** identifies and handles
unwanted or irrelevant content.

Cleaning may involve removing formatting artifacts,
handling punctuation, correcting encoding problems,
or filtering selected tokens.

What constitutes noise depends on the task.

## Stopword

A **stopword** is a commonly occurring word
that may be excluded from some forms of text analysis.

Stopwords are often grammatical words
such as articles, prepositions, and conjunctions.

Stopword removal can simplify frequency analysis,
but some common words carry important meaning.

For example, negation words may be essential
for sentiment analysis or interpretation.

## Stopword Removal

**Stopword removal** is the process
of excluding tokens identified as stopwords.

It is a task-dependent preprocessing decision,
not a universal requirement for NLP.

Modern language models generally use token sequences
without traditional stopword removal.

## Whitespace

**Whitespace** consists of characters
that separate textual content,
including spaces, tabs, and line breaks.

Whitespace may be normalized
or used to identify token boundaries.

## Token Frequency

**Token frequency** is the number of times
a token occurs within a document or corpus.

Frequency counts help describe vocabulary usage
and identify common terms.

## Preprocessing Tradeoff

A **preprocessing tradeoff** occurs when
an operation reduces unwanted variation
but also risks removing useful information.

For example, lowercasing removes case differences
but may also remove distinctions between proper names
and ordinary words.

Preprocessing decisions should be evaluated
against the requirements of the analysis.

---

[◄ Back to 🏠 Home](index.md)
