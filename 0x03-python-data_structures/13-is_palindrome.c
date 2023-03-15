#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 *
 * @head: Pointer to the address of a listint_t list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *stack = NULL;
    listint_t *current = *head;

    while (current != NULL)
    {
        listint_t *new = malloc(sizeof(listint_t));
        new->n = current->n;
        new->next = stack;
        stack = new;
        current = current->next;
    }

    current = *head;
    while (current != NULL)
    {
        if (current->n != stack->n)
        {
            return (0);
        }
        current = current->next;
        stack = stack->next;
    }

    return (1);
}
