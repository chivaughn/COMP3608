d(_A). d(_B). d(_C). d(_D). d(_E).


prove(_Z) :- r2(_Y), d(_D),
	write("Rule 1: Y & D -> Z"), nl, !. % cut operator

r2(_Y) :- r3(_X), d(_B), d(_E),
	write("Rule 2: X & B & E -> Y"), nl.

r3(_X) :- d(_A),
	write("Rule 3: A -> X"), nl.

r4(_L) :- d(_C),
	write("Rule 3: C -> L"), nl.

r5(_N) :- d(_L), d(_M),
	write("Rule 3: L & M -> N"), nl.
