section .data
    a dw 7; 16
    b db 2 ; 8
    e dd 5 ; 32
    x dq 10 ; 64

section .text
    global main

main:
    ; calc (b * b) into cx
    mov al, [b] ; al = 2
    mul byte [b] ; ax = al * [b] => ax = al * 2 => ax = 4
    mov cx, ax ; temp cx = ax => cx = 4

    ; calc (2 * a - b)
    mov ax, 2 ; ax = 2
    mul word [a] ; dx:ax = 2 * 7 = 14 (dx = 0, ax = 14)

    mov dx, 0 ; clear dx
    mov dl, [b] ; dx = 2
    sub ax, dx ; ax - dx = 14 - 2 = 12 

    ; integar div (2 * a - b) / (b * b)
    mov dx, 0 ; dx = 0
    div cx ; ax = dx:ax / cx = 12 / 4 = 3
    mov cx, ax ; cx = ax = 3

    ; x - b + 8 + (3) + e
    ; x - b
    mov rbx, [x] ; rbx = x
    mov rdx, 0 ; rdx = 0
    mov dl, [b] ; rdx = 2
    sub rbx, rdx ; rbx = 10 - 2 = 8

    ; add 8
    add rbx, 8 ; rbx = 8 + 8 = 16

    ; add cx aka (3)
    mov rdx, 0 ; rdx = 0
    mov dx, cx ; rdx = 3 
    add rbx, rdx ; rbx = 16 + 3 = 19 

    ; add e 
    mov rdx, 0 ; rdx = 0
    mov edx, [e] ; edx = 5
    add rbx, rdx ; rbx = 19 + 5 = 24

    ret
