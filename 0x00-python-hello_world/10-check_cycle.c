#include "lists.h"

/**
 * check_cycle - checks if singly linked list has cycle in it
 * @list: A ptr to the list
 * Return: 0 if no cycle, 1 if there is cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *num = list;
	listint_t *set = list;

	while (list && num && num->next)
	{
		list = list->next;
		num = num->next->next;

		if (list == num)
		{
			list = set;
			set =  num;
			while (1)
			{
				num = set;
				while (num->next != list && num->next != set)
				{
					num = num->next;
				}
				if (num->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
