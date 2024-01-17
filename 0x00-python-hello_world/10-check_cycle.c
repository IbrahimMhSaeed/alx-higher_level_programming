#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int search_list(listint_t *list, listint_t *original, int i)
{
	listint_t *temp;
	int j;

	j = 0;
	temp = original;

	while (1)
	{
		if (temp == list)
		{
			if (j < i)
				return (1);
			else
				break;
		}
		j++;
		temp = temp->next;
	}
	return (0);

}

int check_cycle(listint_t *list)
{
	listint_t *temp;
	int i;

	i = 0;
	if (list == NULL)
		return (0);

	temp = list;

	while (temp != NULL)
	{
		if (search_list(temp, list, i))
			return (1);

		i++;
		temp = temp->next;
	}
	return (0);
}
