;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname ta-solver-starter) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
;; ta-solver-starter.rkt



;  PROBLEM 1:
;
;  Consider a social network similar to Twitter called Chirper. Each user has a name, a note about
;  whether or not they are a verified user, and follows some number of people.
;
;  Design a data definition for Chirper, including a template that is tail recursive and avoids
;  cycles.
;
;  Then design a function called most-followers which determines which user in a Chirper Network is
;  followed by the most people.
;

(define-struct chirper (name verified following))
;; chirper is a user (make-Chirper string boolean (listof Chirper)
;; Interp. the chirper's name, verification status, and the people they follow.

;; Examples
(define C1 (make-chirper "BOB" true (list (make-chirper "STAN" true empty))))
(define C2 (make-chirper "STAN" true empty))
(define C3
  (shared ((-A- (make-chirper "BOB" true (list -B-)))
           (-B- (make-chirper "STAN" true empty)))
    -A-))
(define C4
  (shared ((-A- (make-chirper "BOB" true (list -B- -C-)))
           (-B- (make-chirper "STAN" true (list -C-)))
           (-C- (make-chirper "POT" true (list -A-)))
           )
    -A-))

;; Template
#;(define (fn-for-chirper chirper) (
                                    local
                                     [
                                      (define (fn-for-chirper chirper todo visited tail) (
                                                                                          (...
                                                                                           (chirper-name)
                                                                                           (chirper-verified)
                                                                                           fn-for-loc (append (chirper-following) todo) (cons (chirper) todo) tail
                                                                                           )
                                                                                          ))
                                      (define (fn-for-loc todo visited tail) (
                                                                              cond
                                                                               [(empty? todo) ...]
                                                                               [else (
                                                                                      fn-for-chirper (first todo) (rest todo)
                                                                                                     )]
                                                                               ))
                                      ]
                                     (fn-for-chirper chirper empty empty)
                                     ))

;; Signature
;; chirper -> chirper

;; Purpose
;; consume a chirper and produce the chirper that has the most followers

;; Examples
;;

;; Stub
;;

(define-struct collection (name listofFollowers))

