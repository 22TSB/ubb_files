global main

section .data

section .text
main:
    ; Setup Number 1 (0005FFFFh) into DX:AX
    mov dx, 0005h    ; High part
    mov ax, 0FFFFh   ; Low part

    ; Setup Number 2 (00020002h) into CX:BX
    mov cx, 0002h    ; High part
    mov bx, 0002h    ; Low part

    ; Execute
    add ax, bx       ; FFFFh + 0002h = 0001h. 
                     ; This overflows the 16-bit limit! Carry Flag (CF) = 1.
    adc dx, cx       ; 0005h + 0002h + 1 (from CF) = 0008h.

    ; Final Result in DX:AX is 00080001h.
    ret
