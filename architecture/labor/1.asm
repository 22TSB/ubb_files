default rel
extern exit

section .data
    a dw 4        ; Word
    b db 10       ; Byte
    c dw 5        ; Word
    d dd -20      ; Doubleword 
    x dq 10       ; Quadword 

; Aufgabe 16
; (a * a + b / c - 1) / (b + c) + d - x
; Variablen: a – Word; b – Byte; c – Word; d – Doubleword; x –
; Quadword

section .text

global main
main:
    ; (b / c)
    mov al, [b]
    cbw
    cwd
    idiv word [c]
    cwde
    mov ecx, eax

    ; (a * a)
    mov ax, [a]
    cwde
    imul eax, eax

    ; (a*a + b/c - 1)
    add eax, ecx
    sub eax, 1
    mov ecx, eax

    ; (b + c)
    mov al, [b]
    cbw
    add ax, [c]
    cwde
    mov ebx, eax

    ; (a*a + b/c - 1) / (b+c)
    mov eax, ecx
    cdq
    idiv ebx

    ; ... + d
    add eax, [d]

    ; ... - x (64-bit boundary)
    cdqe                  ; Sign-extend EAX into RAX for 64-bit operations
    sub rax, qword [x]    ; Subtract the Quadword

    ; Store the final result in RBX
    mov rbx, rax          

    ; exit(0)
    mov rcx, 0            ; 64-bit calling convention parameter for exit
    call exit