;; Template
(define (most-followers chirper) (
                                  local
                                   [
                                    (define (fn-for-chirper chirper todo visited previous collection) (
                                                                                                       cond
                                                                                                        [(member (chirper-name chirper) visited) (
                                                                                                                                                  local
                                                                                                                                                   [
                                                                                                                                                    (define (getChirperCollection chirper collection) (
                                                                                                                                                                                                       cond
                                                                                                                                                                                                        [(empty? collection) false] ;; impossible
                                                                                                                                                                                                        [(string=? (chirper-name chirper) (collection-name (first collection))) (first collection)]
                                                                                                                                                                                                        [else (getChirperCollection chirper (rest collection))]       
                                                                                                                                                                                                        ))
                                                                                                                                                    (define chirperCollection (getChirperCollection chirper collection)) ;; find and gets the Room's Collection (make-collection String listofString)
                                                                                                                                                    (define (updateMainCollection collection chirperCollection) (
                                                                                                                                                                                                                 local
                                                                                                                                                                                                                  [
                                                                                                                                                                                                                   (define (updateMainCollection previousList collection chirperCollection) (
                                                                                                                                                                                                                                                                                             cond
                                                                                                                                                                                                                                                                                              [(empty? collection) (append previousList collection)]
                                                                                                                                                                                                                                                                                              [(string=? (collection-name chirperCollection) (collection-name (first collection))) (append previousList (list (make-collection (collection-name chirperCollection) (append (list previous) (collection-listofFollowers chirperCollection)))) (rest collection))]
                                                                                                                                                                                                                                                                                              [else (updateMainCollection (cons (first collection) previousList) (rest collection) chirperCollection)]
                                                                                                                                                                                                                                                                                              ))
                                                                                                                                                                                                                   ]
                                                                                                                                                                                                                  (updateMainCollection empty collection chirperCollection)      
                                                                                                                                                                                                                  ))
                                                                                                                                                    ]
                                                                                                                                                   (
                                                                                                                                                    if
                                                                                                                                                    (member previous (collection-listofFollowers chirperCollection)) ;; if previous in room's list 
                                                                                                                                                    (fn-for-lor todo visited (chirper-name chirper) collection) ;; true, skip
                                                                                                                                                    (fn-for-lor todo visited (chirper-name chirper) (updateMainCollection collection chirperCollection)) ;; false, add previous to room's collection, update collections list
                                                                                                                                                    )
                                                                                                                                                   )]
                                                                                                        [else (
                                                                                                               if
                                                                                                               (false? previous) ; check if at starting root
                                                                                                               (fn-for-lor (append (chirper-following chirper) todo) (cons (chirper-name chirper) visited) (chirper-name chirper) (append (list (make-collection (chirper-name chirper) empty)) collection))
                                                                                                               (fn-for-lor (append (chirper-following chirper) todo) (cons (chirper-name chirper) visited) (chirper-name chirper) (append (list (make-collection (chirper-name chirper) (list previous))) collection))
                                                                                                               )]
                                                                                                        ))
                                    (define (fn-for-lor todo visited previous collection) (
                                                                                           cond
                                                                                            [(empty? todo) (findMost collection)] ; collection
                                                                                            [else (
                                                                                                   fn-for-chirper (first todo) (rest todo) visited previous collection
                                                                                                                  )]
                                                                                            ))

                                    (define (findMost collection) (
                                                                   local
                                                                    [
                                                                     (define (findMost collection topRoom) (
                                                                                                            cond
                                                                                                             [(empty? collection) topRoom]
                                                                                                             [(>= (length (collection-listofFollowers (first collection))) (length (chirper-following topRoom))) (findMost (rest collection) (make-chirper (collection-name (first collection)) true (collection-listofFollowers (first collection))))]
                                                                                                             [ else (findMost (rest collection) topRoom)]
                                                                                                             ))
                                                                     ]
                                                                    (findMost collection (make-chirper "empty" true empty))
                                                                    ))
                                    ]
                                   (fn-for-chirper chirper empty empty false empty)
                                   ))


;  PROBLEM 2:
;
;  In UBC's version of How to Code, there are often more than 800 students taking
;  the course in any given semester, meaning there are often over 40 Teaching Assistants.
;
;  Designing a schedule for them by hand is hard work - luckily we've learned enough now to write
;  a program to do it for us!
;
;  Below are some data definitions for a simplified version of a TA schedule. There are some
;  number of slots that must be filled, each represented by a natural number. Each TA is
;  available for some of these slots, and has a maximum number of shifts they can work.
;
;  Design a search program that consumes a list of TAs and a list of Slots, and produces one
;  valid schedule where each Slot is assigned to a TA, and no TA is working more than their
;  maximum shifts. If no such schedules exist, produce false.
;
;  You should supplement the given check-expects and remember to follow the recipe!



;; Slot is Natural
;; interp. each TA slot has a number, is the same length, and none overlap

(define-struct ta (name max avail))
;; TA is (make-ta String Natural (listof Slot))
;; interp. the TA's name, number of slots they can work, and slots they're available for

(define SOBA (make-ta "Soba" 2 (list 1 3)))
(define UDON (make-ta "Udon" 1 (list 3 4)))
(define RAMEN (make-ta "Ramen" 1 (list 2)))
(define COOKIE (make-ta "Cookie" 1 (list 1)))

(define NOODLE-TAs (list SOBA UDON RAMEN))



(define-struct assignment (ta slot))
;; Assignment is (make-assignment TA Slot)
;; interp. the TA is assigned to work the slot

;; Schedule is (listof Assignment)


;; ============================= FUNCTIONS


;; (listof TA) (listof Slot) -> Schedule or false
;; produce valid schedule given TAs and Slots; false if impossible

