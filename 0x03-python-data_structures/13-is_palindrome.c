#include "lists.h"

/**
 * reverse_listint - Reverses a singly-linked listint_t list
 * @head: A pointer to star node of the list to reverse
 *
 * Return: A pointer to the head of reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *new = *head, *prev, *next = NULL;

	while (new)
	{
		next = new->next;
		new->next = prev;
		prev = new;
		new = next;
	}

	*head = prev;
	return (*head);
}

int is_palindrome(listint_t **head)
{
	listint_t *tmp, *rev, *mind;
	size_t size = 0, r;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tmp = *head;
	while (tmp)
	{
		size++;
		tmp = tmp->next;
	}

	tmp = *head;
	for (r = 0; r < (size / 2) - 1; r++)
		tmp = tmp->next;

	if ((size % 2) == 0 && tmp->n != tmp->next->n)
		return (0);

	tmp = tmp->next->next;
	rev = reverse_listint(&tmp);
	mind = rev;

	tmp = *head;
	while (rev)
	{
		if (tmp->n != rev->n)
			return (0);
		tmp = tmp->next;
		rev = rev->next;
	}
	reverse_listint(&mind);

	return (1);
}
