
(deffacts my_facts "Database"
   (A TRUE)
   (B TRUE)
   (C TRUE)
   (D TRUE)
   (E TRUE))

 (defrule Rule1
	(Y TRUE)
	(D TRUE)
	=>
	(assert (Z TRUE))
	(printout t "Z is true" crlf))

(defrule Rule2
	(X TRUE)
	(B TRUE)
	(E TRUE)
	=>
	(assert (Y TRUE))
	(printout t "Y is true" crlf))

(defrule Rule3
	(A TRUE)
	=>
	(assert (X TRUE))
	(printout t "X is true" crlf))