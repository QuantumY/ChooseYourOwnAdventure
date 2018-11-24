#include "stdh.h"
#include "choice.h"

int main()
{	
	choice a;
	choice b;
	choice c;

	b.title = "hello from b!";
	c.title = "hello from c!";

	b.id = "a.b";
	c.id = "a.c";

	a.addChoice(&b);
	a.addChoice(&c);

	choice* next_choice;

	next_choice = a.prompt();

	while (true)
	{
		next_choice = next_choice->prompt();
	}

	return 0;
}
