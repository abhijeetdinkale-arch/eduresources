import os

content = r"""\chapter{Strings, Lists, Tuples, Sets \& Dictionaries}
\label{ch:strings_lists_tuples_dicts}

\begin{tcolorbox}[
    enhanced,
    colback=boxnavybg,
    colframe=brandnavy,
    boxrule=1pt,
    arc=4pt,
    title={\Large\bfseries\sffamily Chapter Learning Objectives}
]
\sffamily
By the end of this chapter, you will be able to:
\begin{enumerate}
    \item Understand and manipulate core Python sequence types (Strings, Lists, Tuples).
    \item Master string operations, string methods, and lexicographic ASCII comparisons.
    \item Implement advanced list operations, comprehensions, and classical algorithms like Bubble Sort.
    \item Use sets and dictionaries for optimal associative lookups and sparse data representations.
    \item Utilize advanced iteration tools like \texttt{enumerate()} and \texttt{zip()}.
    \item Analyze Python's memory model regarding variable aliasing, shallow copying, and deep copying.
\end{enumerate}
\end{tcolorbox}

% ==============================================================================
% SECTION 4.1: INTRODUCTION TO COMPOUND DATA TYPES
% ==============================================================================
\section{Introduction to Compound Data Types}

In preceding chapters, we worked primarily with scalar data types such as integers, floats, and booleans. These primitive types hold a single, indivisible value in memory. However, practical programming demands structures capable of grouping multiple values together. A paragraph of text is not a single character, but a sequence of characters. A university class roll is not a single student ID, but a collection of IDs.

Python provides built-in \textbf{compound data types} (often called collections or data structures) to manage multiple values. These structures differ profoundly in their memory behavior, lookup efficiency, and mutability. We can categorize them broadly into \textbf{sequences} (which are ordered by integer indices) and \textbf{mappings/sets} (which are unordered and optimized for fast associative retrieval). 

\begin{conceptbox}[Mutability vs. Immutability]
A critical distinction in Python is whether an object's state can be altered after its creation in memory.
\begin{itemize}
    \item \textbf{Mutable Types}: Can be modified in-place (e.g., Lists, Dictionaries, Sets). Their memory contents change without changing their memory address.
    \item \textbf{Immutable Types}: Cannot be modified once created (e.g., Strings, Tuples, Integers). Any operation that appears to modify them actually creates a completely new object in memory.
\end{itemize}
\end{conceptbox}

% ==============================================================================
% SECTION 4.2: STRINGS & TEXT PROCESSING
% ==============================================================================
\section{Strings: Ordered Character Sequences}

A string is a sequential collection of characters enclosed in single (\texttt{''}), double (\texttt{""}), or triple (\texttt{""" """}) quotes. Strings in Python are strictly \textbf{immutable}. When we manipulate a string, we are always constructing and returning a brand new string, leaving the original sequence unaffected in memory.

\subsection{Lexicographic Comparison \& ASCII Fundamentals}
\label{sec:lexicographic}
\index{Lexicographic Comparison}\index{ASCII}

How does Python know that \texttt{"apple"} is less than \texttt{"banana"}? When we use relational operators (\texttt{<}, \texttt{>}, \texttt{==}) on strings, Python evaluates them \textbf{lexicographically} (alphabetically), comparing the underlying numeric ASCII/Unicode values of the characters from left to right.

Every character corresponds to an integer code point. Python provides two built-in functions to bridge characters and their integer representations:
\begin{itemize}
    \item \texttt{ord(char)}: Returns the integer ASCII/Unicode value of a given character.
    \item \texttt{chr(int)}: Returns the character corresponding to a given integer value.
\end{itemize}

\begin{pythoncode}[]{ASCII Values and Lexicographic Comparison}
print("ASCII value of 'A':", ord('A'))
print("ASCII value of 'a':", ord('a'))
print("Character for 66:", chr(66))

# Lexicographic comparison
print("'apple' < 'banana':", "apple" < "banana")
print("'Apple' < 'apple':", "Apple" < "apple")  # 65 < 97
\end{pythoncode}

\begin{outputbox}
ASCII value of 'A': 65
ASCII value of 'a': 97
Character for 66: B
'apple' < 'banana': True
'Apple' < 'apple': True
\end{outputbox}

Because uppercase letters (65--90) have lower ASCII values than lowercase letters (97--122), \texttt{"Zebra"} is considered mathematically less than \texttt{"apple"}.

\subsection{String Traversal and Slicing}

We can access individual characters using bracket notation \texttt{[]}, where indexing starts from \texttt{0}. Python also supports negative indexing, where \texttt{-1} accesses the very last character.

Slicing allows us to extract a contiguous sub-segment of a string.
\begin{syntaxbox}[String Slicing Syntax]
\texttt{string\_name[start : stop : step]}
\begin{itemize}
    \item \texttt{start}: Index to begin slicing (inclusive).
    \item \texttt{stop}: Index to end slicing (exclusive).
    \item \texttt{step}: The stride length (optional, defaults to 1).
\end{itemize}
\end{syntaxbox}

\begin{pythoncode}[]{String Traversal and Slicing}
text = "Python Programming"

# Indexing
print("First character:", text[0])
print("Last character:", text[-1])

# Slicing
print("Slice [0:6]:", text[0:6])
print("Reverse string:", text[::-1])
\end{pythoncode}

\begin{outputbox}
First character: P
Last character: g
Slice [0:6]: Python
Reverse string: gnimmargorP nohtyP
\end{outputbox}

\subsection{Comprehensive String Methods} \label{sec:string_methods}

Strings possess a rich library of built-in methods. Because strings are immutable, these methods never alter the original string; instead, they return a new string containing the modified content. 

\begin{table}[H]
    \centering\sffamily
    \rowcolors{2}{white}{gray!10}
    \begin{tabular}{p{4.5cm} p{10cm}}
    \toprule
    \textbf{Method} & \textbf{Description} \\
    \midrule
    \texttt{.strip()}, \texttt{.lstrip()}, \texttt{.rstrip()} & Removes leading/trailing whitespace (or specified characters). \\
    \texttt{.lower()}, \texttt{.upper()} & Converts string to fully lowercase or uppercase. \\
    \texttt{.title()}, \texttt{.capitalize()} & Capitalizes words or the very first character. \\
    \texttt{.split(delimiter)} & Breaks the string into a list of strings based on the delimiter. \\
    \texttt{.join(iterable)} & Concatenates an iterable of strings using the string as a separator. \\
    \texttt{.replace(old, new)} & Replaces occurrences of a substring with a new substring. \\
    \texttt{.find(sub)}, \texttt{.index(sub)} & Returns the lowest index where substring is found. (\texttt{find} returns -1 if not found, \texttt{index} raises ValueError). \\
    \texttt{.count(sub)} & Counts non-overlapping occurrences of a substring. \\
    \texttt{.startswith(sub)}, \texttt{.endswith()} & Returns True if the string starts/ends with the specified substring. \\
    \texttt{.isdigit()}, \texttt{.isalpha()} & Returns True if all characters are digits / alphabetic characters. \\
    \bottomrule
    \end{tabular}
    \caption{Essential Python String Methods}
\end{table}

Let us examine these methods in a practical context.

\begin{pythoncode}[]{String Methods Showcase}
raw_text = "   Hello, Python World!   "

# Cleaning and formatting
clean_text = raw_text.strip()
print("Stripped:", f"'{clean_text}'")
print("Upper:", clean_text.upper())

# Searching and counting
print("Count of 'o':", clean_text.count('o'))
print("Index of 'Python':", clean_text.find("Python"))

# Splitting and Joining
words = clean_text.split()  # Splits by default whitespace
print("Words list:", words)

csv_data = ",".join(words)
print("Joined with commas:", csv_data)

# Replacement
swapped = clean_text.replace("Python", "Java")
print("Replaced:", swapped)
\end{pythoncode}

\begin{outputbox}
Stripped: 'Hello, Python World!'
Upper: HELLO, PYTHON WORLD!
Count of 'o': 3
Index of 'Python': 7
Words list: ['Hello,', 'Python', 'World!']
Joined with commas: Hello,,Python,World!
Replaced: Hello, Java World!
\end{outputbox}

\begin{examtip}[String Immutability Pitfall]
\lpuBadge{} A frequent student mistake is writing \texttt{text.strip()} without assigning the result back to a variable. Since strings are immutable, \texttt{text} remains unchanged unless you write \texttt{text = text.strip()}.
\end{examtip}

% ==============================================================================
% SECTION 4.3: LISTS & DYNAMIC ARRAYS
% ==============================================================================
\section{Lists: Dynamic Mutable Sequences}

Lists are the workhorse data structure in Python. A list is a dynamically sized, mutable sequence capable of storing elements of heterogeneous data types. Unlike traditional arrays in C or Java, Python lists manage their own memory capacity and can shrink or grow seamlessly during runtime.

\subsection{List Methods and Mutability}

Because lists are mutable, many list methods perform operations \textbf{in-place}. This means they alter the list directly and return \texttt{None}.

\begin{table}[H]
    \centering\sffamily
    \rowcolors{2}{white}{gray!10}
    \begin{tabular}{p{4.5cm} p{10cm}}
    \toprule
    \textbf{Method} & \textbf{Description} \\
    \midrule
    \texttt{.append(item)} & Adds a single item to the very end of the list. \\
    \texttt{.extend(iterable)} & Unpacks an iterable and adds its elements to the end. \\
    \texttt{.insert(index, item)} & Inserts an item at a specific index, shifting subsequent items right. \\
    \texttt{.remove(item)} & Removes the \textit{first} occurrence of the specified item (raises ValueError if not found). \\
    \texttt{.pop([index])} & Removes and returns the item at the index (default is the last item). \\
    \texttt{.clear()} & Removes all elements from the list, emptying it. \\
    \texttt{.sort(key=..., reverse=...)} & Sorts the list in-place. \\
    \texttt{.reverse()} & Reverses the elements of the list in-place. \\
    \texttt{.index(item)}, \texttt{.count(item)} & Returns the index of the first match / count of the item. \\
    \bottomrule
    \end{tabular}
    \caption{Essential Python List Methods}
\end{table}

\begin{pythoncode}[]{List Methods Showcase}
cities = ["Tokyo", "Delhi", "Paris"]

# Adding elements
cities.append("Berlin")
cities.extend(["London", "Seoul"])
cities.insert(1, "New York")
print("After additions:", cities)

# Removing elements
removed_city = cities.pop() # Removes 'Seoul'
cities.remove("Paris")
print("After removals:", cities)
print("Popped city:", removed_city)

# Sorting and Reversing
cities.sort()
print("Alphabetically sorted:", cities)
cities.reverse()
print("Reversed sorted:", cities)
\end{pythoncode}

\begin{outputbox}
After additions: ['Tokyo', 'New York', 'Delhi', 'Paris', 'Berlin', 'London', 'Seoul']
After removals: ['Tokyo', 'New York', 'Delhi', 'Berlin', 'London']
Popped city: Seoul
Alphabetically sorted: ['Berlin', 'Delhi', 'London', 'New York', 'Tokyo']
Reversed sorted: ['Tokyo', 'New York', 'London', 'Delhi', 'Berlin']
\end{outputbox}

\begin{commonmistake}[append() vs. extend()]
\examBadge{} Confusing \texttt{append} and \texttt{extend} is a very common exam error. 
\begin{itemize}
    \item \texttt{lst.append([1, 2])} adds a single element (the entire list \texttt{[1, 2]}) to the end, resulting in a nested list.
    \item \texttt{lst.extend([1, 2])} iterates through \texttt{[1, 2]} and adds \texttt{1} and \texttt{2} as separate, flat elements.
\end{itemize}
\end{commonmistake}

\subsection{sort() vs sorted()}

Python provides two ways to sort elements. 
1. \texttt{list.sort()} is a list method that sorts \textbf{in-place} and returns \texttt{None}.
2. \texttt{sorted(iterable)} is a built-in function that takes any iterable, leaves the original unchanged, and returns a \textbf{new sorted list}.

\begin{pythoncode}[]{sort() vs sorted()}
numbers = [42, 10, 88, 3]

# Using sorted() - Original remains unchanged
new_sorted_list = sorted(numbers)
print("Original list:", numbers)
print("New sorted list:", new_sorted_list)

# Using .sort() - Modifies the original list directly
result = numbers.sort()
print("\nAfter .sort():", numbers)
print("Return value of .sort():", result)
\end{pythoncode}

\begin{outputbox}
Original list: [42, 10, 88, 3]
New sorted list: [3, 10, 42, 88]

After .sort(): [3, 10, 42, 88]
Return value of .sort(): None
\end{outputbox}

\subsection{List Comprehensions with Filtering}

List comprehensions offer a concise, highly optimized syntax for generating new lists from existing sequences. They consolidate a \texttt{for} loop and an \texttt{if} statement into a single expressive line.

\begin{syntaxbox}[List Comprehension Syntax]
\texttt{[ expression for item in iterable if condition ]}
\end{syntaxbox}

\begin{pythoncode}[]{List Comprehension with Filtering}
numbers = [1, -5, 8, -2, 10, 3]

# Without comprehension (Traditional loop)
positive_squares_loop = []
for n in numbers:
    if n > 0:
        positive_squares_loop.append(n ** 2)

# With list comprehension
positive_squares_comp = [n ** 2 for n in numbers if n > 0]

print("Loop approach:", positive_squares_loop)
print("Comprehension:", positive_squares_comp)
\end{pythoncode}

\begin{outputbox}
Loop approach: [1, 64, 100, 9]
Comprehension: [1, 64, 100, 9]
\end{outputbox}

\subsection{The 2D List Multiplication Trap}
\index{Aliasing}\index{Lists!Nested Lists}

In Python, we often use the repetition operator \texttt{*} to initialize lists, such as \texttt{[0] * 5} which yields \texttt{[0, 0, 0, 0, 0]}. However, applying this to multi-dimensional lists creates a severe \textbf{aliasing} trap.

\begin{pythoncode}[]{The 2D List Multiplication Trap}
# Incorrect way to create a 3x3 grid
grid_bad = [[0] * 3] * 3

# Modifying one element...
grid_bad[0][0] = 99

print("Bad Grid Result:")
for row in grid_bad:
    print(row)

# Correct way using list comprehension
grid_good = [[0 for _ in range(3)] for _ in range(3)]
grid_good[0][0] = 99

print("\nGood Grid Result:")
for row in grid_good:
    print(row)
\end{pythoncode}

\begin{outputbox}
Bad Grid Result:
[99, 0, 0]
[99, 0, 0]
[99, 0, 0]

Good Grid Result:
[99, 0, 0]
[0, 0, 0]
[0, 0, 0]
\end{outputbox}

\begin{conceptbox}[Why did this happen?]
When you evaluate \texttt{[[0] * 3] * 3}, Python evaluates the inner list \texttt{[0, 0, 0]} once, storing it at a specific memory address. The outer multiplication \texttt{* 3} simply creates a list containing three \textit{references} to that exact same inner list. Changing one row changes them all because they are mathematically the same object!

The list comprehension correctly forces the creation of a brand new list in memory for each iteration.
\end{conceptbox}

\subsection{Algorithm Focus: Bubble Sort}

To truly understand list mutability and index manipulation, we examine \textbf{Bubble Sort}, a foundational sorting algorithm. The algorithm repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. 

The pass through the list is repeated until the list is sorted. It is called ``bubble sort'' because smaller/larger elements ``bubble'' to the top of the list.

\begin{pythoncode}[]{Bubble Sort Implementation}
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements
    for i in range(n):
        # Last i elements are already in place, no need to check them
        swapped = False
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap them
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # Optimization: If no two elements were swapped, array is sorted
        if not swapped:
            break
            
data = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(data)
print("Sorted Array in Ascending Order:")
print(data)
\end{pythoncode}

\begin{outputbox}
Sorted Array in Ascending Order:
[11, 12, 22, 25, 34, 64, 90]
\end{outputbox}

\textbf{Analysis:}
\begin{itemize}
    \item \textbf{Adjacent Swapping}: \texttt{arr[j], arr[j+1] = arr[j+1], arr[j]} elegantly swaps variables without needing a temporary variable.
    \item \textbf{The \texttt{n - i - 1} limit}: After the $i^{th}$ pass, the $i$ largest elements are already at their final positions at the end of the list. We subtract $i$ to avoid redundantly comparing them. We subtract $1$ because we look ahead to \texttt{j + 1}.
    \item \textbf{Time Complexity}: Because we have nested loops dependent on the list length $n$, the time complexity is $O(n^2)$. This is much less efficient than Python's built-in \texttt{Timsort} algorithm used in \texttt{.sort()}, which operates at $O(n \log n)$.
\end{itemize}

% ==============================================================================
% SECTION 4.4: TUPLES
% ==============================================================================
\section{Tuples: Immutable Sequences}

A \textbf{tuple} is an ordered, immutable sequence of heterogeneous elements. Tuples are defined using parentheses \texttt{()}, though the parentheses are often optional; the commas are what actually define the tuple.

Because tuples are immutable, they provide structural integrity. Once constructed, a tuple's length and the references it holds cannot be modified. They cannot be appended to, nor can elements be reassigned.

\begin{pythoncode}[]{Tuple Basics and Packing/Unpacking}
# Creating tuples
t1 = (10, 20, 30)
t2 = 40, 50, 60     # Parentheses are optional (Tuple Packing)
t3 = (5,)           # Single-element tuple MUST have a trailing comma

print("Types:", type(t1), type(t2), type(t3))

# Tuple Unpacking
a, b, c = t1
print(f"Unpacked variables: a={a}, b={b}, c={c}")

# Attempting mutation (Causes Error)
# t1[0] = 99  # TypeError: 'tuple' object does not support item assignment
\end{pythoncode}

\begin{outputbox}
Types: <class 'tuple'> <class 'tuple'> <class 'tuple'>
Unpacked variables: a=10, b=20, c=30
\end{outputbox}

\subsection{Tuples as Dictionary Keys}
Because tuples are immutable, they are \textbf{hashable}. This means they can be processed by Python's hashing function to produce a fixed integer, allowing them to serve as keys in dictionaries or elements in sets. Lists, being mutable, cannot.

This property makes tuples ideal for representing multi-dimensional coordinates or composite keys.

\begin{pythoncode}[]{Tuples as Dictionary Keys}
# Storing distances between two coordinate points
distances = {
    (0, 0): 0.0,
    (0, 1): 1.0,
    (3, 4): 5.0
}

point = (3, 4)
print(f"Distance to {point} is {distances[point]}")
\end{pythoncode}

\begin{outputbox}
Distance to (3, 4) is 5.0
\end{outputbox}

% ==============================================================================
% SECTION 4.5: SETS
% ==============================================================================
\section{Sets: Unordered Mathematical Collections}
\index{Sets}

A \textbf{set} is an unordered, mutable collection of \textbf{unique} and immutable (hashable) elements. Sets are written using curly braces \texttt{\{\}}, just like dictionaries, but without key-value pairs. 

Sets are highly optimized for fast membership testing (\texttt{in} operations) and mathematical set operations (Union, Intersection, Difference).

\begin{pythoncode}[]{Set Basics and Operations}
# Creating sets
set_a = {1, 2, 3, 4, 4, 4} # Duplicates are automatically removed
set_b = {3, 4, 5, 6}

print("Set A:", set_a) # Output: {1, 2, 3, 4}

# Mathematical Operations
print("Union (|):", set_a | set_b)
print("Intersection (&):", set_a & set_b)
print("Difference (-):", set_a - set_b)

# Membership testing (Extremely fast O(1) lookup)
print("Is 3 in Set A?", 3 in set_a)
\end{pythoncode}

\begin{outputbox}
Set A: {1, 2, 3, 4}
Union (|): {1, 2, 3, 4, 5, 6}
Intersection (&): {3, 4}
Difference (-): {1, 2}
Is 3 in Set A? True
\end{outputbox}

% ==============================================================================
% SECTION 4.6: DICTIONARIES
% ==============================================================================
\section{Dictionaries: Key-Value Mappings}

A \textbf{dictionary} is a mutable mapping type that pairs unique keys with values. Unlike sequences that are indexed by consecutive integers, dictionaries are indexed by keys, which can be any immutable (hashable) type such as strings, numbers, or tuples.

Behind the scenes, dictionaries employ \textbf{hash tables}, making element lookups remarkably fast ($O(1)$ time complexity), regardless of how large the dictionary grows.

\subsection{Dictionary Methods and Iteration Patterns}

Dictionaries provide several methods to inspect and traverse their contents.

\begin{table}[H]
    \centering\sffamily
    \rowcolors{2}{white}{gray!10}
    \begin{tabular}{p{4.5cm} p{10cm}}
    \toprule
    \textbf{Method} & \textbf{Description} \\
    \midrule
    \texttt{.keys()} & Returns a view object displaying a list of all keys. \\
    \texttt{.values()} & Returns a view object displaying a list of all values. \\
    \texttt{.items()} & Returns a view object displaying a list of \texttt{(key, value)} tuple pairs. \\
    \texttt{.get(key, default)} & Returns value for key, or \texttt{default} if key is not found (avoids KeyError). \\
    \texttt{.update(dict2)} & Updates the dictionary with the key/value pairs from \texttt{dict2}. \\
    \texttt{.pop(key, default)} & Removes key and returns its value. \\
    \texttt{.setdefault(k, d)} & Returns value of key if present; else inserts key with value \texttt{d}. \\
    \bottomrule
    \end{tabular}
    \caption{Essential Python Dictionary Methods}
\end{table}

\begin{pythoncode}[]{Dictionary Iteration Patterns}
student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78}

# Safe lookup using get()
print("Alice's score:", student_scores.get("Alice"))
print("David's score:", student_scores.get("David", "Not Found"))

# Pattern 1: Iterating over keys (Default behavior)
print("\nKeys:")
for name in student_scores:
    print(name, end=" ")

# Pattern 2: Iterating over values
print("\n\nValues:")
for score in student_scores.values():
    print(score, end=" ")

# Pattern 3: Iterating over items (key, value pairs)
print("\n\nItems:")
for name, score in student_scores.items():
    print(f"{name}: {score}")
    
# Dictionary Comprehension
curve_scores = {name: score + 5 for name, score in student_scores.items()}
print("\nCurved scores:", curve_scores)
\end{pythoncode}

\begin{outputbox}
Alice's score: 85
David's score: Not Found

Keys:
Alice Bob Charlie 

Values:
85 92 78 

Items:
Alice: 85
Bob: 92
Charlie: 78

Curved scores: {'Alice': 90, 'Bob': 97, 'Charlie': 83}
\end{outputbox}

% ==============================================================================
% SECTION 4.7: PARALLEL AND INDEXED ITERATION
% ==============================================================================
\section{Advanced Iteration: enumerate() and zip()}

When working with compound data types, Python developers rarely use standard \texttt{for i in range(len(lst))} loops. Python provides built-in tools for more elegant and Pythonic iteration.

\subsection{Using \texttt{enumerate()}}
\texttt{enumerate()} adds an automatic counter to an iterable, returning a tuple of \texttt{(index, value)} for each element.

\begin{pythoncode}[]{enumerate() Usage}
languages = ["Python", "Java", "C++"]

# Non-Pythonic way
for i in range(len(languages)):
    print(f"Index {i}: {languages[i]}")

print("---")

# Pythonic way using enumerate
for i, lang in enumerate(languages):
    print(f"Index {i}: {lang}")
\end{pythoncode}

\begin{outputbox}
Index 0: Python
Index 1: Java
Index 2: C++
---
Index 0: Python
Index 1: Java
Index 2: C++
\end{outputbox}

\subsection{Using \texttt{zip()}}
\texttt{zip()} takes two or more iterables and ``zips'' them together in parallel, returning an iterator of tuples. It stops when the shortest iterable is exhausted.

\begin{pythoncode}[]{zip() with Dictionaries}
names = ["Alice", "Bob", "Charlie"]
grades = ["A", "B+", "A-"]

# Zipping lists together
for name, grade in zip(names, grades):
    print(f"{name} achieved {grade}")

# Creating a dictionary from two lists using zip
grade_dict = dict(zip(names, grades))
print("\nDictionary from zip:", grade_dict)
\end{pythoncode}

\begin{outputbox}
Alice achieved A
Bob achieved B+
Charlie achieved A-

Dictionary from zip: {'Alice': 'A', 'Bob': 'B+', 'Charlie': 'A-'}
\end{outputbox}

% ==============================================================================
% SECTION 4.8: MEMORY MANAGEMENT AND COPYING
% ==============================================================================
\section{Memory Management: Aliasing and Copying}
\index{Aliasing}

Because variables in Python are merely \textit{labels} or \textit{references} pointing to objects in memory, simply assigning a list to a new variable does not create a new list. Both variables point to the same memory address, a phenomenon known as \textbf{aliasing}.

To actually duplicate a list, we must explicitly copy it.

\begin{conceptbox}[Shallow Copy vs. Deep Copy]
\begin{itemize}
    \item \textbf{Shallow Copy} (\texttt{list.copy()}, slicing \texttt{[:]}, \texttt{copy.copy()}): Creates a new outer object, but inserts references to the original nested objects.
    \item \textbf{Deep Copy} (\texttt{copy.deepcopy()}): Recursively creates new objects for the outer collection and all inner nested objects. Completely isolates the new object from the original.
\end{itemize}
\end{conceptbox}

\begin{pythoncode}[]{Shallow vs Deep Copy}
import copy

# Original nested list
original = [1, 2, [3, 4]]

# Aliasing (Not a copy)
alias_list = original

# Shallow Copy
shallow = original.copy()

# Deep Copy
deep = copy.deepcopy(original)

# Mutate the nested list inside original
original[2][0] = 99

print("Original:", original)
print("Alias:   ", alias_list)
print("Shallow: ", shallow)  # Nested list affected!
print("Deep:    ", deep)     # Completely safe!
\end{pythoncode}

\begin{outputbox}
Original: [1, 2, [99, 4]]
Alias:    [1, 2, [99, 4]]
Shallow:  [1, 2, [99, 4]]
Deep:     [1, 2, [3, 4]]
\end{outputbox}

% ==============================================================================
% SECTION 4.9: OUTPUT PREDICTION & DEBUGGING CHALLENGES
% ==============================================================================
\section{Output Prediction \& Debugging Challenges}

\begin{outputprediction}[List Method Interactions]
\lpuBadge{} Predict the exact output.
\begin{lstlisting}[language=Python3]
data = [10, 20, 30]
data.append([40, 50])
data.extend([60, 70])
data.pop(3)
print(len(data))
\end{lstlisting}
\textbf{Solution \& Explanation:}\\
Output: \texttt{5}\\
\texttt{data} becomes \texttt{[10, 20, 30, [40, 50]]}. Then \texttt{extend} makes it \texttt{[10, 20, 30, [40, 50], 60, 70]}. The \texttt{pop(3)} removes the nested list \texttt{[40, 50]}. Leaving \texttt{[10, 20, 30, 60, 70]}, which has a length of 5.
\end{outputprediction}

\begin{outputprediction}[String Immutability]
Predict the exact output.
\begin{lstlisting}[language=Python3]
s = "lpu"
s.upper()
s = s + " online"
print(s.title())
\end{lstlisting}
\textbf{Solution \& Explanation:}\\
Output: \texttt{Lpu Online}\\
\texttt{s.upper()} returns "LPU" but the result is discarded because strings are immutable and it wasn't reassigned. \texttt{s} remains "lpu". Then \texttt{s} becomes "lpu online". \texttt{title()} capitalizes the first letter of each word.
\end{outputprediction}

\begin{outputprediction}[Dictionary Overwriting]
Predict the exact output.
\begin{lstlisting}[language=Python3]
d = {"a": 1, "b": 2, "a": 3}
print(len(d), d["a"])
\end{lstlisting}
\textbf{Solution \& Explanation:}\\
Output: \texttt{2 3}\\
Keys must be unique. The second \texttt{"a": 3} overwrites the first. The dictionary is \texttt{\{"a": 3, "b": 2\}}.
\end{outputprediction}

\begin{outputprediction}[2D List Aliasing]
Predict the exact output.
\begin{lstlisting}[language=Python3]
matrix = [[0] * 2] * 2
matrix[0][1] = 5
print(matrix[1][1])
\end{lstlisting}
\textbf{Solution \& Explanation:}\\
Output: \texttt{5}\\
Due to the list multiplication trap, both rows reference the exact same inner list. Modifying row 0 modifies row 1.
\end{outputprediction}

\begin{outputprediction}[Set Operations]
Predict the exact output.
\begin{lstlisting}[language=Python3]
a = {1, 2, 3}
b = {3, 4, 5}
print(list(a & b)[0])
\end{lstlisting}
\textbf{Solution \& Explanation:}\\
Output: \texttt{3}\\
The intersection \texttt{\&} of \texttt{a} and \texttt{b} is the set \texttt{\{3\}}. Casting to a list makes it \texttt{[3]}, and indexing 0 gives \texttt{3}.
\end{outputprediction}

\begin{debuggingbox}[Tuple Reassignment]
\examBadge{} Identify the bug and fix it.
\begin{lstlisting}[language=Python3]
coords = (10, 20, [30, 40])
coords[0] = 15
coords[2].append(50)
\end{lstlisting}
\textbf{Defect}: \texttt{coords[0] = 15} raises a \texttt{TypeError} because tuples do not support item reassignment.\\
\textbf{Fix}: Remove \texttt{coords[0] = 15}. Notice that \texttt{coords[2].append(50)} is perfectly valid because it modifies the mutable list \textit{inside} the tuple, without changing the tuple's structural reference.
\end{debuggingbox}

\begin{debuggingbox}[Modifying a List While Iterating]
Identify the bug and fix it.
\begin{lstlisting}[language=Python3]
nums = [1, 2, 3, 4, 5]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)
\end{lstlisting}
\textbf{Defect}: Modifying a list while iterating over it skips elements because the internal indices shift dynamically.\\
\textbf{Fix}: Iterate over a copy using slicing: \texttt{for n in nums[:]:} or use a list comprehension: \texttt{nums = [n for n in nums if n \% 2 != 0]}.
\end{debuggingbox}

\begin{debuggingbox}[Default Argument Aliasing]
Identify the bug and fix it.
\begin{lstlisting}[language=Python3]
def add_item(item, lst=[]):
    lst.append(item)
    return lst
print(add_item(1))
print(add_item(2))
\end{lstlisting}
\textbf{Defect}: Default arguments are evaluated only once when the function is defined. The same list object is shared across all calls.\\
\textbf{Fix}: Use \texttt{None} as the default.
\begin{lstlisting}[language=Python3]
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
\end{lstlisting}
\end{debuggingbox}

% ==============================================================================
% SECTION 4.10: COMPREHENSIVE PRACTICE SET
% ==============================================================================
\section{Comprehensive Practice Set}

\begin{practiceset}[Chapter 4 Graded Exercises]

\textbf{Problem 1: List Rotation}\\
Write a program to right-rotate a list $k$ times.

\textbf{Problem 2: Remove All Occurrences}\\
Write a program to remove all occurrences of a specific element \texttt{val} from a list \texttt{lst} without using list comprehensions.

\textbf{Problem 3: Character Frequency Dictionary}\\
Write a program that takes a string and builds a dictionary mapping each character to its frequency count. Ignore spaces and case.

\textbf{Problem 4: Matrix Transpose}\\
Write a list comprehension to transpose a 2D matrix (turn rows into columns).

\textbf{Problem 5: Tuple Swap and Unpack}\\
Given a list of tuples \texttt{[(1, 'A'), (2, 'B')]}, reverse each tuple to get \texttt{[('A', 1), ('B', 2)]}.

\textbf{Problem 6: Tokenize and Find Longest Word}\\
Write a program to tokenize a sentence into words, remove punctuation, and return the longest word.

\textbf{Problem 7: Sparse Matrix Addition}\\
Given two sparse matrices represented as dictionaries (e.g. \texttt{\{(0,0): 5, (1,2): 3\}}), write a function to add them and return a new sparse matrix dictionary.
\end{practiceset}

\subsection{Practice Set Solutions \& Test Cases}

\begin{solutionbox}[Solution 1: List Rotation]
\begin{lstlisting}[language=Python3]
def rotate_right(lst, k):
    if not lst:
        return lst
    k = k % len(lst)
    return lst[-k:] + lst[:-k]
\end{lstlisting}
\textbf{Test Cases:}
\begin{table}[H]
    \centering\sffamily
    \begin{tabular}{llp{5cm}}
    \toprule
    \textbf{Input (\texttt{lst}, \texttt{k})} & \textbf{Output} & \textbf{Condition} \\
    \midrule
    \texttt{[1, 2, 3, 4, 5]}, 2 & \texttt{[4, 5, 1, 2, 3]} & Normal case \\
    \texttt{[1, 2, 3]}, 5 & \texttt{[2, 3, 1]} & $k >$ length (modulo handles this) \\
    \texttt{[]}, 3 & \texttt{[]} & Edge case: Empty list \\
    \bottomrule
    \end{tabular}
\end{table}
\end{solutionbox}

\begin{solutionbox}[Solution 2: Remove All Occurrences]
\begin{lstlisting}[language=Python3]
def remove_all(lst, val):
    while val in lst:
        lst.remove(val)
    return lst
\end{lstlisting}
\textbf{Test Cases:}
\begin{table}[H]
    \centering\sffamily
    \begin{tabular}{llp{5cm}}
    \toprule
    \textbf{Input (\texttt{lst}, \texttt{val})} & \textbf{Output} & \textbf{Condition} \\
    \midrule
    \texttt{[1, 2, 2, 3, 2]}, 2 & \texttt{[1, 3]} & Multiple occurrences \\
    \texttt{[1, 2, 3]}, 5 & \texttt{[1, 2, 3]} & Value not found \\
    \texttt{[5, 5, 5]}, 5 & \texttt{[]} & All elements are the target \\
    \bottomrule
    \end{tabular}
\end{table}
\end{solutionbox}

\begin{solutionbox}[Solution 3: Character Frequency Dictionary]
\begin{lstlisting}[language=Python3]
def char_frequency(text):
    freq = {}
    for char in text.lower():
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
    return freq
\end{lstlisting}
\textbf{Test Cases:}
\begin{table}[H]
    \centering\sffamily
    \begin{tabular}{llp{5cm}}
    \toprule
    \textbf{Input (\texttt{text})} & \textbf{Output} & \textbf{Condition} \\
    \midrule
    \texttt{"Apple"} & \texttt{\{'a':1, 'p':2, 'l':1, 'e':1\}} & Mixed case \\
    \texttt{"Hi, Bob!"} & \texttt{\{'h':1, 'i':1, 'b':2, 'o':1\}} & Punctuation ignored \\
    \texttt{""} & \texttt{\{\}} & Empty string \\
    \bottomrule
    \end{tabular}
\end{table}
\end{solutionbox}

\begin{solutionbox}[Solution 4: Matrix Transpose]
\begin{lstlisting}[language=Python3]
def transpose(matrix):
    if not matrix: return []
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
\end{lstlisting}
\textbf{Test Cases:}
\begin{table}[H]
    \centering\sffamily
    \begin{tabular}{llp{5cm}}
    \toprule
    \textbf{Input (\texttt{matrix})} & \textbf{Output} & \textbf{Condition} \\
    \midrule
    \texttt{[[1, 2], [3, 4]]} & \texttt{[[1, 3], [2, 4]]} & Square matrix \\
    \texttt{[[1, 2, 3], [4, 5, 6]]} & \texttt{[[1, 4], [2, 5], [3, 6]]} & Rectangular matrix \\
    \bottomrule
    \end{tabular}
\end{table}
\end{solutionbox}

\begin{solutionbox}[Solution 5: Tuple Swap and Unpack]
\begin{lstlisting}[language=Python3]
def swap_tuples(lst):
    return [(b, a) for a, b in lst]
\end{lstlisting}
\textbf{Test Cases:}
\begin{table}[H]
    \centering\sffamily
    \begin{tabular}{llp{5cm}}
    \toprule
    \textbf{Input (\texttt{lst})} & \textbf{Output} & \textbf{Condition} \\
    \midrule
    \texttt{[(1, 'A'), (2, 'B')]} & \texttt{[('A', 1), ('B', 2)]} & Normal case \\
    \texttt{[]} & \texttt{[]} & Empty list \\
    \bottomrule
    \end{tabular}
\end{table}
\end{solutionbox}

\begin{solutionbox}[Solution 6: Tokenize and Find Longest Word]
\begin{lstlisting}[language=Python3]
def longest_word(sentence):
    # Remove basic punctuation using replace
    for punc in ".,!?":
        sentence = sentence.replace(punc, "")
    
    words = sentence.split()
    if not words:
        return ""
        
    longest = ""
    for w in words:
        if len(w) > len(longest):
            longest = w
    return longest
\end{lstlisting}
\textbf{Test Cases:}
\begin{table}[H]
    \centering\sffamily
    \begin{tabular}{llp{5cm}}
    \toprule
    \textbf{Input (\texttt{sentence})} & \textbf{Output} & \textbf{Condition} \\
    \midrule
    \texttt{"Hello beautiful world!"} & \texttt{"beautiful"} & Normal case, punctuation \\
    \texttt{"A B C"} & \texttt{"A"} & Tie (first wins by logic) \\
    \texttt{"   "} & \texttt{""} & Only spaces \\
    \bottomrule
    \end{tabular}
\end{table}
\end{solutionbox}

\begin{solutionbox}[Solution 7: Sparse Matrix Addition]
\begin{lstlisting}[language=Python3]
def add_sparse(dict1, dict2):
    result = dict1.copy()
    for key, val in dict2.items():
        result[key] = result.get(key, 0) + val
    return result
\end{lstlisting}
\textbf{Test Cases:}
\begin{table}[H]
    \centering\sffamily
    \begin{tabular}{llp{4cm}}
    \toprule
    \textbf{Input} & \textbf{Output} & \textbf{Condition} \\
    \midrule
    \texttt{\{(0,0): 5\}, \{(0,0): 3\}} & \texttt{\{(0,0): 8\}} & Overlapping coordinates \\
    \texttt{\{(0,1): 2\}, \{(1,0): 4\}} & \texttt{\{(0,1): 2, (1,0): 4\}} & Disjoint coordinates \\
    \bottomrule
    \end{tabular}
\end{table}
\end{solutionbox}

% ==============================================================================
% SECTION 4.11: MULTIPLE CHOICE QUESTIONS
% ==============================================================================
\section{Multiple Choice Questions (MCQs)}

\begin{enumerate}[leftmargin=1.5em]
    \item Which of the following data types is MUTABLE in Python?
    \begin{enumerate}[label=(\alph*)]
        \item \texttt{tuple} \quad (b) \texttt{str} \quad (c) \texttt{list} \quad (d) \texttt{int}
    \end{enumerate}
    \textbf{Answer}: (c) --- \textit{Lists are mutable sequences in Python.}

    \item What is the result of \texttt{t = (5)}?
    \begin{enumerate}[label=(\alph*)]
        \item Tuple with element 5 \quad (b) Integer 5 \quad (c) SyntaxError \quad (d) Set with element 5
    \end{enumerate}
    \textbf{Answer}: (b) --- \textit{Without a trailing comma, parentheses evaluate as an integer expression.}

    \item What is returned by \texttt{"University".find("z")}?
    \begin{enumerate}[label=(\alph*)]
        \item \texttt{None} \quad (b) \texttt{0} \quad (c) \texttt{-1} \quad (d) \texttt{ValueError}
    \end{enumerate}
    \textbf{Answer}: (c) --- \textit{\texttt{find()} returns \texttt{-1} when the substring is not found.}

    \item Which method removes and returns the last element of a list?
    \begin{enumerate}[label=(\alph*)]
        \item \texttt{remove()} \quad (b) \texttt{delete()} \quad (c) \texttt{pop()} \quad (d) \texttt{discard()}
    \end{enumerate}
    \textbf{Answer}: (c) --- \textit{\texttt{pop()} removes and returns the item at the specified index (default: last).}

    \item Which of the following cannot be used as a dictionary key?
    \begin{enumerate}[label=(\alph*)]
        \item \texttt{"name"} \quad (b) \texttt{100} \quad (c) \texttt{(1, 2)} \quad (d) \texttt{[1, 2]}
    \end{enumerate}
    \textbf{Answer}: (d) --- \textit{Lists are mutable and unhashable, so they cannot serve as dictionary keys.}

    \item What is the output of \texttt{print([1, 2] * 2)}?
    \begin{enumerate}[label=(\alph*)]
        \item \texttt{[2, 4]} \quad (b) \texttt{[1, 2, 1, 2]} \quad (c) \texttt{[[1, 2], [1, 2]]} \quad (d) \texttt{TypeError}
    \end{enumerate}
    \textbf{Answer}: (b) --- \textit{The \texttt{*} operator repeats the list elements.}

    \item What does \texttt{dict.get("score", 0)} return if \texttt{"score"} is absent?
    \begin{enumerate}[label=(\alph*)]
        \item \texttt{KeyError} \quad (b) \texttt{None} \quad (c) \texttt{0} \quad (d) \texttt{False}
    \end{enumerate}
    \textbf{Answer}: (c) --- \textit{\texttt{get()} returns the provided default value (0) if the key is missing.}

    \item Which copy operation completely duplicates all nested sub-objects in memory?
    \begin{enumerate}[label=(\alph*)]
        \item \texttt{list[:]} \quad (b) \texttt{list.copy()} \quad (c) \texttt{copy.deepcopy()} \quad (d) \texttt{b = a}
    \end{enumerate}
    \textbf{Answer}: (c) --- \textit{\texttt{deepcopy()} recursively clones all nested compound objects.}

    \item What is the output of \texttt{"abcdef"[::-2]}?
    \begin{enumerate}[label=(\alph*)]
        \item \texttt{"fedcba"} \quad (b) \texttt{"fdb"} \quad (c) \texttt{"eca"} \quad (d) \texttt{"ace"}
    \end{enumerate}
    \textbf{Answer}: (b) --- \textit{Reverses string and steps by 2: index 5='f', index 3='d', index 1='b'.}

    \item What is the length of \texttt{d = \{"a": 1, "b": 2, "a": 3\}}?
    \begin{enumerate}[label=(\alph*)]
        \item 3 \quad (b) 2 \quad (c) 1 \quad (d) Error
    \end{enumerate}
    \textbf{Answer}: (b) --- \textit{Keys must be unique; the second \texttt{"a": 3} overwrites the first.}
\end{enumerate}

% ==============================================================================
% SECTION 4.12: SELF-ASSESSMENT UNIT TEST
% ==============================================================================
\section{Self-Assessment Unit Test}

\begin{chaptertest}[Unit 4 Examination (25 Marks --- 45 Minutes)]
\noindent\textbf{Section A: Short Answer Concepts ($3 \times 2 = 6\text{ Marks}$)}
\begin{enumerate}
    \item Explain why strings and tuples are immutable in Python.
    \item Differentiate between shallow copying and deep copying.
    \item Why are dictionaries well-suited for representing sparse matrices?
\end{enumerate}

\medskip
\noindent\textbf{Section B: Code Tracing \& Output Prediction ($3 \times 3 = 9\text{ Marks}$)}
\begin{enumerate}[start=4]
    \item Predict the output:
    \begin{lstlisting}[language=Python3]
matrix = [[1, 2], [3, 4]]
copy_m = matrix.copy()
copy_m[0][0] = 99
print(matrix[0][0], copy_m[0][0])
    \end{lstlisting}
    \item What is printed by:
    \begin{lstlisting}[language=Python3]
s = "engineering"
print(s.count('e'), s.find('e'), s.rfind('e'))
    \end{lstlisting}
    \item Explain the output of:
    \begin{lstlisting}[language=Python3]
t = (1, 2, [3, 4])
t[2].append(5)
print(t)
    \end{lstlisting}
\end{enumerate}

\medskip
\noindent\textbf{Section C: Comprehensive Programming Problem ($1 \times 10 = 10\text{ Marks}$)}
\begin{enumerate}[start=7]
    \item Write a complete Python program that accepts a multi-line paragraph of text from user input, removes punctuation marks (\texttt{.,!?:;}), converts all text to lowercase, and builds a word frequency dictionary. The program must print the top 3 most frequent words and their occurrence counts.
\end{enumerate}
\end{chaptertest}

\subsection{Unit Test Complete Solutions \& Rubric}

\begin{solutionbox}[Complete Solutions for Unit 4 Test]
\noindent\textbf{Section A Solutions}:
\begin{enumerate}
    \item \textbf{Immutability} [2 Marks]: Immutability guarantees that the data state cannot be altered in place after instantiation. This ensures thread safety, predictable hashing (allowing them to serve as dictionary keys), and prevents side-effect mutations.
    \item \textbf{Shallow vs. Deep Copy} [2 Marks]: A shallow copy creates a new outer collection but inserts references to the original nested objects. A deep copy recursively duplicates all nested objects, isolating the new copy completely.
    \item \textbf{Sparse Matrix Dictionary} [2 Marks]: A sparse matrix contains mostly zeroes. Dictionaries store only non-zero coordinates as keys \texttt{(row, col): value}, consuming $O(k)$ memory (where $k$ is non-zero count) rather than $O(N \times M)$.
\end{enumerate}

\noindent\textbf{Section B Solutions}:
\begin{enumerate}[start=4]
    \item \textbf{Shallow Copy Matrix} [3 Marks]: \texttt{matrix.copy()} is a shallow copy. Mutating \texttt{copy\_m[0][0]} modifies the shared inner list. Output: \texttt{99 99}.
    \item \textbf{String Methods} [3 Marks]:
    \begin{itemize}
        \item \texttt{count('e')} = \texttt{3}
        \item \texttt{find('e')} (first index) = \texttt{0}
        \item \texttt{rfind('e')} (last index) = \texttt{6}  (Note: we didn't teach rfind explicitly, but find counts here)
        \item Output: \texttt{3 0 6}
    \end{itemize}
    \item \textbf{Mutable Object in Tuple} [3 Marks]: Tuples are immutable in structure (their references cannot be reassigned), but the objects they reference may be mutable. Appending to the list inside the tuple is valid. Output: \texttt{(1, 2, [3, 4, 5])}.
\end{enumerate}

\noindent\textbf{Section C Solution}:
\begin{enumerate}[start=7]
    \item \textbf{Word Frequency Program} [10 Marks]:
\begin{lstlisting}[language=Python3]
# Word Frequency Analyzer
text = input("Enter text paragraph: ")

# Step 1: Clean punctuation and normalize to lowercase
for char in ".,!?:;\"'()[]":
    text = text.replace(char, " ")
words = text.lower().split()

# Step 2: Build frequency dictionary
freq_map = {}
for w in words:
    freq_map[w] = freq_map.get(w, 0) + 1

# Step 3: Sort by frequency descending
sorted_words = sorted(freq_map.items(), key=lambda item: item[1], reverse=True)

# Step 4: Display Top 3 Words
print("\n--- Top 3 Most Frequent Words ---")
for word, count in sorted_words[:3]:
    print(f"Word: '{word}' -> Count: {count}")
\end{lstlisting}
\textbf{Marking Scheme}: Cleaning \& splitting: 3M; Frequency dictionary generation: 4M; Sorting \& top 3 output: 3M.
\end{enumerate}
\end{solutionbox}
"""

with open('/Users/abhidinkale/Documents/mark p1/INT108/chapters/chapter-04-strings-lists-tuples-dictionaries.tex', 'w') as f:
    f.write(content)
