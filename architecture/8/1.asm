default rel
extern exit

section .data
    x db 'ac', 10
    y db 17
    c db 0

section .text

global main
main:
    mov ax, [y]
    mov bl, 10
    div bl ; al = 1 : ah = 7

    mov [y], al ; n /= 10
    add ah, '0'
    mov [c], ah

    mov rax, 1
    mov rdi, 1
    mov rsi, c
    mov rdx, 1
    syscall
    ;;;;;;;
    mov al, [y]
    add al, '0'
    mov [c], al

    mov rax, 1
    mov rdi, 1
    mov rsi, c
    mov rdx, 1
    syscall



    ; read(0, x, 3)
    ; mov rax, 0 ; write
    ; mov rdi, 0 ; fd keyb
    ; mov rsi, x ; pointer *x "ac"
    ; mov rdx, 3 ; len x
    ; syscall

    ; write(1, x, 2)
    ; mov rax, 1 ; write
    ; mov rdi, 1 ; fd screen
    ; mov rsi, x ; pointer *x "ac"
    ; mov rdx, 3 ; len x
    ; syscall
    
    ; exit(0)
    ; call exit

    ; ret
    mov rax, 60 ; exit()
    mov rdi, 0 ; return code
    syscall
