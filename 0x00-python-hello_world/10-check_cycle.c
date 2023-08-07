#include "lists.h"
#include <stdlib.h>


/**
 * check_cycle -  checks if a singly linked list has a cycle in it.
 * @list: list
 *
 * Return: 0 if no cycle , 1 if there is cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *pre = NULL;
	listint_t *cur = NULL;

	if (list == NULL)
	{
		return (0);
	}


	pre = list;
	cur = list;

	while (cur != NULL && pre != NULL)
	{
		cur = cur->next;
		if (cur == pre)
		{
			return (1);
		}
		pre = pre->next;
		cur = cur->next;

	}

	return (0);
}
