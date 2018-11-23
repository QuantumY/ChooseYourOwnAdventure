#include "stdh.h"
#include "choice.h"

int main()
{
	std::cout << "Hello Testing!!" << std::endl;
	std::cin.ignore();


	choice a;
	choice b;
	choice c;

	a.addChoice(&b);
	a.addChoice(&c);

	a.prompt();
	
	return 0;
}
