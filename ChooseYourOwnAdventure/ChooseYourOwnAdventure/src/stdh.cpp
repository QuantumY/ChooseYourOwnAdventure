#include "stdh.h"

std::string removews(std::string tr)	//to remove from
{
	std::string out;

	for (int i = 0; i <= tr.length(); i++)
	{
		if (tr[i] != ' ' && tr[i] != '\t' && tr[i] != '\n')
		{
			out += tr[i];
		}
	}

	return out;
}
