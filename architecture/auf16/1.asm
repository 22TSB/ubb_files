default rel
extern exit

section .data
    a dw -5         ; Word
    b db 10        ; Byte
    c dw -5        ; Word
    d dd 5         ; Doubleword
    x dq 20        ; Quadword

; Aufgabe 16
; (a * a + b / c - 1) / (b + c) + d - x
; Variablen: a – Word; b – Byte; c – Word; d – Doubleword; x – Quadword

section .text

global main
main:
    ; a * a
    mov al, byte [a]
    imul byte [a]
    mov bx, ax 

    ; b / c
    mov al, byte [b] 
    cbw
    cwd
    idiv word [c]

    ; subtract 1
    sub ax, 1 
    
    ; add ax to bx
    add bx, ax

    ; b + c 
    mov al, byte [b]
    cbw
    add ax, word [c]
    
    ; ax = b + c 
    ; bx = (a * a + b / c - 1) 
    ; swap
    mov cx, ax
    mov ax, bx
    mov bx, cx
    ; ax = (a * a + b / c - 1) 
    ; bx = b + c 

    ; num / denum
    cwd
    idiv bx

    ; ax + d
    cwde
    add eax, dword [d]

    ; - x
    cdqe
    sub rax, qword [x]

    mov rbx, rax

    ; exit(0)
    mov rcx, 0
    call exit
