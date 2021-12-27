perm([H|T],Permutation):-
    findall(A,permutation([H|T],A),List),
    length(List,Length),
    Random is random(Length),
    Random > 0,
    nth1(Random,List,Permutation),!.


main :- nth0(2,[1,2,3,4],X), writeln(X).