;(define SOBA (make-ta "Soba" 2 (list 1 3)))
;(define UDON (make-ta "Udon" 1 (list 3 4)))
;(define RAMEN (make-ta "Ramen" 1 (list 2)))

;(define NOODLE-TAs (list SOBA UDON RAMEN))

;; Examples
(check-expect (schedule-tas empty empty) empty)
(check-expect (schedule-tas empty (list 1 2)) false)
(check-expect (schedule-tas (list SOBA) empty) empty)
(check-expect (schedule-tas (list SOBA) (list 1)) (list (make-assignment SOBA 1)))
(check-expect (schedule-tas (list SOBA) (list 2)) false)
(check-expect (schedule-tas (list SOBA) (list 1 3)) (list (make-assignment SOBA 3)
                                                          (make-assignment SOBA 1)))
(check-expect (schedule-tas NOODLE-TAs (list 1 2 3 4))
              (list
               (make-assignment RAMEN 2)
               (make-assignment UDON 4)
               (make-assignment SOBA 3)
               (make-assignment SOBA 1)))
(check-expect (schedule-tas NOODLE-TAs (list 1 2 3 4 5)) false)


;; Stub
;(define (schedule-tas tas slots) empty) ;stub

;; Template
#;(define (schedule-tas talist slotlist) (
                                          local
                                           [
                                            #;(define (removeElement list element) (
                                                                                  local
                                                                                   [
                                                                                    (define (removeElement element previousIndex list) (
                                                                                                                                        cond
                                                                                                                                         [(empty? list) (append previousIndex list)]
                                                                                                                                         [(equal? element (first list)) (append previousIndex (rest list))]
                                                                                                                                         [else (removeElement element (append previousIndex (cons (first list) empty)) (rest list))]  
                                                                                                                                         ))
                                                                                    ]
                                                                                   (removeElement element empty list)
                                                                                   ))
                                            (define (removeElement list element func func2) (
                                                                                  local
                                                                                   [
                                                                                    (define (removeElement element previousIndex list func func2) (
                                                                                                                                        cond
                                                                                                                                         [(empty? list) (append previousIndex list)]
                                                                                                                                         [(equal? (func element) (func2 (first list))) (append previousIndex (rest list))]
                                                                                                                                         [else (removeElement element (append previousIndex (cons (first list) empty)) (rest list) func func2)]  
                                                                                                                                         ))
                                                                                    ]
                                                                                   (removeElement element empty list func func2)
                                                                                   ))
                                         
                                            #;(define (removeTa list ta) (
                                                                        local
                                                                         [
                                                                          (define (removeTa ta previousIndex list) (
                                                                                                                    cond
                                                                                                                     [(empty? list) (append previousIndex list)]
                                                                                                                     [(equal? (ta-name ta) (ta-name (first list))) (append previousIndex (rest list))]
                                                                                                                     [else (removeTa ta (append previousIndex (list (first list))) (rest list))]  
                                                                                                                     ))
                                                                          ]
                                                                         (removeTa ta empty list)
                                                                         ))
                                            (define (removeTa list ta func func2) (
                                                                        local
                                                                         [
                                                                          (define (removeTa ta previousIndex list func func2) (
                                                                                                                    cond
                                                                                                                     [(empty? list) (append previousIndex list)]
                                                                                                                     [(equal? (func ta) (func2 (first list))) (append previousIndex (rest list))]
                                                                                                                     [else (removeTa ta (append previousIndex (list (first list))) (rest list) func func2)]  
                                                                                                                     ))
                                                                          ]
                                                                         (removeTa ta empty list func func2)
                                                                         ))
                                          
                                            (define (scheduleTA ta talist slotlist schedule og) (
                                                                                                 cond
                                                                                                  [(equal? 0 (ta-max ta)) (scheduleTAList (removeElement talist ta ta-name ta-name) slotlist schedule)] ;; when TA is done scheduling.
                                                                                                  [(empty? (ta-avail ta)) (scheduleTAList (removeElement talist ta ta-name ta-name) slotlist schedule)] ;; when TA avail is filled
                                                                                                  [else (
                                                                                                         if
                                                                                                         (member (first (ta-avail ta)) slotlist) ;; if TA has slot matching slotlist
                                                                                                         (scheduleTA (make-ta (ta-name ta) (sub1 (ta-max ta)) (removeElement (ta-avail ta) (first (ta-avail ta)) identity identity)) talist (removeElement slotlist (first (ta-avail ta)) identity identity) (cons (make-assignment og (first (ta-avail ta))) schedule) ta)
                                                                                                         (scheduleTA (make-ta (ta-name ta) (ta-max ta) (removeElement (ta-avail ta) (first (ta-avail ta)) identity identity)) talist slotlist schedule ta) ;; check next avail
                                                                                                         )]
                                                                                                  ))
                                          
                                            (define (scheduleTAList talist slotlist schedule) (
                                                                                               cond
                                                                                                [(empty? talist) (
                                                                                                                  if
                                                                                                                  (empty? slotlist)
                                                                                                                  schedule
                                                                                                                  false
                                                                                                                  )]
                                                                                                #;[else (
                                                                                                         if
                                                                                                         (equal? 0 (ta-max (first talist))) ;; skip TA because theyre filled ;; assume ta list dont include invalid tas
                                                                                                         (scheduleTAList (rest talist) slotlist schedule)
                                                                                                         (scheduleTA (first talist) talist slotlist schedule (first talist)) ;; process TA
                                                                                                         )]
                                                                                                [else (scheduleTA (first talist) talist slotlist schedule (first talist)) ;; process TA
                                                                                                      ]
                                                                                                ))
                                            ]
                                           (scheduleTAList talist slotlist empty)
                                           ))



