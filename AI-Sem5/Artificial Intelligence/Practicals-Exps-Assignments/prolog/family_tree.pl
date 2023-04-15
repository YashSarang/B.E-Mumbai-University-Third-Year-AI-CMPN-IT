female(shruti).
female(bharati).
female(usha).
female(rukmini).
female(namrata).
female(geeta).
male(liladhar).
male(neel).
male(narayan).
male(babaji).
male(abhijeet).
male(hariom).
parent(liladhar,shruti).
parent(bharati,shruti).
parent(liladhar,neel).
parent(bharati,neel).
parent(narayan,bharati).
parent(usha,bharati).
parent(rukmini,liladhar).
parent(babaji,liladhar).
parent(narayan,abhijeet).
parent(usha,abhijeet).
parent(geeta,narayan).
parent(hariom,narayan).
mother(X,Y):- parent(X,Y),female(X).
father(X,Y):- parent(X,Y),male(X).
haschild(X):- parent(X,_).
sister(X,Y):- parent(Z,X),parent(Z,Y),female(X),X\==Y.
brother(X,Y):- parent(Z,X),parent(Z,Y),male(X),X\==Y.
grandparent(X,Y):- parent(X,Z),parent(Z,Y).
grandmother(X,Z):- mother(X,Y),parent(Y,Z).
grandfather(X,Z):- father(X,Y),parent(Y,Z).
wife(X,Y):- parent(X,Z),parent(Y,Z),female(X),male(Y).
uncle(X,Z):- brother(X,Y),parent(Y,Z).
predecessor(X, Z):- parent(X, Z).
predecessor(X, Z):- parent(X, Y),predecessor(Y, Z).
