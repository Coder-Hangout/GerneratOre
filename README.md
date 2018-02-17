# GerneratOre

This is a generator to create strings.
To generate a string put the configuration array into the generate function.

---
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
The structure of the **words array** contains all collections of words:
```
words = [ collection_1, collection_2, ... , collection_n ]
```
A **collection array** contains a list of words of the same type and category.
For better overall view and future features, provide a short description.
```
collection = [ description, word_1, word_2, ... , word_n ]
```
---

The **structure array** is the core of GeneratOre.
Here is the "code" to generate the string out of the words.
But there is not only one structure array, there can be multiple ones, inside each other.
The first place of **every** structure is the probability of it, we come to that later.
```
structure = [ probability, event_1, event_2,..., event_n]
```
There are two different types of **events**.
1. Select a **random word** from a word collection.
This works by writing the position of the collection inside words.
If you type -1 nothing will happen, this will be useful for the other option.

2. **Decide between multiple structures**. This works with an array of structures. 
One of them will be randomly selected based on the probability. 
The greater the value of it in comparison, the greater the chance.

```
structure = [ 1(probability), 5(collection), 6(collection), [ 
                                                            [2(probability), 8(collection), 7(collection)], 
                                                            [5(probability), 7(collection)], 
                                                            [2(probability),-1(nothing)] 
                                                            ](decision)
                                                            , 5(collection) ]
```