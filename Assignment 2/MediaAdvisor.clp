(defrule start_1
    => (printout t "What sort of environment is a trainee dealing with on the job?" crlf)
       (bind ?enviro (read))
       (assert (the environment is ?enviro)))

(defrule start_2
	(the environment is ?eniviro)
    => (printout t "In what way is a trainee expected to act or respond on the job?" crlf)
       (bind ?work (read))
       (assert (the job is ?work)))


 (defrule start_3
	(the environment is ?eniviro)
	(the job is ?work)
    => (printout t "Is feedback on the trainee’s progress required during training?" crlf)
       (bind ?isrequired (read))
       (assert (feedback is ?isrequired)))


(defrule Rule_1
	(or (or (or (the environment is papers)
				(the environment is manuals))
				(the environment is documents))
				(the environment is textbooks))
	=>
	(assert (the stimulus_situation is verbal)))

(defrule Rule_2
	(or (or (or (the environment is pictures)
				(the environment is illustrations))
				(the environment is photographs))
				(the environment is diagrams))
	=>
	(assert (the stimulus_situation is visual)))

(defrule Rule_3
	(or (or (the environment is machines)
			(the environment is buildings))
			(the environment is tools))
	=>
	(assert (the stimulus_situation is 'physical object')))


(defrule Rule_4
	(or (or (the environment is numbers)
			(the environment is formulas))
			(the environment is 'computer programs'))
	=>
	(assert (the stimulus_situation is symbolic)))

(defrule Rule_5
	(or (or (the job is lecturing)
			(the job is advising))
			(the job is counselling))
	=>
	(assert (the stimulus_response is oral)))

(defrule Rule_6
	(or (or (the job is building)
			(the job is repairing))
			(the job is troubleshooting))
	=>
	(assert (the stimulus_response is 'hands-on')))

(defrule Rule_7
	(or (or (the job is writing)
			(the job is typing))
			(the job is drawing))
	=>
	(assert (the stimulus_response is documented)))

(defrule Rule_8
	(or (or (the job is evaluating)
			(the job is reasoning))
			(the job is investigating))
	=>
	(assert (the stimulus_response is analytical)))

(defrule Rule_9
	(the stimulus_situation is 'physical object')
	(the stimulus_response is 'hands-on')
	(feedback is required)
	=>
	(assert (medium is workshop))
	(printout t "medium is workshop" crlf))