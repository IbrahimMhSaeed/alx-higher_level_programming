#include "lists.h"

/**
 * insert_node - insert node in sorted linked list
 * @head: head of list
 * @number: number to be inserted in list
 * Return: address of new node (Success) || NULL (fail)
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *before;
	listint_t *current;
	listint_t *answer;

	before = NULL;
	current = *head;

	if (*head == NULL)
		return (NULL);

	while (current != NULL)
	{
		if (number <= current->n)
		{
			answer = malloc(sizeof(listint_t));
			if (answer == NULL)
				return (NULL);
			answer->n = number;
			if (before == NULL)
			{
				answer->next = *head;
				*head = answer;
				return (answer);
			}
			answer->next = current;
			before->next = answer;
			return (answer);

		}

		current = current->next;
		if (before == NULL)
			before = *head;
		else
			before = before->next;
	}
	answer = add_nodeint_end(head, number);

	return (answer);
}
