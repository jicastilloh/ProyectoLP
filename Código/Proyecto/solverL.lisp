;; autor: Junior Castillo - jicastilloh@unah.hn
;; version: 0.0.3

(defvar texto (second *posix-argv*)) ;; La variable texto guarda la información que se pasó como parámetro


;; Defino una función que recibe una cadena de texto, lee cada línea de dicho texto, crea la estructura del programa `solverP.pl` y luego crea el programa insertando cada línea.
(defun leer_texto (cadena)
  ;; Defino una lista la cual va a contener la estructura de cada línea del programa `solverP.pl`
  (let 
    (
      (line (read-line cadena nil))
      (nueva_linea (list "found(" ").")) ;; Defino una lista la cual va a contener la estructura de cada línea del programa `solverP.pl`
    )
    (when line 
      ;; Actualizo la variable 'nueva_linea' en una cadena con formato que va a contener los elementos que tenía anteriormente como una lista                    
      (setq nueva_linea (format nil "~a~a~a" (car nueva_linea) line (car (reverse nueva_linea))))
      
      ;; Abro el archivo 'solverP.pl' en modo escritura, si no existe lo creará, si existe agregará el texto que contiene la variable 'nueva_linea'
      (with-open-file (stream "solverP.pl" :direction :output :if-exists :append :if-does-not-exist :create)
        (write-line nueva_linea stream))
      (leer_texto cadena)
    )
  )
)

(leer_texto (make-string-input-stream texto))