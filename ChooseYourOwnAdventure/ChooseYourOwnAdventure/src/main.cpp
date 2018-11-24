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

	ba.id = 'a';
	bb.id = 'b';

	ca.id = 'a';
	cb.id = 'b';

	b.id = 'a';
	c.id = 'b';

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
