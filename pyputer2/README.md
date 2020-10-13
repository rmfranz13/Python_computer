# Second attempt at the same thing.

Issue with 1st attempt: The literal 1's and 0's were member variables
of each chip. However, it is clear now that each 1 and 0 should exist
on it's own, independent of the chip. This is because, when wiring 
chips together, if I set an input pin of one chip to the output pin 
of another, without a pin being it's own object, the input pin will
merely hold whatever value the output pin had at the time of assignment.
With each pin being it's own object, each chip will have a reference to that
"physical" pin object, thus it'll always be up-to-date.

Additionally, each object will live in it's own file, named after the object,
rather than having large files of related objects.