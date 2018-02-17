# GerneratOre

This is a generator to create strings.
To generate a string put the configuration array into the generate function.

```
genreate(config)
> generated String
```
The configuration array is were you build the actual generator.
It is like a own little programming language.

The structure of the **configure array**:
```
conf = [ words, structure ]
```
The structure of the **word array**:
```
words = [ collection_1, collection_2, ... , collection_n ]
```
A collection array contains a list of words
The structure of a **collection array**:
```
collection = [ description, word_1, word_2, ... , word_n ]
```


