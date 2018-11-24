#include "stdh.h"
#include "choice.h"

int main()
{	
	choice a;
	choice b;
	choice c;

	choice ba;
	choice bb;

	choice ca;
	choice cb;

	ba.title = "START->a->a";
	bb.title = "START->a->b";

	ca.title = "START->b->a";
	cb.title = "START->b->b";

	b.title = "hello from b!";
	c.title = "hello from c!";

	b.id = "a.b";
	c.id = "a.c";

	b.addChoice(&ba);
	b.addChoice(&bb);

	c.addChoice(&ca);
	c.addChoice(&cb);

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
