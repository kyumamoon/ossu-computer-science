;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname mergedsortV2) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
;; Merge Sort

;; Signature
;; listof Number -> listof Number

;; Purpose
;; consumes a list and produce a list in ascending order using merge sort algorithm.

;; Examples
(check-expect (merge-sort empty) empty)
(check-expect (merge-sort (list 2)) (list 2))
(check-expect (merge-sort (list 1 2)) (list 1 2))
(check-expect (merge-sort (list 4 3)) (list 3 4))
(check-expect (merge-sort (list 6 5 3 1 8 7 2 4)) (list 1 2 3 4 5 6 7 8))

;; Stub
;(define (merge-sort lon) lon)

;; Template
;; template according to generative recursion

(define (merge-sort lon) (
                          cond
                           [(empty? lon) empty]
                           [(empty? (rest lon)) lon]
                           [else (
                                  merge
                                  (merge-sort (take lon (quotient (length lon) 2)))
                                  (merge-sort (drop lon (quotient (length lon) 2)))
                                  )]
                          ))


;; (listof Number) (listof Number) -> (listof Number)
(check-expect (merge (list 1 2) (list 3 4)) (list 1 2 3 4))
(check-expect (merge (list 1 2) (list 3 4 5)) (list 1 2 3 4 5))
(check-expect (merge (list 3 4) (list 1 2)) (list 1 2 3 4))
(check-expect (merge (list 2) (list 1)) (list 1 2))
(check-expect (merge (list 2 3) (list 1)) (list 1 2 3))

(define (merge list1 list2) (
                             local
                              [
                               (define (merge list1 list2 answer) (
                                                                   cond
                                                                   [(empty? list1) (append answer list2)]
                                                                   [(empty? list2) (append answer list1)]
                                                                   [else (
                                                                          if
                                                                          (< (first list1) (first list2))
                                                                          (merge (rest list1) list2 (append answer (cons (first list1) empty)))
                                                                          (merge list1 (rest list2) (append answer (cons (first list2) empty)))
                                                                          )]
                                                                   ))
                               ]
                              (merge list1 list2 empty)
                             ))

(define (take list length) (
                            local
                             [
                              (define (take list index answer) (
                                                         if
                                                         (equal? index length)
                                                         answer
                                                         (take (rest list) (add1 index) (append answer (cons (first list) empty)))
                                                                ))
                              ]
                             (take list 0 empty)
                            ))

(define (drop list length) (
                            local
                             [
                              (define (drop list index answer) (
                                                                cond
                                                                 [(empty? list) answer]
                                                                 [else (
                                                                        if
                                                                        (>= index length)
                                                                        (drop (rest list) (add1 index) (append answer (cons (first list) empty)))
                                                                        (drop (rest list) (add1 index) answer)
                                                                        )]
                                                                ))
                              ]
                             (drop list 0 empty)
                            ))