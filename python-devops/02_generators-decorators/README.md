# The Iteration Protocol

### Iterable

An object that can be looped over. It's anything we can put in the right side of the `in` keword in a `for` loop. E.g., lists, tuples, strings, dictionaries, sets, files, and range objects

- An object is considered **iterable** if it implements the `__iter__()` special method.

- The `__iter__()` method returns an iterator.

### Iterator

An object that produces the next value in a sequence when asked. It **remembers** its position in the sequence.

- An object is an **iterator** if it implements the `__next__()` special method. When there are no more items, `__next__()` raises the `StopIteration` exception.

- **Iterators** normally also implement the `__iter__()` method, which makes them **iterables** too.
