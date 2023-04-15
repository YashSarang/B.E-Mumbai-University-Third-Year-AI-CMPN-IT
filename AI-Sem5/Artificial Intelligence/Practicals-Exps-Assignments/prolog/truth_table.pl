and(A, B) :- A, B.

evaluate(E, true) :- E, !.
evaluate(_, false).

bool(true).
bool(false).

tableBody(A,B,E) :-
  bool(A),
  bool(B),
  write(A),
  write(' \t '),
  write(B),
  write(' \t '),
  evaluate(E, Result),
  write(Result),nl, fail.
