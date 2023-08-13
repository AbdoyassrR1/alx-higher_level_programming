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
	listint_t *a = *head;
	listint_t *b = *head;

	if (*head == NULL)
		return (1);

	while (b && b->next && b->next->next)
	{
		a = a->next;
		b = b->next->next;
	}

	a = reverse_listint(&a);
	b = *head;
	while (a && b)
	{
		if (a->n != b->n)
			return (0);
		a = a->next;
		b = b->next;
	}

	return (1);
}

/**
 * reverse_listint - function that reverses a listint_t linked list.
 * @head: pointer to the first element in the list
 * Return: a pointer to the first node of the reversed list
*/

listint_t *reverse_listint(listint_t **head)
{
	listint_t *next = NULL;
	listint_t *prev = NULL;


	while (*head != NULL)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}
	*head = prev;

	return (*head);
}
