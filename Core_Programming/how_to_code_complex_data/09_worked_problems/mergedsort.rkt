;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname mergedsort) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))


;; Signature
;; (listof Number) -> (listofNumber)

;; Purpose
;; consume a list of number and produce a sorted list of number using mergesort algorithm.

;; Example
(check-expect (mergeSort empty) empty)
(check-expect (mergeSort (list 1)) (list 1))
(check-expect (mergeSort (list 2 1)) (list 1 2))
(check-expect (mergeSort (list 3 1 2 4)) (list 1 2 3 4))

;; Stub
(define (mergeSort list) empty)

;; Template
(define (mergeSort list) (
                          (define (mergeSort list) (
                                                    cond
                                                     [(< (length list) 2) list]
                                                     [else (
                                                            merge (mergeSort (split list "left")) (mergeSort(split list "right"))
                                                            )]
                                                    ))
                          (define (merge listA listB) (

                                                       ))

                          (define (split list side) (
                                                     
                                                     ))
                          ))