#include <stdlib.h>
#include "lists.h"
/**
  * insert_node - insert a num into a singly linked list.
  * @head: ptr to the ptr of list.
  * @number: numb to be inserted.
  *
  * Return: Address f for new node, NULL if not success.
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *set, *new;

	new = malloc(sizeof(listint_t));
	if (new != NULL)
	{
		new->n = number;
		if (*head == NULL || (*head)->n >= new->n)
		{
			new->next = *head;
			*head = new;
			return (new);
		}
		else
		{
			set = *head;
			while (set->next != NULL && set->next->n < new->n)
				set = set->next;
			new->next = set->next;
			set->next = new;
			return (new);
		}
	}
	return (NULL);
}
