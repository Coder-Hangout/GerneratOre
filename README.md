# GerneratOre

This is a generator to create strings.
To generate a string put the configuration array into the generate function.

```python
genreate(config)
> generated String
```
The configuration array is were you build the actual generator.
It is like a own little programming language.

The structure of the **configure array**:
```python
conf = [ words, structure ]
```
The structure of the **words array** contains all collections of words:
```python
words = [ collection_1, collection_2, ... , collection_n ]
```
A **collection array** contains a list of words of the same type and category.
For better overall view and future features, provide a short description.
```python
collection = [ description, word_1, word_2, ... , word_n ]
```


The **structure array** is the core of GeneratOre.
Here is the "code" to generate the string out of the words.
But there is not only one structure array, there can be multiple ones, inside each other.
The first place of **every**
```python
structure = []
```