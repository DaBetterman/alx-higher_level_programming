/**
* check_cycle - checks if a linked list is circular or not
* @list: list to check
* Return: 1 (linked list is circular) 0 (no loop detected)
*/

#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *mark_1 = NULL, *mark_2 = NULL;

	mark_1 = mark_2 = list;
	while (list && mark_1 && mark_2 && mark_1->next && mark_2->next)
	{
		mark_1 = mark_1->next;
		mark_2 = mark_2->next->next;
		if (!mark_2 || !mark_1)
			return (0);
		if (mark_2->next == mark_1)
			return (1);
	}
	return (0);
}