;; Template REVISED
(define (schedule-tas talist slotlist) (
                                        local
                                         [
                                          (define (removeElement list element func func2) (
                                                                                  local
                                                                                   [
                                                                                    (define (removeElement element previousIndex list func func2) (
                                                                                                                                        cond
                                                                                                                                         [(empty? list) (append previousIndex list)]
                                                                                                                                         [(equal? (func element) (func2 (first list))) (append previousIndex (rest list))]
                                                                                                                                         [else (removeElement element (append previousIndex (cons (first list) empty)) (rest list) func func2)]  
                                                                                                                                         ))
                                                                                    ]
                                                                                   (removeElement element empty list func func2)
                                                                                   ))
                                          (define (scheduleTA ta talist slotlist schedule og) (
                                                                                               cond
                                                                                                [(equal? 0 (ta-max ta)) (scheduleTAList (removeElement talist ta ta-name ta-name) slotlist schedule)] ;; when TA is done scheduling.
                                                                                                [(empty? (ta-avail ta)) (scheduleTAList (removeElement talist ta ta-name ta-name) slotlist schedule)] ;; when TA avail is filled
                                                                                                [(member (first (ta-avail ta)) slotlist) (scheduleTA (make-ta (ta-name ta) (sub1 (ta-max ta)) (removeElement (ta-avail ta) (first (ta-avail ta)) identity identity)) talist (removeElement slotlist (first (ta-avail ta)) identity identity) (cons (make-assignment og (first (ta-avail ta))) schedule) ta)]  ;; if TA has slot matching slotlist
                                                                                                [else (scheduleTA (make-ta (ta-name ta) (ta-max ta) (removeElement (ta-avail ta) (first (ta-avail ta)) identity identity)) talist slotlist schedule ta)] ;; check next avail
                                                                                                ))
                                          
                                          (define (scheduleTAList talist slotlist schedule) (
                                                                                             cond
                                                                                              [(empty? talist) (
                                                                                                                if
                                                                                                                (empty? slotlist)
                                                                                                                schedule
                                                                                                                false
                                                                                                                )]
                                                                                              [else (scheduleTA (first talist) talist slotlist schedule (first talist))] ;Process first TA on list
                                                                                              ))
                                          ]
                                         (scheduleTAList talist slotlist empty)
                                         ))


















