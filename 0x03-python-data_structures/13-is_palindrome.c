#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: ptr to the head of the linked list
 *
 * Return: 1 if it is palindrome , 0 otherwise
*/

int is_palindrome(listint_t **head)
{
	listint_t *list_a = *head;
	listint_t *list_b = *head;


	if (*head == NULL)
	{
		return (1);
	}

	while (list_a->next && list_b->next)
	{
		list_a = list_a->next;
		list_b = list_b->next;
	}

	list_a = *head;
	list_b = reverse_listint(&list_b);

	while (list_a && list_b)
	{
		if (list_a->n != list_b->n)
		{
			return (0);
		}
		list_a = list_a->next;
		list_b = list_b->next;
	}
	return (1);
	

}
