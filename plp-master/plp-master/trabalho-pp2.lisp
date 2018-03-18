;1a questão da lista
(defun lista(entrada)(cond((eq entrada nil)"fim ou lista vazia") 
			     ((pprint entrada)) ((lista(cdr entrada)))
			     )
	)


;2a questão da lista
(defun fat (n) "Calc fatorial de um numero"
	(if (<= n 0)
		1
		(* n (fat (- n 1)))
	)
)


(defun som (i) "Calc somatorio"
	(if(= i 0)
		0
		(+ (+ (/ (fat i) (+ i 1)) (- i 1))(som (- i 1))
	)
))
;3a questão da lista
(defun quadrado (x)
 	(* x x)
)

(defun calc_quad (lista) 
	(cond ((equal lista nil) 0) 
		((and (integerp (car lista)) (= (mod (car lista) 2) 0)) (+ (calc_quad (cdr lista)) (quadrado (car lista))))
		(t (calc_quad (cdr lista)))
		)
)


;4a questão da lista
(defun verifica (lista) 
	(cond ((equal lista nil) 0) 
		((integerp (car lista)) (+ 1 (verifica (cdr lista))))
		(t (verifica (cdr lista)))
	)
)

;5a questão da lista
(defun resultante(x y) (format t "A lista Resultante: ~S~%" (list (setq s(+ x y))(setq sub (- x y))(setq mult(* x y))(setq div(/ x y)))))
 
(defun ordena (s sub mult div) (format t "A lista Ordenada em forma Crescente:~S" (sort (cons s (cons sub (cons mult (cons div nil)))) #'<)))

(defun entrada () (print "Digite o primeiro valor: ") (setf x (read)) (print "Digite o segundo valor: ") (setf y (read)) (resultante x y) (ordena s sub mult div))
