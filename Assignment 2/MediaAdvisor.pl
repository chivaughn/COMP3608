environment(machines).
job(repairing).
feedback(required).

prove(_workshop):- r3(stimulus_situation), r6(stimulus_response), r9(feedback),
  write("medium is workshop"), nl.

r3(stimulus_situation):-
  write('What sort of environment is a trainee dealing with on the job?'),
  nl,
  read(X),
  environment(X).

  r6(stimulus_response):-
    write('In what way is a trainee expected to act or respond on the job?'),
    nl,
    read(X),
    job(X).

  r9(feedback):-
    write("Is feedback on the trainee's progress required during training?"),
    nl,
    read(X),
    feedback(X).
