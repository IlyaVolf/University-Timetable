from pyswip import Prolog

prolog = Prolog()
prolog.consult("main.pl")
# q = prolog.query("main(1).")
# print(sorted(q))
print(list(prolog.query("main(1).")))
