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
	listint_t *curr = *head;
	int arr[1024];
	int len = 0;
	int i;


	if (*head == NULL)
	{
		return (1);
	}

	while (curr != NULL)
	{
		arr[len] = curr->n;
		curr = curr->next;
		len++;
	}

	for (i = 0; i < len / 2; i++)
	{
		if (arr[i] != arr[len - i - 1])
		{
			return (0);
		}
	}

	return (1);

}
