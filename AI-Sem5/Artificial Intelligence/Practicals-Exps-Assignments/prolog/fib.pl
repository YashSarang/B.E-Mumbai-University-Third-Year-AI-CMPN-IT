:- dynamic(stored/1).
memo(Goal) :-
stored(Goal) -> true;
Goal, assertz(stored(Goal)).

fib(1,1) :- !, write('1, ').
fib(2,1) :- !, write('1, ').
fib(N,F) :-
N1 is N-1, memo(fib(N1,F1)),
N2 is N-2, memo(fib(N2,F2)),
F is F1 + F2,
write(F), write(', ').
