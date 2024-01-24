#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * mem_error - print allocation error message
 * Return: always -1 (Fail)
 */

int mem_error(void)
{
	perror("Error: Memory allocation");
	return (-1);
}

/**
 * mem_error_free - print allocation error and free array
 * @arr: array to be freed
 * Return: always -1 (Fail
 */

int mem_error_free(int *arr)
{
	perror("Error: Memory allocation");
	free(arr);
	return (-1);
}
/**
 * is_palindrome - check if a list is palindrome or not
 * @head: head of linked list
 * Return 1 Palindrome || 0 not Palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int count;
	int *arr;
	int size;
	int st, end;

	count = 0;
	temp = *head;
	size = 1024;
	arr = malloc(sizeof(int) * size);
	if (arr == NULL)
		return (mem_error());
	while (temp != NULL)
	{
		if (count >= size)
		{
			size *= 2;
			arr = realloc(arr, (sizeof(int) * size));
			if (arr == NULL)
				return (mem_error_free(arr));
		}
		arr[count] = temp->n;
		count++;
		temp = temp->next;
	}
	if (count == 0)
	{
		free(arr);
		return (0);
	}
	st = 0;
	end = count - 1;
	while (st < end)
	{
		if (arr[st] != arr[end])
		{
			free(arr);
			return (0);
		}
		end--;
		st++;
	}

	free(arr);
	return (1);

}
