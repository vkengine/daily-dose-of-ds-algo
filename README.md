# My collection of DS and ALGO problems I solve everyday

## crash course:
What Are Data Structures?
```
The elementary particles of algorithms, data structures are 
woven into the very fabric of computer science and are 
essential building blocks of all applications
```
Complexity Analysis :
```
Complexity Analysis
The process of determining how efficient an algorithm is. Complexity analysis usually involves finding both the time complexity and the space complexity of an algorithm.
Complexity analysis is effectively used to determine how "good" an algorithm is and whether it's "better" than another one.

Time Complexity
A measure of how fast an algorithm runs, time complexity is a central concept in the field of algorithms and in coding interviews.
It's expressed using Big O notation.

Space Complexity
A measure of how much auxiliary memory an algorithm takes up, space complexity is a central concept in the field of algorithms and in coding interviews.

It's expressed using Big O notation.
```

Memory:
```
Bit
Short for binary digit, a bit is a fundamental unit of information in Computer Science that represents a state with one of two values, typically 0 and 1.

Any data stored in a computer is, at the most basic level, represented in bits.

Byte
A group of eight bits. For example, 01101000 is a byte.

A single byte can represent up to 256 data values (28).

Since a binary number is a number expressed with only two symbols, like 0 and 1, a byte can effectively represent all of the numbers between 0 and 255, inclusive, in binary format.

The following bytes represent the numbers 1, 2, 3, and 4 in binary format.

1: 00000001
2: 00000010
3: 00000011
4: 00000100
Fixed-Width Integer
An integer represented by a fixed amount of bits. For example, a 32-bit integer is an integer represented by 32 bits (4 bytes), and a 64-bit integer is an integer represented by 64 bits (8 bytes).

The following is the 32-bit representation of the number 1, with clearly separated bytes:

00000000 00000000 00000000 00000001
The following is the 64-bit representation of the number 10, with clearly separated bytes:

00000000 00000000 00000000 00000000 00000000 00000000 00000000 00001010
Regardless of how large an integer is, its fixed-width-integer representation is, by definition, made up of a constant number of bits.

It follows that, regardless of how large an integer is, an operation performed on its fixed-width-integer representation consists of a constant number of bit manipulations, since the integer is made up of a fixed number of bits.

Memory
Broadly speaking, memory is the foundational layer of computing, where all data is stored.
Data stored in memory is stored in bytes and, by extension, bits.
Bytes in memory can "point" to other bytes in memory, so as to store references to other data.
The amount of memory that a machine has is bounded, making it valuable to limit how much memory an algorithm takes up.
Accessing a byte or a fixed number of bytes (like 4 bytes or 8 bytes in the case of 32-bit and 64-bit integers) is an elementary operation, which can be loosely treated as a single unit of operational work.
```

Big O Notation:
```
The notation used to describe the time complexity and space complexity of algorithms.

Variables used in Big O notation denote the sizes of inputs to algorithms. For example, O(n) might be the time complexity of an algorithm that traverses through an array of length n; similarly, O(n + m) might be the time complexity of an algorithm that traverses through an array of length n and through a string of length m.

The following are examples of common complexities and their Big O notations, ordered from fastest to slowest:

Constant: O(1)
Logarithmic: O(log(n))
Linear: O(n)
Log-linear: O(nlog(n))
Quadratic: O(n2)
Cubic: O(n3)
Exponential: O(2n)
Factorial: O(n!)
Note that in the context of coding interviews, Big O notation is usually understood to describe the worst-case complexity of an algorithm, even though the worst-case complexity might differ from the average-case complexity.

For example, some sorting algorithms have different time complexities depending on the layout of elements in their input array. In rare cases, their time complexity will be much worse than in more common cases. Similarly, an algorithm that takes in a string and performs special operations on uppercase characters might have a different time complexity when run on an input string of only uppercase characters vs. on an input string with just a few uppercase characters.

Thus, when describing the time complexity of an algorithm, it can sometimes be helpful to specify whether the time complexity refers to the average case or to the worst case (e.g., "this algorithm runs in O(nlog(n)) time on average and in O(n2) time in the worse case").
```

Array :
```

A linear collection of data values that are accessible at numbered indices, starting at index 0.

The following are an array's standard operations and their corresponding time complexities:

Accessing a value at a given index: O(1)
Updating a value at a given index: O(1)
Inserting a value at the beginning: O(n)
Inserting a value in the middle: O(n)
Inserting a value at the end:
amortized O(1) when dealing with a dynamic array
O(n) when dealing with a static array
Removing a value at the beginning: O(n)
Removing a value in the middle: O(n)
Removing a value at the end: O(1)
Copying the array: O(n)
```