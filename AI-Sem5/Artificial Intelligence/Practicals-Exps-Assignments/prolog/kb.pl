likes(john,X) :- food(X).
food(apple).
food(X) :- vegetable(X).
food(X) :- eats(P,X), alive(P).
alive(anil).
eats(anil,peanuts).
eats(harry,X) :- eats(anil,X).
