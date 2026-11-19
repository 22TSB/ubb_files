section .data
    a dw 4 ; 16
    b db 2 ; 8
    c dw 2 ; 16
    d dd 2 ; 32
    x dq 5 ; 64
    ; (a * a + b / c - 1) / (b + c) + d - x
    ; Variablen: a – Word; b – Byte; c – Word; d – Doubleword; x –
    ; Quadword
    ; ------------------------------------------

section .text
    global main

main:
    ; calc b / c
    mov ax, 0 ; clear ax
    mov al, [b] ; ax = 2
    mov dx, 0 ; prep dx for 16 bit div
    div word [c] ; ax = dx:ax / c = 2 / 2 = 1
    mov di, ax ; save temp div res

    ; b + c
    mov bx, 0 ; clear bx
    mov bl, [b] ; bx = 2
    add bx, [c] ; bx = 2 + 2 = 4
    mov si, bx ; save temp save res

    ; calc (a * a + b / c - 1)
    mov ax, [a] ; ax = 4
    mul word [a] ; dx:ax = 4 * 4 = 16 (ax = 16, dx = 0)
    
    add ax, di ; add (b / c) from di. ax = 16 + 1 = 17
    sub ax, 1 ; ax = 17 - 1 = 16, num iz ready

    ; num / denum
    mov dx, 0 ; clear dx before div dx:ax
    div si ; ax = 16 / 4 = 4 (quotient is in ax)

    ; quoetient + d - x
    mov rbx, 0 ; clear rbx
    mov bx, ax ; rbx = 4

    ; add d (32 bit)
    mov rdx, 0 ; clear rdx
    mov edx, [d] ; rdx = 2
    add rbx, rdx ; rbx = 4 + 2

    ; sub x (64 bit)
    sub rbx, [x] ; rbx = 6 - 5 = 1
      

    ; exit (0)
    push dword 0
    call [exit]
