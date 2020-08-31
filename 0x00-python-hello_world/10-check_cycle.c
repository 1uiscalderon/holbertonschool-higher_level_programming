#include "lists.h"

/**
 * check_cycle -  Checks if a singly linked list has a cycle.
 * @list: Pointer to elements in the list
 * Return: 1 if is true, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle = list, *rabbit = list;

	if (!list)
		return (0);

		while (turtle && rabbit && rabbit->next)
	{
		rabbit = rabbit->next->next;
		turtle = turtle->next;
		if (turtle == rabbit)
			return (1);
	}
	return (0);
}
