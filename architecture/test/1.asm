default rel
extern exit

section .data
    a db -5         ; Byte
    b db 11        ; Byte
    c db -4        ; Byte
    d dd 5         ; Doubleword
    x dq 20        ; Quadword

; Aufgabe 19
; (a + b) / (c - 2) - d + 2 - x
; Variablen: a, b, c – Byte; d – Doubleword; x – Quadword

section .text

global main
main:
    ; c - 2
    mov al, byte [c]
    sub al, 2
    mov bl, al

    ; a + b
    mov al, byte [a]
    add al, byte [c]

    ; num / denum
    cbw
    idiv bl

    ; + 2
    add al, 2

    ; - d
    cwde
    sub eax, dword [d]

    ; - x
    cdqe
    sub rax, qword [x]

    mov rbx, rax

    ; exit(0)
    mov rcx, 0
    call exit
