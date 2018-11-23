#include "stdh.h"
#include "choice.h"

int main()
{	
	choice a;
	choice b;
	choice c;

	b.title = "hello from b!";
	c.title = "hello from c!";

	b.id = 'a';
	c.id = 'b';

	a.addChoice(&b);
	a.addChoice(&c);

	a.prompt();

	return 0;
}
