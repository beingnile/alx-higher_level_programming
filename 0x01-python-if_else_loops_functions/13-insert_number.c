#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list
 *
 * @head: Pointer to pointer of the first node of listint_t list
 * @number: Value to be included in node to insert
 *
 * Return: Address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *current;
    listint_t *new;
    listint_t *temp;

    current = *head;
    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = number;
    new->next = NULL;

    if (*head == NULL)
        *head = new;
    else
    {
        while (current->next != NULL)
        {
            if (current->next->n > number)
            {
                temp = current->next;
                current->next = new;
                new->next = temp;
                break;
            }
            current = current->next;
        }
    }

    return (new);
}
