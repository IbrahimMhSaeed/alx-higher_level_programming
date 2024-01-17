#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *temp;

	if (list == NULL)
		return (0);

	temp = list;
	temp = temp->next;

	while (temp != NULL)
	{
		if (temp == list)
			return (1);

		temp = temp->next;
	}
	return (0);
}
