#pragma once

#include "stdh.h"

class choice
{ 
public:
	char id;			//choice id
	std::string title;	//choice title
	std::string text;	//choice text
	std::vector<choice*> choices;

	choice();
	choice* prompt();
	void addChoice(choice*);
	~choice();

private:
};
