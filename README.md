# Python_computer
This is an attempt to build a computer from first principles, roughly following the book ["The Elements of Computing Systems"](https://www.nand2tetris.org/) by Noam Nisan and Shimon Schocken, at least to get started. I highly recommed the book which literally explains every necessary detail.

While the book itself does not use Python, my goal is to re-build the architecture completely in Python, removing the need to understand the free software they provide (which is very useful if you are building the computer yourself and just want something that works, but not useful if you're a control freak like me who doesn't trust anyone (except Guido, the Benevolent)). At first, I plan to follow the book's instruction using only the fundamental Nand gate, but then optimizing using only Python built-ins and the Python standard library as needed to improve performance. Though optimizing away from the fundamental Nand gate is frowned upon because it is a disconnect in the understanding that any black box can be constructed from Nand, so perhaps when that bridge is crossed, there can be a 'proof that this black box can be implemented from Nand'-object, before using a more optimal solution. Additionally, this strict complience to Python is in effort to eliminate dependencies, so that anyone who can download Python can have the whole thing. The only exception is Tkinter, which is the most general gui kit I can find (works for everything except on mobile, I think). Maybe different guis could be developed for different platforms.

Everything is to be visible and accessible to an individual whose only tool is python, so there is no confusion or software troubles that can hinder a complete understanding of how a simple (yet not completely useless... hopefully) virtual computer works. From fundamental [logic gates](https://en.wikipedia.org/wiki/Logic_gate), to the [assembler](https://en.wikipedia.org/wiki/Assembly_language), to the [compiler](https://en.wikipedia.org/wiki/Compiler), to the [operating system](https://en.wikipedia.org/wiki/Operating_system), to high-level programming and games. It should make concrete all those low-level ideas that everyone pretends to understand. This virtual computer is not unlike a [cannulated cow](https://en.wikipedia.org/wiki/Cannulated_cow) of computers. 

Secondary goals are optimizing the system after it is built (still sticking to python built-ins) and possibly developing more sophisticated computer systems once the underlying architecture is fully understood. It would be very cool to eventually work out simplistic versions of popular operating systems like Windows or Linux, and could see this eventually turning into a crappy but easy-for-me-to-use-because-I-built-it virtual machine. Sky's the limit really. Let's see what python can do!
