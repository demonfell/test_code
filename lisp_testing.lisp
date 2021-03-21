(+ 1 1)

;; abs function from sicp video
(defun my-abs (x)
     (if (< x 0)
            (- x)
            (x)))

;; ert for testing

;; loop through a list
(setq jamie-list '(1 2 3 4))
(dolist (element jamie-list)
  (when (= (mod element 2) 0)
    (print element)))

(let (some-var)
  (when (null some-var)
    (message "var is null")))

;; first is the value if it's true, and next the value if it's false
(let ((some-var 0)
  (other-var 90))
(if (null some-var)
    (message "Not supposed to happen.")
  (message "Yay!")))

 (setq jamie-list '(1 2 3 4))
  
(defun sum-evens (some-list)
    (let ((sum 0))
    (dolist (element some-list)
      (when (= (mod element 2) 0)
      (setq sum (+ sum element))))
    sum))

(sum-evens jamie-list)

;; test
(require 'ert)
(ert-deftest sum-evens-test ()
  (should (= (sum-evens '(1 3 5)) 0))
  (should (= (sum-evens '(2 4 6)) 12)))
  

(defun cheap-count-words ()
  (interactive)
  (let ((words 0))
    (save-excursion
      (goto-char (point-min))
      (while (forward-word)
	(setq words (1+ words))))
    (message (format "Words in buffer: %s" words))
    words))

(ert-deftest count-words-test ()
  (get-buffer-create "*test*")
  (with-current-buffer "*test*"
    (erase-buffer)
    (insert "Hello World")
    (should (= (cheap-count-words) 2))
    )
    (kill-buffer "*test*"))
 
